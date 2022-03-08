# find_hidden_file
파일에 다른 파일이 숨겨져 있는지 확인하고 파일 시그니처를 이용해서 이를 분리해내는 코드이다.
<br>
![고양이](https://user-images.githubusercontent.com/85146195/157223767-74421fdc-fd91-464b-9c15-6c8bf2391956.jpg)<br>
위 파일은 고양이 사진이지만, 이 파일 안에는 또 다른 파일이 숨겨져 있다.<br>
만약 다른 파일이 숨겨져있다는 정보를 얻지 못한 상태에서 위 사진을 봤다면, 그냥 고양이 사진일 것이다. 

사진이나 압축파일 등 특정 파일은 파일시그니처라는 것을 가지고 있고 이를 이용해 파일의 시작과 끝을 나타낸다. 이를 이용하면 특정 파일 뒤에 내가 숨기고 싶은 파일을 쉽게 숨길 수 있다.<br>
간단하게 파일 숨기는 방법 : https://she11.tistory.com/85 <br>

그래서 find_fidden_file.py의 코드는 signature.py의 딕셔너리화 시킨 파일 시그니처를 기반으로 파일안의 숨겨진 파일이 있는지 찾아 파일을 분리해준다.<br>

사용방법 : python hiddenfile_find.py [filename]

<img width="471" alt="image" src="https://user-images.githubusercontent.com/85146195/157225177-bfa0a412-92fe-4354-99db-e99fcc979547.png">

2개의 파일이 시그니처를 이용해서 찾아낼 수 있었고, 파일을 각각 분리한다. 

<img width="594" alt="image" src="https://user-images.githubusercontent.com/85146195/157225980-0f15e916-9b25-489b-8b00-db85665396f6.png">
file_out_1.jpeg 파일은 아까 봤던 고양이 사진의 순수한 원본이고, file_out_2.zip 파일은 '중요한 파일.txt'가 들어있는 zip 파일이다.

이로써 그저 고양이 사진으로만 보였던 파일에서 중요한 파일이 담긴 압축파일이 숨어있음을 확인할 수 있다.
<br><br>
problem1.png 파일안에는 여러 파일들이 숨어 있다. 이 파일을 통해 테스트해보면 여러 파일이 나오는 것을 직접 확인할 수 있을 것이다.
