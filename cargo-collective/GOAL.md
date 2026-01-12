# 프로젝트 목표: CargoCollective 포트폴리오 GitHub Pages 이전

## 프로젝트 개요

이 프로젝트의 목표는 CargoCollective에 게시된 모든 포트폴리오 자료를 GitHub Pages로 완벽하게 이전하는 것입니다.

**핵심 목표**: CargoCollective에 올려놓은 모든 자료를 빠짐없이 가져와서 GitHub Pages로 포트폴리오를 옮기는 것입니다.

## 이전 대상 자료

각 페이지에서 다음 자료들을 누락 없이 가져와야 합니다:

- **텍스트**: 모든 페이지의 텍스트 콘텐츠
- **이미지**: 모든 이미지 파일
- **GIF**: 모든 GIF 애니메이션 파일
- **임베디드 동영상 링크**: Vimeo, YouTube 등 임베디드 동영상 링크

## 주요 작업 단계

- [ ] CargoCollective의 모든 페이지 리스트업
- [ ] 페이지별 텍스트 추출 및 마크다운 변환
- [ ] 이미지 및 GIF 다운로드 및 로컬 저장
- [ ] 임베디드 동영상(Vimeo, YouTube 등) 링크 정리
- [ ] Jekyll 또는 Vite를 이용한 사이트 구성 및 배포

## 프로젝트 목록 (검증 필요)

### Main Grid
ColorPiece, DoodlAR, Toonify, Project Awkward, Blow A Kiss, Object Segmentation, DICE, One Zero, Motion Recognition, Snapchat Lenses, The Tree of Babel, Posture & Eye Care, Face Recognition Games, Go Card, Smile Face-in, Swipe!, Suprememe, Sigh, Tweequency, Glitch, Dead Wood, Humanphobia, Fandamonium, Emotion Detection, Smile Filter

### Archive (Blog)
ITP Thesis, Generative Music, Game Design and The Psychology of Choice, Machine Learning for the Web, Art Toy Design, Design for Discomfort, Soft Sensing, Haptics, Tweet Reader, Detourning the Web, Voice, The Rest of You, Metabolism, Habitual Energy, Physical Computing

## 검증 체크리스트

### 파일 검증
- [ ] 각 프로젝트에 해당하는 `.md` 파일이 존재하는지 확인
- [ ] 모든 페이지의 텍스트, 이미지, GIF, 동영상 링크가 포함되어 있는지 확인

### 미디어 검증
- [ ] 모든 이미지/GIF가 로컬에 저장되어 있는지 확인
- [ ] 이미지/GIF 링크가 올바른지 확인
- [ ] 임베디드 동영상이 정상적으로 재생되는지 확인

### 사이트 구성 검증
- [ ] `_data/projects.yml`이 홈페이지 그리드에 맞게 업데이트되었는지 확인
- [ ] `_config.yml`이 필요에 따라 업데이트되었는지 확인
- [ ] 레이아웃이 원본 포트폴리오의 미적 특성을 유지하는지 확인

## 최종 검증

- [ ] GitHub Pages 사이트의 각 페이지를 원본 CargoCollective 사이트와 비교 검증
- [ ] 모든 이미지와 GIF가 정상적으로 로드되는지 확인
- [ ] 모든 임베디드 동영상이 정상적으로 재생되는지 확인