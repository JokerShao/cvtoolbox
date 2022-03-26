import numpy as np


class Test:
    def __init__(self) -> object:
        self.a_ = []
        self.b_ = 0
        self.c_ = np.zeros((1,1), dtype=np.float64)

    def add_a(self) -> None:
        self.a_.append(1)

    def add_b(self) -> None:
        self.b_ += 1

    def add_c(self) -> None:
        self.c_ += 1

    def get_a(self) -> list:
        return self.a_

    def get_b(self) -> int:
        return self.b_

    def get_c(self) -> np.ndarray:
        return self.c_

    def get_a_copy(self) -> list:
        return self.a_.copy()

    def get_c_copy(self) -> np.array:
        return self.c_.copy()


if __name__ == '__main__':

    test = Test()
    a = test.get_a()
    a_copy = test.get_a_copy()
    b = test.get_b()
    c = test.get_c()
    c_copy = test.get_c_copy()

    print('id(test.a_):'.rjust(13), id(test.a_))
    print('id(a):'.rjust(13), id(a))
    print('id(a_copy):'.rjust(13), id(a_copy))

    print('id(test.b_):'.rjust(13), id(test.b_))
    print('id(b):'.rjust(13), id(b))

    print('id(test.c_):'.rjust(13), id(test.c_))
    print('id(c):'.rjust(13), id(c))
    print('id(c_copy):'.rjust(13), id(c_copy))

    test.add_a()
    test.add_b()
    test.add_c()

    print('test.a_:'.rjust(13), test.a_)
    print('a:'.rjust(13), a)
    print('a_copy:'.rjust(13), a_copy)

    print('test.b_:'.rjust(13), test.b_)
    print('b:'.rjust(13), b)

    print('id(test.b_):'.rjust(13), id(test.b_))
    print('id(b):'.rjust(13), id(b))

    print('test.c_:'.rjust(13), test.c_)
    print('c:'.rjust(13), c)
    print('c_copy:'.rjust(13), c_copy)

