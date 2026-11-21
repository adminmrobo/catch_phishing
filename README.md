# 가짜 사이트를 잡아라 — 피싱 사이트 탐지 연구실 (catch_phishing_lab)

> AI를 활용한 피싱 사이트 탐지 · 연구실 모델 대회 해설 (6장 + 목차)

UCI Website Phishing 데이터(웹사이트 1,353개, 단서 9개, 정답 3종)로 **피싱 사이트 탐지 모델 대회**를 엽니다. 인턴 시아(로지스틱 회귀) · 인턴 모아(의사결정나무) · 조수 하루(그래디언트 부스팅)가 출전하고, 박사(심사위원장) · 주판봇(채점) · 초파리 연구원(검증)이 심사하며, 미공개 식구 X1~X3이 방청석에서 질문 카드를 듭니다. 단서 아홉 개를 하나씩 쉽게 풀고, 데이터를 검진하고, 예선의 데이터 누수를 적발한 뒤, 네 라운드로 심사하고 직접 사이트를 넣어 봅니다.

- 사이트: https://adminmrobo.github.io/catch_phishing/
- 저장소: https://github.com/adminmrobo/catch_phishing
- 분야: 인공지능 (지도학습 · 분류 · 평가)

글 · 안상선 (www.ahnboat.xyz) · (주)M-Robo 대표

## 목차

| 장 | 파일 | 중챕터 |
|---|---|---|
| 목차 | `index.html` | 3줄 요약 · 대회의 식구 · 대회 안내 · 목차 · 데이터와 저장소 |
| 1 피싱 사이트와 대회 개막 | `ch1_phishing.html` | 피싱의 흔적 · 규칙 하나로 잡아 보기 · 정답 세 가지 · 시험지 봉인과 층화 |
| 2 아홉 가지 단서 | `ch2_clues.html` | 변수 사전 · 페이지가 하는 일 · 주소와 신분증 · 평판과 나이 · 설명서와 반대인 방향 · 대결(단서 하나 vs 아홉) |
| 3 데이터 건강검진 | `ch3_checkup.html` | 빈 값·허용값 · IQR과 Z(대결: 이상치를 지우면?) · 똑같은 행 46%와 정답 충돌 · Isolation Forest·LOF |
| 4 출전 모델과 예선 | `ch4_models.html` | SMOTE · 시아의 로지스틱 회귀 · 모아의 의사결정나무 · 하루의 그래디언트 부스팅 · 예선 누수 적발 |
| 5 본선 · 심사 · 시상 | `ch5_final.html` | 정확도 · 의심 사이트(macro F1) · 5겹 교차검증 · 처음 보는 단서 조합 · 시상식 · 참고 기록 |
| 6 실전 연습장 | `ch6_practice.html` | 사이트 검사 창구 · 검사 라인 · Colab에서 다시 치르기 · 현장에 옮기면 |

## 대회 결과 (코드 재현)

| 출전자 | 모델 | 정확도 | macro F1 | 교차검증 평균 | 처음 보는 조합 |
|---|---|---|---|---|---|
| 조수 하루 (우승) | 그래디언트 부스팅 | 0.9188 | 0.8817 | 0.9046 | 0.8367 |
| 인턴 모아 | 의사결정나무 | 0.8856 | 0.8586 | 0.8744 | 0.8061 |
| 인턴 시아 | 로지스틱 회귀 | 0.8081 | 0.7179 | 0.7827 | 0.7347 |

의심 사이트 F1은 모아(0.7907)가, 교차검증 흔들림은 시아(표준편차 0.0073)가 가장 좋았습니다. 원래 노트북 순서(SMOTE를 나누기 전에 적용)의 예선 기록은 데이터 누수로 무효 처리했습니다.

## 폴더

```
index.html, ch1~ch6 *.html   해설 페이지 (외부 라이브러리 없음, 글꼴만 외부)
data/website_phishing.csv    데이터 (UCI Website Phishing, 1,353행 × 10열, 값 그대로)
data/variable_dictionary.csv 변수 사전 (변수 · 의미 · 관찰된 값)
data/results.json            code/01_contest.py 결과 (모든 페이지 숫자의 원본)
code/                        재현 코드 · requirements · 설명
img/                         표지 그림 자리 (cover_00~06.webp를 넣으면 대체 표지 대신 보임)
kg/{페이지}/                 지식 색인 원본 kg.json · refs.json · meta.json
docs/                        표지 지시문(Genspark용) · 이미지 제작 명세서 · 검수 보고서
review_log.json              검수 기록 (페르소나 점수)
cover_manifest.json          표지·온톨로지 현황 (ahnboat_lab_cover_status가 수집)
KG_new_ids.json              시리즈 등록부에 더할 새 개념 ID
```

## 데이터

원래 실습은 다른 저장소의 CSV를 불러왔지만, 이 시리즈부터는 이 저장소에 같은 데이터를 옮겨 두고 여기서 읽습니다.

```python
import pandas as pd
url = 'https://raw.githubusercontent.com/adminmrobo/catch_phishing/main/data/website_phishing.csv'
df = pd.read_csv(url)   # (1353, 10)
```

> 출처: Abdelhamid, N. (2014). Website Phishing [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5B301 — 라이선스 CC BY 4.0 (출처 표시 조건으로 공유·변형 가능)
>
> 소개 논문: Abdelhamid, N., Ayesh, A., & Thabtah, F. (2014). Phishing detection based Associative Classification data mining. *Expert Systems with Applications*, 41(13), 5948–5959. https://doi.org/10.1016/j.eswa.2014.03.019

## 숫자 표시 원칙

- 데이터 파일로 직접 센 값과 코드를 다시 돌린 값은 "코드 재현"(scikit-learn 1.9.1 · imbalanced-learn 0.14.2), 강의 노트북에 찍혀 있던 값은 "강의 노트북 값", 설명을 위해 만든 값과 그림은 "설명용"으로 표시했습니다.
- 버전 차이로 노트북 값과 소수점 셋째 자리부터 다른 곳이 있습니다. 대조표는 5장 5-6에 있습니다. 노트북에서 로지스틱 회귀 0.8007 · 에이다부스트 0.8081이던 정확도가 재현에서는 0.8081 · 0.8007로 서로 바뀌어 나왔고, 원인은 확인하지 못했습니다.
- 데이터 설명서는 단서 값 1을 "정상 쪽 신호"로 적었지만, 이 데이터에서는 web_traffic만 그 방향이고, 예/아니오 단서인 having_IP_Address를 빼면 일곱 단서가 반대 방향(상관계수 음수)입니다. 해설은 원인을 단정하지 않고 관찰만 적었습니다(2장 2-4).
- 페이지 속 사이트 화면과 이름(연구실은행 · 연구실상점 · lab-bank.example 등)은 모두 지어낸 것입니다.

## 저작권

캐릭터 이름·설정·그림의 저작권은 안상선에게 있으며 허락 없이 쓸 수 없습니다. 데이터는 원 출처의 CC BY 4.0을 따릅니다.
