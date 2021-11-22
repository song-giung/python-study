"""
컴파일러가 소스 코드를 바이트 코드로 변환하고 이를 로컬에 캐쉬로 저장한다(.pyc, .pyo)
그리고 스택 기반 가상 머신에서 바이트 코드를 실행한다.
중간 과정을 살펴 보자
바이트 코드를 더 쉽게 검사하기 위한 도구 dis
"""
import dis


def greet(name):
    return f'Hello, {name}'

dis.dis(greet)
"""
 10           0 LOAD_CONST               1 ('Hello, ')
              2 LOAD_FAST                0 (name)
              4 FORMAT_VALUE             0
              6 BUILD_STRING             2
              8 RETURN_VALUE
"""