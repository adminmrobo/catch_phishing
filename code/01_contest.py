# -*- coding: utf-8 -*-
"""피싱 사이트 탐지 연구실 — 모델 대회 재현 코드
사용법:  python code/01_contest.py [CSV 경로 또는 URL]  [결과 JSON 경로]
기본 데이터: 이 저장소의 data/website_phishing.csv
"""
import sys, json, itertools
import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline

SEED = 42
URL = 'https://raw.githubusercontent.com/adminmrobo/catch_phishing/main/data/website_phishing.csv'
src = sys.argv[1] if len(sys.argv) > 1 else URL
out = sys.argv[2] if len(sys.argv) > 2 else None
df = pd.read_csv(src)
FEAT = [c for c in df.columns if c != 'Result']
R = {}

# 1) 데이터 기본 점검
R['shape'] = list(df.shape)
R['nulls'] = int(df.isnull().sum().sum())
R['value_table'] = {c: {str(k): int(v) for k, v in df[c].value_counts().sort_index().items()} for c in df.columns}
R['dup_full'] = int(df.duplicated().sum())
R['unique_rows'] = int(df.drop_duplicates().shape[0])
R['dup_feat'] = int(df.duplicated(subset=FEAT).sum())
R['unique_feat'] = int(df.drop_duplicates(subset=FEAT).shape[0])
kinds = df.groupby(FEAT)['Result'].nunique()
R['conflict_groups'] = int((kinds > 1).sum())
conf_keys = set(kinds[kinds > 1].index)
R['conflict_rows'] = int(df[FEAT].apply(tuple, axis=1).isin(conf_keys).sum())

# 2) 이상탐지
X0 = df[FEAT]
Q1, Q3 = X0.quantile(.25), X0.quantile(.75); IQR = Q3 - Q1
R['iqr_out'] = {c: int(((X0[c] < Q1[c] - 1.5 * IQR[c]) | (X0[c] > Q3[c] + 1.5 * IQR[c])).sum()) for c in FEAT}
z = (X0 - X0.mean()) / X0.std()
R['z_out'] = {c: int((z[c].abs() > 3).sum()) for c in FEAT}
R['z_ip1'] = round(float(z.loc[X0['having_IP_Address'] == 1, 'having_IP_Address'].iloc[0]), 3)
iso = IsolationForest(contamination=0.05, random_state=SEED).fit_predict(X0)
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05).fit_predict(X0)
R['iso_n'] = int((iso == -1).sum()); R['lof_n'] = int((lof == -1).sum()); R['both_n'] = int(((iso == -1) & (lof == -1)).sum())
R['iso_ratio_by_class'] = {str(k): round(float(v), 4) for k, v in pd.Series(iso == -1).groupby(df['Result']).mean().items()}

# 3) 탐색: 값별 정답 비율, 상관
cond = {}
for c in FEAT:
    t = pd.crosstab(df[c], df['Result'])
    cond[c] = {str(v): {str(k): int(t.loc[v, k]) if k in t.columns else 0 for k in [-1, 0, 1]} for v in t.index}
R['cond'] = cond
R['corr_result'] = {c: round(float(df[c].corr(df['Result'])), 4) for c in FEAT}
R['class_mean'] = {str(k): {c: round(float(v), 4) for c, v in g[FEAT].mean().items()} for k, g in df.groupby('Result')}
R['result_counts'] = {str(k): int(v) for k, v in df['Result'].value_counts().sort_index().items()}

# 4) 전처리: -1(피싱)->0, 0(의심)->1, 1(정상)->2
y = df['Result'].map({-1: 0, 0: 1, 1: 2}); X = X0.copy()
MODELS = {
    'LogisticRegression': lambda: LogisticRegression(max_iter=1000, random_state=SEED),
    'DecisionTree': lambda: DecisionTreeClassifier(random_state=SEED),
    'KNN': lambda: KNeighborsClassifier(n_neighbors=5),
    'SVM': lambda: SVC(kernel='rbf', random_state=SEED),
    'RandomForest': lambda: RandomForestClassifier(n_estimators=100, random_state=SEED),
    'GradientBoosting': lambda: GradientBoostingClassifier(random_state=SEED),
    'AdaBoost': lambda: AdaBoostClassifier(random_state=SEED),
}

# 5) 원본 방식(누수): SMOTE 먼저 -> 나누기
Xs, ys = SMOTE(random_state=SEED).fit_resample(X, y)
a, b, c_, d = train_test_split(Xs, ys, test_size=0.2, random_state=SEED)
R['leaky'] = {}
for n, f in MODELS.items():
    p = f().fit(a, c_).predict(b)
    R['leaky'][n] = {'acc': round(accuracy_score(d, p), 4), 'f1': round(f1_score(d, p, average='macro'), 4)}
R['leaky_shape'] = list(Xs.shape)

# 6) 올바른 방식: 나누기(stratify) -> 학습용에만 SMOTE
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=SEED, stratify=y)
Xtr_s, ytr_s = SMOTE(random_state=SEED).fit_resample(Xtr, ytr)
R['split'] = {'train': {str(k): int(v) for k, v in ytr.value_counts().sort_index().items()},
              'train_smote': {str(k): int(v) for k, v in ytr_s.value_counts().sort_index().items()},
              'test': {str(k): int(v) for k, v in yte.value_counts().sort_index().items()}}
tu = Xtr.drop_duplicates()
seen = Xte.reset_index().rename(columns={'index': 'rid'}).merge(tu, on=FEAT, how='inner')['rid'].unique()
seen_mask = Xte.index.isin(seen)
R['seen_n'] = int(seen_mask.sum()); R['unseen_n'] = int((~seen_mask).sum())
fitted = {}; R['correct'] = {}
for n, f in MODELS.items():
    m = f().fit(Xtr_s, ytr_s); fitted[n] = m; p = m.predict(Xte)
    R['correct'][n] = {
        'acc': round(accuracy_score(yte, p), 4),
        'prec': round(precision_score(yte, p, average='macro'), 4),
        'rec': round(recall_score(yte, p, average='macro'), 4),
        'f1': round(f1_score(yte, p, average='macro'), 4),
        'cm': confusion_matrix(yte, p).tolist(),
        'rec_cls': [round(v, 4) for v in recall_score(yte, p, average=None)],
        'prec_cls': [round(v, 4) for v in precision_score(yte, p, average=None)],
        'f1_cls': [round(v, 4) for v in f1_score(yte, p, average=None)],
        'acc_seen': round(accuracy_score(yte[seen_mask], p[seen_mask]), 4),
        'acc_unseen': round(accuracy_score(yte[~seen_mask], p[~seen_mask]), 4),
    }

# 7) 5겹 교차검증 (각 겹의 학습 부분에만 SMOTE)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
R['cv'] = {}
for n, f in MODELS.items():
    s = cross_val_score(Pipeline([('smote', SMOTE(random_state=SEED)), ('model', f())]), X, y, cv=cv, scoring='accuracy')
    s2 = cross_val_score(Pipeline([('smote', SMOTE(random_state=SEED)), ('model', f())]), X, y, cv=cv, scoring='f1_macro')
    R['cv'][n] = {'mean': round(s.mean(), 4), 'std': round(s.std(), 4), 'folds': [round(v, 4) for v in s],
                  'f1_mean': round(s2.mean(), 4), 'f1_std': round(s2.std(), 4)}

# 8) 출전 모델 해부
lr, dt, gb = fitted['LogisticRegression'], fitted['DecisionTree'], fitted['GradientBoosting']
R['lr_coef'] = {cls: {c: round(float(w), 4) for c, w in zip(FEAT, lr.coef_[i])} for i, cls in enumerate(['phishy', 'suspicious', 'legit'])}
R['lr_intercept'] = [round(float(v), 4) for v in lr.intercept_]
R['dt_depth'] = int(dt.get_depth()); R['dt_leaves'] = int(dt.get_n_leaves())
R['imp_dt'] = {c: round(float(v), 4) for c, v in zip(FEAT, dt.feature_importances_)}
R['imp_gb'] = {c: round(float(v), 4) for c, v in zip(FEAT, gb.feature_importances_)}
R['gb_staged'] = [round(accuracy_score(yte, p), 4) for p in gb.staged_predict(Xte)]
t3 = DecisionTreeClassifier(max_depth=3, random_state=SEED).fit(Xtr_s, ytr_s)
R['dt3_acc'] = round(accuracy_score(yte, t3.predict(Xte)), 4)
tr = t3.tree_
R['dt3'] = [{'f': (FEAT[tr.feature[i]] if tr.children_left[i] != -1 else None), 't': round(float(tr.threshold[i]), 2),
             'l': int(tr.children_left[i]), 'r': int(tr.children_right[i]),
             'v': [int(round(x)) for x in (tr.value[i][0] * tr.n_node_samples[i])], 'n': int(tr.n_node_samples[i])} for i in range(tr.node_count)]
dacc = {}
for k in range(1, 16):
    m = DecisionTreeClassifier(max_depth=k, random_state=SEED).fit(Xtr_s, ytr_s)
    dacc[k] = [round(accuracy_score(ytr_s, m.predict(Xtr_s)), 4), round(accuracy_score(yte, m.predict(Xte)), 4)]
R['dt_depth_curve'] = dacc

# 9) 모든 단서 조합(3^7 x 2 x 2 = 8,748개)에 대한 세 출전 모델의 판정표
vals = [sorted(df[c].unique().tolist()) for c in FEAT]
grid = pd.DataFrame(list(itertools.product(*vals)), columns=FEAT)
R['grid_vals'] = vals
for n, key in [('LogisticRegression', 'lr'), ('DecisionTree', 'dt'), ('GradientBoosting', 'gb')]:
    m = fitted[n]
    R['grid_' + key] = ''.join(str(int(v)) for v in m.predict(grid))
    pr = m.predict_proba(grid)
    R['gridp_' + key] = ''.join(str(min(9, int(v * 10))) for v in pr.max(axis=1))
R['test_idx'] = [int(i) for i in Xte.index]

print(json.dumps({k: R[k] for k in ['shape', 'dup_full', 'unique_rows', 'conflict_groups', 'seen_n', 'unseen_n']}, ensure_ascii=False))
for n in MODELS:
    print(f"{n:20s} leaky {R['leaky'][n]['acc']:.4f} | acc {R['correct'][n]['acc']:.4f} f1 {R['correct'][n]['f1']:.4f} "
          f"| cv {R['cv'][n]['mean']:.4f}±{R['cv'][n]['std']:.4f} | seen {R['correct'][n]['acc_seen']:.4f} unseen {R['correct'][n]['acc_unseen']:.4f}")
if out:
    json.dump(R, open(out, 'w'), ensure_ascii=False)
