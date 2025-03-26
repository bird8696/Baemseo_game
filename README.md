# Baemseo_game

# 🧛 Vampire Survivors Lite

`Vampire Survivors Lite`는 파이게임(Pygame)을 기반으로 제작된 탑다운 슈팅 로그라이크 게임입니다.  
마우스로 조준하고, 키보드로 이동하며 적을 처치해 점수를 올리는 방식으로, 심플하지만 중독성 있는 구조로 설계되었습니다.
<img width="602" alt="메인페이지" src="https://github.com/user-attachments/assets/03062ebe-9ae8-424f-9308-ee1d29cf9def" />

---

## 🎮 게임 시스템

- **플레이어 선택**  
  게임 시작 전 3종류의 캐릭터 중 하나를 선택할 수 있습니다.  
  각 캐릭터는 서로 다른 총알 색상을 지니며, 향후 무기 특성도 추가될 예정입니다.
  <img width="602" alt="캐릭터 선택화면" src="https://github.com/user-attachments/assets/b2b924c6-ccd9-459b-afad-7dd4ace17d89" />


- **적 몬스터 종류**  
  - `monster1`: 일반형
   ![몬스터1](https://github.com/user-attachments/assets/db45513e-a7ee-42ce-9e13-e62f3ee9692f)

  - `monster2`: 빠른 돌진형
   ![몬스터2](https://github.com/user-attachments/assets/b51e8184-0058-40d6-ad01-9b47f88383d6)

  - `monster3`: 느리지만 원거리 총알 발사
    ![몬스터3](https://github.com/user-attachments/assets/e3a4cfa9-164f-4afd-a3cb-3c9af3814a5d)


- **공격 시스템**
  - 마우스 클릭으로 발사 (기본 직선 발사)
  - 업그레이드 시스템을 통해 3방향 스프레드 슛 또는 총알 크기 증가 가능

- **업그레이드 메뉴**
  - 일정 조건 달성 시 등장
  - 총알 사이즈 증가 / 180도 방향 공격 선택 가능

- **UI 구성**
  - 점수 표시
  - 게임 오버 시 메뉴 제공 (Retry / Main Menu)
    
<img width="593" alt="게임화면1" src="https://github.com/user-attachments/assets/b4f4be98-bdbf-4fc0-91c8-d0fa0d47afd2" />

---

## 🧠 코드 구조 설명

```plaintext
📁 project/
│
├─ main.py            # 메인 게임 코드
│
├─ image/             # 캐릭터 및 몬스터 이미지 파일
│   ├─ 주인공1.png
│   ├─ 주인공2.png
│   ├─ 주인공3.png
│   ├─ 몬스터1.png
│   ├─ 몬스터2.png
│   └─ 몬스터3.png
```

- `Player` 클래스  
  → 이동, 캐릭터 별 총알 색 설정 포함

- `Enemy`, `EnemyBullet` 클래스  
  → 적의 타입에 따라 이동 속도와 공격 방식 다름

- `Bullet` 클래스  
  → 플레이어 총알 (업그레이드에 따라 크기/방향 달라짐)

- `Button` 클래스  
  → 메인 메뉴, 게임 오버, 캐릭터 선택, 업그레이드에 사용

- `main()` 함수  
  → 전체 게임 루프 제어, 스테이지, 충돌처리, 점수 처리

---

## 🔧 업데이트 예정 기능

| 항목 | 설명 |
|------|------|
| ✅ 캐릭터별 무기 특성 | 각 캐릭터마다 공격 방식, 범위, 속도 등 차별화 |
| ✅ 체력 시스템 (HP) | 플레이어 및 적 체력 추가, 체력 UI |
| ✅ 맵 구현 | 타일 기반 스크롤 맵 또는 고정된 방 구조 |
| ✅ 아이템 드랍 | 적 처치 시 확률적 드랍 (회복, 강화 등) |
| ✅ 적 웨이브 시스템 | 점점 강해지는 웨이브/라운드 시스템 |
| ✅ 사운드 효과 | 총알 발사음, 적 처치음, 배경음악 |
| ✅ 보스 몬스터 | 특정 조건 혹은 웨이브마다 강력한 보스 등장 |

---

## 📦 설치 및 실행 방법

```bash
pip install pygame
python main.py
```

---

## 🧑‍💻 제작자

- 💻 Code by: [Kuchyo] and [ChatGPT]
- 🎨 Pixel Art: Custom / Generated / ChatGPT
- 🔧 Engine: Python 3.13.2 + Pygame

---

## 📃 라이선스

MIT License
