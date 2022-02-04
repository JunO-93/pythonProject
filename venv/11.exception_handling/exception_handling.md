# 예외처리
```buildoutcfg
* 프로그램 실행 중에 발생하는 에러를 미연에 방지
```

### try_except
```buildoutcfg
try:
    예외가 발생할 수 있는 코드
except:
    예외 발생 시 실행할 코드
else:
    예외 발생하지 않은 경우 실행할 코드 #잘 안쓰임
finally:
    항상 실행할 코드 # 예외가 발생해도 안해도 항상 실행되는 코드
```

### raise 구문사용법
```buildoutcfg
*에러를 강제로 만드는 방법

raise 예외 ("에러메세지")

raise Exception

raise Exception("에러메세지")
```

### 예외 계층 구조
```buildoutcfg
except ZeroDivisionError:

except ArithmeticError: # FloatingPointError, OverflowError, ZeroDivisionError 다 포함

except Exception:  #모든 내장 예외들을 받을 수 있다
```

### 에러만들기
```buildoutcfg
* Exception 클래스를 상속받으면 된다.

class 예외(Exception):
    def __init__(self)
        super().__init__("에러 메세지")
```