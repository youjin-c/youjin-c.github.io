# CargoCollective → GitHub Pages 마이그레이션 진행 현황

> 마지막 업데이트: 2026-01-10 (세션 3)

## 프로젝트 구조

```text
youjin-c.github.io/
├── cargo-collective/                        ← 스크래핑 작업 폴더
│   ├── markdown/                            ← 스크래핑 원본 (46개 .md)
│   ├── images/                              ← 스크래핑 이미지 원본 (35개 폴더)
│   ├── download_images.py                   ← Admin Console URL 기반 이미지 다운로드
│   ├── scrape_*.py                          ← 스크래핑 스크립트
│   ├── PROGRESS.md                          ← 이 파일 (작업 현황)
│   └── GOAL.md                              ← 프로젝트 목표
│
├── *.md                                     ← GitHub Pages용 (Jekyll front matter 포함)
├── images/                                  ← GitHub Pages용 이미지
└── _site/                                   ← Jekyll 빌드 결과
```

### 작업 흐름

1. **스크래핑** → `cargo-collective/`에 원본 저장
2. **정리** → Jekyll front matter 추가, 네비게이션 제거 등
3. **배포** → 최상단에 복사하여 GitHub Pages 사용

---

## 전체 프로젝트 목록 및 상태

> **범례**: .md 재작업 = 이번 세션(세션2)에서 scrape_missing.py로 마크다운 재스크래핑 / 이미지 재작업 = download_images.py로 Admin Console URL 기반 다운로드

### Main Grid 프로젝트 (24개)

| 프로젝트 | .md 파일 | .md 재작업 | 이미지 수 | 이미지 재작업 |
|----------|----------|------------|-----------|---------------|
| ColorPiece | O | O (세션1) | 9 | O (세션2) |
| DoodlAR | O | O (세션2) | 4 | O (세션1) |
| Toonify | O | O (세션2) | 4 | O (세션1) |
| Project Awkward | O | O (세션2) | 1 | O (세션1) |
| Blow A Kiss | O | O (세션2) | 4 | O (세션1) |
| Object Segmentation | O | O (세션2) | 8 | O (세션1) |
| DICE | O | O (세션2) | 11 | O (세션1) |
| One Zero | O | O (세션2) | 9 | O (세션1) |
| Motion Recognition | O | O (세션1) | 8 | O (세션1) |
| Snapchat Lenses | O | O (세션2) | 1 | O (세션1) |
| The Tree of Babel | O | O (세션1) | 7 | O (세션1) |
| Posture & Eye Care | O | O (세션1) | 10 | O (세션1) |
| Face Recognition Games | O | O (세션2) | 14 | O (세션1) |
| Go Card | O | O (세션2) | 6 | O (세션1) |
| Smile Face-in | O | O (세션1) | 8 | O (세션1) |
| Swipe! | O | O (세션1) | 5 | O (세션1) |
| Suprememe | O | O (세션1) | 16 | O (세션1) |
| *Sigh* | O | O (세션2) | 4 | O (세션2) |
| Tweequency | O | O (세션1) | 7 | O (세션1) |
| Glitch | O | O (세션1) | 8 | O (세션1) |
| Dead Wood | O | O (세션1) | 20 | O (세션1) |
| Humanphobia | O | O (세션2) | 4 | O (세션1) |
| Fandamonium | O | O (세션1) | 1 | O (세션1) |
| Emotion Detection | O | O (세션1) | 12 | O (세션1) |
| Smile Filter | O | O (세션1) | 11 | O (세션1) |

### Archive (Blog) 프로젝트 (15개)

| 프로젝트 | .md 파일 | .md 재작업 | 이미지 수 | 이미지 재작업 |
|----------|----------|------------|-----------|---------------|
| ITP Thesis | O | O (세션1) | 41 | O (세션1) |
| Generative Music | O | O (세션2) | 5 | O (세션2) |
| Game Design & Psychology | O | O (세션2) | 6 | O (세션2) |
| Machine Learning for Web | O | O (세션1) | 3 | O (세션2) |
| Art Toy Design | O | O (세션2) | 76 | O (세션2) |
| Design for Discomfort | O | O (세션2) | 18 | O (세션2) |
| Soft Sensing | O | O (세션1) | 8 | O (세션2) |
| Haptics | O | O (세션1) | 8 | O (세션2) |
| Tweet Reader | O | O (세션2) | 2 | O (세션2) |
| Detourning the Web | O | O (세션1) | 11 | O (세션2) |
| Voice | O | O (세션1) | 7 | O (세션2) |
| The Rest of You | O | O (세션1) | 8 | O (세션2) |
| Metabolism | O | O (세션1) | 4 | O (세션2) |
| Habitual Energy | O | O (세션1) | 6 | O (세션2) |
| Sigh Machine (Blog) | O | O (세션1) | 3 | O (세션2) |

---

## 스크래핑 주의사항

### 429 에러 (Too Many Requests)
- **원인**: 짧은 시간 내 다량 요청 시 IP 차단
- **해결**: 각 요청 간 `time.sleep(random.uniform(5, 10))` 필수
- **429 발생 시**: 즉시 중단 후 30분~1시간 대기

### 고화질 이미지 확보
- 일반 페이지 이미지는 리사이즈된 버전일 수 있음
- Admin 패널 > 프로젝트 > Images 섹션에서 `freight.cargo.site/t/original/...` 링크 사용

### 비공개 프로젝트
- 로그인 세션 쿠키 유지 필요
- Admin 패널의 'DIRECT LINK' 버튼 활용

---

## 검증 체크리스트

### 로컬에서 가능한 검증
- [ ] 각 .md 파일 내용이 비어있지 않은지 확인
- [ ] .md 내 이미지 경로가 실제 파일과 매칭되는지
- [ ] 임베디드 동영상(Vimeo/YouTube) 링크 존재 여부

### 원본 비교 필요 (스크래핑 필요)
- [ ] 텍스트 누락 여부
- [ ] 이미지 누락 여부
- [ ] 이미지 품질 (고화질 원본인지)

---

## 작업 이력

### 2026-01-10 (세션 3)

- **Jekyll 사이트 설정 완료**
  - `_data/projects.yml`의 URL을 `.md` → `.html`로 변경 (Jekyll 빌드 후 URL)
  - 누락된 썸네일 수정: Fandamonium (.gif→.png), Art-Toy-Design (u.png→0.jpeg)
  - 빈 썸네일 추가: Game-Design-and-Psychology, Humanphobia, Tweet-Reader
- **markdown_clean → 최상단 적용 완료** (40개 파일)
  - `cargo-collective/markdown_clean/`의 모든 파일을 최상단에 Jekyll front matter 추가하여 복사
  - 기존에 직접 작성했던 파일들(ColorPiece 등)도 스크래핑 원본으로 덮어씀
- Jekyll 로컬 서버 테스트 완료 (port 4001)

### 2026-01-10 (세션 2)

- Admin Console에서 19개 프로젝트 원본 이미지 URL 추출 완료
  - Machine-Learning-for-the-Web (2), Soft-Sensing (6), Haptics (7)
  - Detourning-the-Web (7), Voice (6), The-rest-of-You (6)
  - Metabolism (2), Habitual-Energy (2), Sigh-Machine (3), *Sigh* (4)
- *Sigh* (Main Grid)와 Sigh-Machine (Blog) 분리 완료
- download_images.py 실행: 236개 이미지 전체 다운로드
- **모든 프로젝트 마크다운 재스크래핑 완료** (17개 추가)
  - Main Grid: DoodlAR, Toonify, Project-Awkward, Blow-A-Kiss, Object-Segmentation, DICE, One-Zero, Snapchat-Lenses, Face-Recognition-Games, Go-Card, Sigh, Humanphobia
  - Archive: Generative-Music, Game-Design-and-Psychology, Art-Toy-Design, Design-for-Discomfort, Tweet-Reader
- 모든 프로젝트 이미지 스크래핑 **완료**
- **스크래핑 100% 완료**: 39개 프로젝트 마크다운 + 이미지

### 2026-01-10 (세션 1)

- 미스크래핑 4개 프로젝트 완료: Swipe!, Suprememe, Tweequency, Dead Wood
- Admin Console에서 14개 프로젝트 원본 이미지 URL 추출 (90개 URL)
- download_images.py로 고화질 이미지 다운로드 완료
- 11개 프로젝트 텍스트 재스크래핑 완료 (scrape_missing.py)
- projects_images.json에 모든 URL/이미지 경로 백업
- 폴더 구조 정리: portfolio-site → cargo-collective로 변경

### 2026-01-09

- 429 에러 발생으로 스크래핑 중단
- 현재까지 완료된 프로젝트: 약 30개 .md 파일 생성
- 이미지 미다운로드 프로젝트 다수 확인
- PROGRESS.md 파일 생성하여 현황 정리 시작
