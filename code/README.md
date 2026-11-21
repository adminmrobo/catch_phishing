# code

| 파일 | 하는 일 |
|---|---|
| `01_contest.py` | 이 시리즈의 모든 숫자를 다시 만듭니다: 데이터 점검, 이상탐지(IQR·Z·Isolation Forest·LOF), 예선 방식(SMOTE → 나누기)과 본선 방식(나누기 → 학습용만 SMOTE)의 모델 7개 점수, 5겹 교차검증, 이미 본/처음 보는 단서 조합 정확도, 세 출전 모델의 판정표(8,748개 조합) |
| `requirements.txt` | 해설의 숫자를 계산한 버전 |

```bash
pip install -r code/requirements.txt
python code/01_contest.py                                   # 이 저장소의 데이터 주소에서 읽기
python code/01_contest.py data/website_phishing.csv data/results.json   # 내려받은 파일로, 결과 저장
```

버전이 다르면 SMOTE가 만드는 점과 일부 모델 계산이 달라 소수점 셋째 자리부터 조금 달라질 수 있습니다. 강의 노트북(Colab) 값과의 대조표는 5장 5-6에 있습니다.
