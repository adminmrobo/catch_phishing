# 표지 지시문 모음 — 가짜 사이트를 잡아라 (피싱 사이트 탐지 연구실)

표지 7장(목차 1 + 장 6)을 Genspark 등 이미지 생성 도구에 그대로 붙여 넣는 지시문입니다. **목차 표지(00)를 먼저 받아** 그림체를 확인한 뒤, 나머지 요청에 그 그림을 참고 이미지로 함께 올립니다.

| 공통 | 내용 |
|---|---|
| 판 | L (16:9, 가로 1920 이상) → 빌드 1600×900 WebP |
| 그림체 | **16비트 RPG풍 픽셀아트 (필수)** — 네모 픽셀이 보이는 굵은 외곽선, 2~3단계 명암. 매끈한 일러스트·벡터·3D·수채화 금지 |
| 저장 이름 | `img/cover_00.webp` ~ `img/cover_06.webp` (페이지가 이 이름을 자동으로 찾아 대체 표지 대신 보여 줌) |
| 참고 이미지 | 네 캐릭터 기본 그림 (GitHub `adminmrobo/fruitfly-lab-expressions`), 4·5장은 인턴 시아·모아 그림도 |
| 배경 | 낮의 연구실 (흰 벽, 큰 창, 자연광). 밤·네온 금지 |
| 금지 | 글자·숫자·물음표·로고, 실제 은행·쇼핑몰·브랜드 로고나 화면, 하얀 둥근 로봇(Money-Robo), 무기·피 |
| 출연 | 모든 표지에 박사·조수·초파리·주판봇. 4·5장은 출전자인 인턴 시아·모아, 5장은 방청석 실루엣 X1~X3도 |

## 받은 뒤 처리
1. PNG/JPG를 1600×900 WebP(220KB 이하)로 바꿔 `img/cover_NN.webp`로 저장
2. 같은 그림을 3:2로 잘라 `img/thumb_NN.webp`, 1200×630으로 잘라 `img/og_NN.webp`
3. `cover_manifest.json`의 해당 항목 `status`를 `ok`로

---

## cover_00 · 목차 · 가짜 사이트를 잡아라

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_00 · L (16:9) |
| 장소 | 연구실 한가운데 대회장. 큰 모니터에 똑같이 생긴 두 로그인 화면(하나는 빨간 경고 표시) |
| 주제 은유 | 진짜와 가짜 사이트를 나란히 두고 돋보기로 비교 |
| 등장 | 박사, 조수, 초파리 연구원, 주판봇 |
| 대체 글 (alt) | 네 캐릭터가 똑같이 생긴 두 로그인 화면 가운데 낚싯바늘이 걸린 가짜 화면을 살피는 낮의 연구실 대회장 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·3D 금지)
- 첨부한 참고 이미지의 캐릭터를 같은 외형으로, 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 왼쪽 아래 구석은 밝고 단순하게 비워 둘 것 (제목 자리)
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline, 2-3 tone shading, small highlights; no smooth gradients, no painterly, vector or 3D look. Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style. Setting: a bright daytime lab with white walls, big windows and natural light, small lavender, mint and pink props.
Scene: the lab turned into a small contest hall. A big wall monitor shows two almost identical blank login windows side by side, the right one has a small red warning mark and a fishing hook icon hanging over it. A banner-free judging desk in the back. The scientist stands center pointing at the monitors, the pink-haired researcher holds a clipboard, the fruit fly inspects the right window with a magnifying glass, the robot raises its abacus excitedly.
Characters (keep exact looks): (1) chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; (2) girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; (3) small anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; (4) boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus;
Height ratio: scientist 1.00, pink-haired researcher 0.90, black-haired maid 0.88, beige-haired maid 0.84, robot 0.72, fruit fly 0.41.
Keep the lower-left 35% bright and simple for a title overlay. No text, no letters, no numbers, no logos, no real brands or real bank screens, no weapons. 16:9.
```

---

## cover_01 · 제1장 · 피싱 사이트와 대회 개막

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_01 · L (16:9) |
| 장소 | 대회 개막 무대, 봉인 테이프를 붙인 시험지 상자 |
| 주제 은유 | 시험지 봉인 |
| 등장 | 박사, 조수, 초파리 연구원, 주판봇 |
| 대체 글 (alt) | 시험지 상자에 봉인 테이프를 붙이는 초파리와 대회를 여는 박사, 각오를 다지는 조수, 빈 점수판을 닦는 주판봇 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·3D 금지)
- 첨부한 참고 이미지의 캐릭터를 같은 외형으로, 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 왼쪽 아래 구석은 밝고 단순하게 비워 둘 것 (제목 자리)
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline, 2-3 tone shading, small highlights; no smooth gradients, no painterly, vector or 3D look. Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style. Setting: a bright daytime lab with white walls, big windows and natural light, small lavender, mint and pink props.
Scene: contest opening. On a lab table, a stack of paper test sheets inside a clear box sealed with a bright yellow seal tape. The fruit fly places the seal, the scientist raises one hand to open the contest, the pink-haired researcher stretches with a determined fist, the robot polishes an empty score board with no numbers.
Characters (keep exact looks): (1) chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; (2) girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; (3) small anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; (4) boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus;
Height ratio: scientist 1.00, pink-haired researcher 0.90, black-haired maid 0.88, beige-haired maid 0.84, robot 0.72, fruit fly 0.41.
Keep the lower-left 35% bright and simple for a title overlay. No text, no letters, no numbers, no logos, no real brands or real bank screens, no weapons. 16:9.
```

---

## cover_02 · 제2장 · 아홉 가지 단서

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_02 · L (16:9) |
| 장소 | 벽에 붙인 단서 카드 아홉 장(그림 기호만), 탐정 놀이 |
| 주제 은유 | 단서 카드 판 |
| 등장 | 박사, 조수, 초파리 연구원, 주판봇 |
| 대체 글 (alt) | 단서 카드 아홉 장을 붙인 코르크 판 앞에서 네 캐릭터가 단서를 읽는 장면 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·3D 금지)
- 첨부한 참고 이미지의 캐릭터를 같은 외형으로, 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 왼쪽 아래 구석은 밝고 단순하게 비워 둘 것 (제목 자리)
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline, 2-3 tone shading, small highlights; no smooth gradients, no painterly, vector or 3D look. Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style. Setting: a bright daytime lab with white walls, big windows and natural light, small lavender, mint and pink props.
Scene: a cork board with nine clue cards pinned in a 3 by 3 grid, each card shows only a simple pixel icon (padlock, long address bar, envelope with arrow, popup window, picture frame, chain link, calendar, crowd, number plate), red strings connect some cards. The scientist explains with a pointer, the pink-haired researcher takes notes, the fruit fly squints at one card suspiciously, the robot counts cards on its abacus.
Characters (keep exact looks): (1) chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; (2) girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; (3) small anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; (4) boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus;
Height ratio: scientist 1.00, pink-haired researcher 0.90, black-haired maid 0.88, beige-haired maid 0.84, robot 0.72, fruit fly 0.41.
Keep the lower-left 35% bright and simple for a title overlay. No text, no letters, no numbers, no logos, no real brands or real bank screens, no weapons. 16:9.
```

---

## cover_03 · 제3장 · 데이터 건강검진

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_03 · L (16:9) |
| 장소 | 데이터 표를 진찰하는 검진실, 똑같이 생긴 종이가 겹겹이 쌓임 |
| 주제 은유 | 청진기로 데이터 진찰 |
| 등장 | 박사, 조수, 초파리 연구원, 주판봇 |
| 대체 글 (alt) | 똑같은 종이 더미를 청진기로 진찰하는 초파리와 이상한 종이를 쓸어 버리려다 멈춘 주판봇 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·3D 금지)
- 첨부한 참고 이미지의 캐릭터를 같은 외형으로, 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 왼쪽 아래 구석은 밝고 단순하게 비워 둘 것 (제목 자리)
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline, 2-3 tone shading, small highlights; no smooth gradients, no painterly, vector or 3D look. Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style. Setting: a bright daytime lab with white walls, big windows and natural light, small lavender, mint and pink props.
Scene: a data checkup room. A long table of identical paper sheets stacked in many duplicate piles. The fruit fly in a small doctor head mirror listens to a stack with a stethoscope, the scientist holds an x-ray style board showing only colored blocks, the pink-haired researcher writes on a clipboard, the robot holds a broom eager to sweep away a few odd sheets but is stopped by a raised hand.
Characters (keep exact looks): (1) chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; (2) girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; (3) small anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; (4) boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus;
Height ratio: scientist 1.00, pink-haired researcher 0.90, black-haired maid 0.88, beige-haired maid 0.84, robot 0.72, fruit fly 0.41.
Keep the lower-left 35% bright and simple for a title overlay. No text, no letters, no numbers, no logos, no real brands or real bank screens, no weapons. 16:9.
```

---

## cover_04 · 제4장 · 출전 모델과 예선

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_04 · L (16:9) |
| 장소 | 출전대 세 개, 각자 모델 소품(저울·나무 화분·작은 나무 여러 그루) |
| 주제 은유 | 세 출전자의 모델 소개 |
| 등장 | 박사, 조수, 초파리 연구원, 주판봇, 인턴 시아, 인턴 모아 |
| 대체 글 (alt) | 저울·갈림길 나무·작은 나무 줄을 든 세 출전자와 깨진 봉인을 가리키는 초파리 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·3D 금지)
- 첨부한 참고 이미지의 캐릭터를 같은 외형으로, 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 왼쪽 아래 구석은 밝고 단순하게 비워 둘 것 (제목 자리)
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline, 2-3 tone shading, small highlights; no smooth gradients, no painterly, vector or 3D look. Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style. Setting: a bright daytime lab with white walls, big windows and natural light, small lavender, mint and pink props.
Scene: three contestant booths. The black-haired maid intern stands at booth one with a balance scale with many small weights, the beige-haired maid intern at booth two with a potted tree whose branches split in yes/no forks, the pink-haired researcher at booth three with a row of small saplings growing step by step. The fruit fly holds a broken seal tape and points at a pile of copied sheets, the scientist judges with arms folded, the robot looks embarrassed scratching its head.
Characters (keep exact looks): (1) chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; (2) girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; (3) small anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; (4) boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; (5) calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron; (6) gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt;
Height ratio: scientist 1.00, pink-haired researcher 0.90, black-haired maid 0.88, beige-haired maid 0.84, robot 0.72, fruit fly 0.41.
Keep the lower-left 35% bright and simple for a title overlay. No text, no letters, no numbers, no logos, no real brands or real bank screens, no weapons. 16:9.
```

---

## cover_05 · 제5장 · 본선 · 심사 · 시상

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_05 · L (16:9) |
| 장소 | 시상대와 심사석, 방청석의 실루엣 셋 |
| 주제 은유 | 시상식 |
| 등장 | 박사, 조수, 초파리 연구원, 주판봇, 인턴 시아, 인턴 모아, 미공개 X1~X3 실루엣 |
| 대체 글 (alt) | 시상대 위 세 출전자와 심사석의 박사·주판봇·초파리, 방청석에서 응원하는 실루엣 셋 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·3D 금지)
- 첨부한 참고 이미지의 캐릭터를 같은 외형으로, 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 왼쪽 아래 구석은 밝고 단순하게 비워 둘 것 (제목 자리)
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline, 2-3 tone shading, small highlights; no smooth gradients, no painterly, vector or 3D look. Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style. Setting: a bright daytime lab with white walls, big windows and natural light, small lavender, mint and pink props.
Scene: award ceremony. A three-step podium: the pink-haired researcher on the top step holding a small trophy, the beige-haired intern on the second step holding two ribbons, the black-haired intern on the third step holding a ribbon and yawning. Behind a judging desk: the scientist with purple sparks in his hand, the robot holding a blank score board, the fruit fly with a clipboard. In the audience seats behind them, three cute solid dark navy-black silhouettes with thin purple rim light, two round white dot eyes and pink blush pixels each, one with a pink ribbon, one with teal glasses glint, one with a small yellow bell, not scary, cheering.
Characters (keep exact looks): (1) chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; (2) girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; (3) small anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; (4) boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus; (5) calm girl maid intern, long straight jet-black hair with side-swept bangs, no headdress, gray eyes, small silver drop earrings, charcoal-black long-sleeved maid dress, large gray bow, long white frilled apron; (6) gentle girl maid intern, long ash-beige wavy hair, white frilled maid headband with a ribbon over the left ear, amber-brown eyes, red and navy plaid bow tie, camel knit cardigan, white frilled apron, black skirt;
Height ratio: scientist 1.00, pink-haired researcher 0.90, black-haired maid 0.88, beige-haired maid 0.84, robot 0.72, fruit fly 0.41.
Keep the lower-left 35% bright and simple for a title overlay. No text, no letters, no numbers, no logos, no real brands or real bank screens, no weapons. 16:9.
```

---

## cover_06 · 제6장 · 실전 연습장

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_06 · L (16:9) |
| 장소 | 사이트 검사 창구와 컨베이어 검사 라인 |
| 주제 은유 | 검사 라인 |
| 등장 | 박사, 조수, 초파리 연구원, 주판봇 |
| 대체 글 (alt) | 색 상자가 지나가는 검사 라인과 창구에서 상자를 받는 주판봇, 램프를 보는 초파리 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·3D 금지)
- 첨부한 참고 이미지의 캐릭터를 같은 외형으로, 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·물음표·로고를 넣지 말 것
- 왼쪽 아래 구석은 밝고 단순하게 비워 둘 것 (제목 자리)
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline, 2-3 tone shading, small highlights; no smooth gradients, no painterly, vector or 3D look. Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style. Setting: a bright daytime lab with white walls, big windows and natural light, small lavender, mint and pink props.
Scene: an inspection line. A small conveyor belt carries colored boxes (red, yellow, green) through a gate with three round lamps on top. The robot sits at a service window receiving a box, the fruit fly watches a box with a red lamp, the pink-haired researcher types on a laptop, the scientist gives a thumbs up.
Characters (keep exact looks): (1) chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie; (2) girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans; (3) small anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings; (4) boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, holding a wooden abacus;
Height ratio: scientist 1.00, pink-haired researcher 0.90, black-haired maid 0.88, beige-haired maid 0.84, robot 0.72, fruit fly 0.41.
Keep the lower-left 35% bright and simple for a title overlay. No text, no letters, no numbers, no logos, no real brands or real bank screens, no weapons. 16:9.
```
