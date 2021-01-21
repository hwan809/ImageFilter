# coloring_image

download: https://drive.google.com/file/d/1gW2JnG_vp1CHg7TIbu2jC8aEhFWfcqEh/view?usp=sharing

RGB값 파일 작성)
0 ~ 255 숫자 3개를 한 줄에, 공백을 사용해 작성
ex) 0 255 0
평가함수 차이)
가우시안 : | 픽셀 RGB 값 - 캔버스 RGB 값 (각각 + 으로 연결) |
대비 : | (픽셀 RGB 값 - 캔버스 RGB 값( '' ) ^ 2) |
속도 : 가우시안 > 대비
정확성 : 대비 > 가우시안
사용 모듈: numpy, pil, tqdm(trange)
