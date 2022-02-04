# 원화를 입력, 환율 입력 -> 달러값출력

won = input("원화금액을 입력하세요>>>")
dollar= input("환율을 입력하세요>>>")

try: # 예외가 발생 할 수 있는 코드
    print(int(won) / int(dollar))
except ValueError as e : # 예외가 발생했을 때 실행되는 코드
    print("문자열 예외가 발생했습니다.", e)
except ZeroDivisionError as e:
    print("나누기 0은 불가능 합니다.", e)
else:
    print("예외가 발생하지 않고 실행되었습니다.")
finally: #파일 닫기 같은 리소스를 반환 해줘야 할 때 사용
    print("항상 실행되는 코드, 예외가 발생하던지 안하던지 항상 실행되는 코드")