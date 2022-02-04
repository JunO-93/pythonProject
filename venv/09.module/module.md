# 모듈

### 모듈 사용방법
```buildoutcfg
import 모듈이름
모듈이름.변수
모듈이름.함수()

import math 
print(math.pi)
print(math.ceil(5.7))

from math import pi,ceil
print(pi)
print(ceil(5.7))
```

###  파이썬 외부 모듈 사용 방법
```buildoutcfg
pip install 모듈이름

pip install pyautogui
```
### 패키지
```buildoutcfg
* 관련 있는 모듈을 하나로 묶어놓은 것
```

#### 패키지 예시 구조
```buildoutcfg
\startcoding
    ㄴ \unit
        ㄴ __init__.py
        ㄴ character.py
        ㄴ item.py        
        ㄴ monster.py
    ㄴ main.py
```
