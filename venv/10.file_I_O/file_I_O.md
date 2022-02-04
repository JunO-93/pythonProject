# 파일 입출력
```buildoutcfg
* 파일로부터 데이터를 읽어와서 프로그램에 사용하기 위해
* 프로그램에서 만든 데이터를 파일형태로 저장하기 위해

- w : 쓰기모드(write)
- a : 추가모드(append)
- r : 읽기모드(read)

파일열기 -> 파일작업 -> 파일닫기
```

### 파일 쓰기 (덮어쓰기)
```buildoutcfg
파일객체 = open("파일이름","파일모드")
파일객체.write(데이터)
파일객체.close()

file=open("data.txt","w")
file.write("1.스타트코딩과 함께 파이썬 공부")
file.close()
```

### 파일 추가 (이어쓰기)
```buildoutcfg
파일객체 = open("파일이름","파일모드")
파일객체.write(데이터)
파일객체.close()

file=open("data.txt","a")
file.write("2.비전공자도 정말 쉽게 배울 수 있습니다.")
file.close()
```

### 파일 읽기 
```buildoutcfg
파일객체 = open("파일이름","파일모드")
파일객체.read(데이터)
파일객체.close()

file=open("data.txt","r")
file.write()  --> 데이터 전체를 가져오게 됨
file.close()
```

### pickle 모듈
```buildoutcfg
* 파일에 파이선 객체를 저장하기

import pickle
data={
    "목표1":"매일 팔굽혀 펴기 100회",
    "목표2":"매일 코딩 공부 1시간"
}

file=open("data.pickle","wb")  # wb --> binary 모드
pickle.dump(data,file)
file.close()

* 파일로부터 파이썬 객체 읽기

file=open("data.pickle","rb")
data = pickle.load(file)
print(data_
file.close()
```

### with 구문
```buildoutcfg
# 사용하는 이유 : file.close()를 항상 자동으로 호출하기 위해

* with 구문 사용 x

file=oepn("data.txt","r")
data=file.read()
file.close()

* with 구문 사용 o

with open("data.txt","r") as file:
    data=file.read()
```
### csv 파일이란?
```buildoutcfg
* csv(comma-separated values)
    데이터가 콤마로 구분된 텍스트 파일 형식
```