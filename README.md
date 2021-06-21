## 365Gallery
[📝 자세한 개발일지](https://github.com/365Gallery/server/wiki)

## 언제 어디서나 즐길 수 있는 비대면 웹 갤러리 서비스

    안녕하세요, 저희는 '벼리 수놓아진 방에'팀 입니다.
    코로나 시대에 비대면 전시가 이루어지면서, 사용자와 소통하는 새로운 형식의 콘텐츠를 생성하고 있습니다.
    저희는 머신러닝을 결합한 새로운 형태의 실시간 체험형 전시를 기획합니다.

## 개발 내용

![image](https://user-images.githubusercontent.com/54340317/120063035-2ac84380-c0a0-11eb-92d0-03ad716561db.png)
<img src="https://user-images.githubusercontent.com/54340317/121770603-2bcf9980-cba5-11eb-8dbe-03c9e0f7ceb0.png" width=500>

- 사용자는 이미지를 업로드 하여 다양한 스타일의 명화로 변환할 수 있다.
- 웹 캠을 활용하여 자신의 모습이 실시간으로 변환되는 모습을 확인할 수 있다.
- Google cloud platform : 구글에서 제공하는 클라우드를 활용하여 서버 구축
- Django, Django Rest Framework, MySQL : REST API 구현
- Tensorflow : ML model을 생성하고 명화풍의 이미지 변환에 사용
- celery & redis : 이미지 변환 비동기 & 분산 처리
- html & css & javascript : UI/UX 개발

## 구현 기능 및 플로우차트

![image](https://user-images.githubusercontent.com/54340317/121307645-2a9b3400-c93b-11eb-9123-d5ec567d4dcb.png)
![image](https://user-images.githubusercontent.com/54340317/121308511-1ad01f80-c93c-11eb-85b2-cd25c55ee08b.png)
![image](https://user-images.githubusercontent.com/54340317/121308527-1f94d380-c93c-11eb-8391-9367dfab1f00.png)


- 사용자는 이미지를 업로드하고 원하는 이미지 화풍을 선택할 수 있다.
- 이미지 화풍은 서양 미술사 흐름에 맞는 8개 학파(인상주의, 야수주의, 입체주의, 추상주의, 표현주의, 미래파, 현실주의, 팝아트)에 대한 20가지 화풍에 대한 서비스를 제공한다.
- 변환된 이미지를 갤러리에 추가할 수 있다.
- 모든 사용자는 갤러리에 저장된 사진에 해당되는 태그를 확인하고 댓글을 남길 수 있다.

## ML 모델 학습 결과

![image](https://user-images.githubusercontent.com/54340317/121308585-2e7b8600-c93c-11eb-8123-92fcac995cb5.png)
![image](https://user-images.githubusercontent.com/54340317/120063121-9a3e3300-c0a0-11eb-9840-2c0858d66034.png)

- 사전 훈련된 Imagenet VGG19 model 사용하여 전이 학습 진행
- 평균 학습 시간 5~6시간 소요 (Epoch 4, Batch size 6, Image size 720 * 900)

## 기대 효과

- 멀어진 예술 작품의 접근성을 높이고 일상을 유쾌한 방식으로 기록할 수 있도록 한다
- 새로운 비대면 체험형 전시 방안을 제안한다

## 시연 동영상

- [최종 시연 동영상](http://cscp2.sogang.ac.kr/CSE4187/CSE4187/UserData/365_final_web.mp4)

## 2021 KCC 한국정보과학회 논문 채택

- 제목 : CNN 모델을 이용한 실시간 미술전시 웹 플랫폼(A Real Time Virtual Web Platform for Art Exhibition with CNN Model)
- 저자 : 방 윤, 채 벼리, 박 수진, 구 명완
- 분야 : 인공지능
- 요약 : 코로나 시대에 전시회 관람이 제약됨으로 인해 많은 미술관과 박물관에서 비대면 전시를 도입하고 있다. 그러나 이는 VR형식에 그쳐, 새로운 소통형 콘텐츠 개발의 필요성이 증대되는 실정이다. 본 논문은 코로나 시대에서 관객이 직접 참여할 수 있는 새로운 체험형 미술 전시 방안을 소개하고 그 작동 원리를 설명한다. 관람객은 이미지가 미술 시대흐름에 따른 화풍으로 변환되는 모습을 포착하며 각 시대별 화풍 스타일 및 미술 역사의 흐름에 대한 이해도를 높일 수 있다. 또한 변환된 사진을 다수에게 공유하는 플 랫폼을 이용하여 일상을 유쾌한 방식으로 기록하며, 예술작품의 접근성을 높일 수 있다.
