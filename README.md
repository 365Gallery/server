## 365Gallery
[📝 자세한 개발일지](https://github.com/365Gallery/server/wiki)

## 언제 어디서나 즐길 수 있는 비대면 웹 갤러리 서비스

    안녕하세요, 저희는 '벼리 수놓아진 방에'팀 입니다.
    코로나 시대에 비대면 전시가 이루어지면서, 사용자와 소통하는 새로운 형식의 콘텐츠를 생성하고 있습니다.
    저희는 머신러닝을 결합한 새로운 형태의 실시간 체험형 전시를 기획합니다.

## 동작과정

![image](https://user-images.githubusercontent.com/54340317/120063035-2ac84380-c0a0-11eb-92d0-03ad716561db.png)

- 사용자는 이미지를 업로드 하여 다양한 스타일의 명화로 변환할 수 있다.
- 웹 캠을 활용하여 자신의 모습이 실시간으로 변환되는 모습을 확인할 수 있다.
- Google cloud platform : 구글에서 제공하는 클라우드를 활용하여 서버 구축
- Django, Django Rest Framework, MySQL : REST API 구현
- Tensorflow : ML model을 생성하고 명화풍의 이미지 변환에 사용
- celery & redis : 이미지 변환 비동기 & 분산 처리
- html & css & javascript : UI/UX 개발

## 구현 기능 및 플로우차트

![image](https://user-images.githubusercontent.com/54340317/120063044-3c115000-c0a0-11eb-9f3b-25e205f77196.png)
![image](https://user-images.githubusercontent.com/54340317/120063049-3ddb1380-c0a0-11eb-97fc-bd6c81259e9c.png)
![image](https://user-images.githubusercontent.com/54340317/120063051-403d6d80-c0a0-11eb-82e3-6e138faf0c96.png)

- 사용자는 이미지를 업로드하고 원하는 이미지 화풍을 선택할 수 있다.
- 이미지 화풍은 서양 미술사 흐름에 맞는 8개 학파(인상주의, 야수주의, 입체주의, 추상주의, 표현주의, 미래파, 현실주의, 팝아트)에 대한 17가지 화풍에 대한 서비스를 제공한다.
- 변환된 이미지를 갤러리에 추가하고, 공유 링크를 생성할 수 있다.
- 공유 링크로 접속하면 모든 사용자 및 비회원은 갤러리 속 사진들을 확인할 수 있다.

![image](https://user-images.githubusercontent.com/54340317/120063121-9a3e3300-c0a0-11eb-9840-2c0858d66034.png)

## 기대 효과

- 멀어진 예술 작품의 접근성을 높이고 일상을 유쾌한 방식으로 기록할 수 있도록 한다
- 새로운 비대면 체험형 전시 방안을 제안한다
