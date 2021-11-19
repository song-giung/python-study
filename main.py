print('love python')


class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1
        # self.num_instances += 1 # 클래스 멤버가 아닌 인스턴스 멤버를 다시 선언하는 것(주의)
