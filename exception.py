# 사용자 정의 에러의 가장 최상위 클래스
class BaseValidationError(ValueError):
    pass


class NameTooShortError(BaseValidationError):
    pass


class NameTooLongError(BaseValidationError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)


try:
    validate('giung')
except BaseValidationError as err:
    pass
"""
# 일반적인 ValueError 를 사용하였을 경우 예외의 정확한 이유를 파악하기 힘들다.

Traceback (most recent call last):
  File "/Users/song-giung/projects/python-study/exception.py", line 6, in <module>
    validate('giung')
  File "/Users/song-giung/projects/python-study/exception.py", line 3, in validate
    raise ValueError
ValueError
"""
"""
사용자 정의 에러를 통해 세분화되고 의도가 분명하게 들어나는 예외처리가 가능하지만,
관련이 없는 에러는 잡히지 않기 때문에 유의하여야 한다.
"""
