# KimJuYoung
김주영 프로젝트 레포지토리

21. 12. 03

1. 8:53분에 git push 했으나 지금 readme 파일이 없어짐
2. 아무래도 git push 를 하는데 문제가 생긴것 같음

어제 내용 다시 적을예정
21. 12. 02

1. 일단 집에서 하던 프로젝트를 개인 레포지토리에 올려보려 시도.
2. cd 디렉토리 해서 git bash 경로를 변경해줌
3. remote 설정을 해서 원격 저장소 개인 레포지토리로 이동
4. git remote add origin 주소
4. branch 를 master에서 main으로 이동하는게 편할 것 같아서 main 으로 브랜치 이동함
5. git init
6. git add .
7. git commit -m "커밋메시지"
8. git push origin main 
9. 끗

그리고 팀 프로젝트에 있는 내 레포지토리로도 저장
1. remote 가 지금 내 개인원격레포지토리 이므로 
2. remote를 끊음 git remove origin
3. remote를 팀 프로젝트에 있는 내 레포지토리로 이동
4. git remote add origin 주소
5. 나머지는 동일

+ git push origin main 이 작동이 안되고 git push origin +main 을 사용해 강제적으로 push를 해줘야 했는데
  지금 이게 readme 파일이 문제인것 같음.
  그래서 지금 쓰고있는 readme파일을 저장한 후 clone으로 다른 로컬디렉토리에 프로젝트를 다운받아보고 그걸 test 레포지토리에 넣어볼 예쩡
  
