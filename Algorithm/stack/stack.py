class Stack:
    from collections.abc import Iterable

    def __init__(self, N, iterable: Iterable = None, defalt=None):
        self.N = N
        if iterable != None:
            if len(iterable) != N:
                self.N = len(iterable)
            self._stack = list(iterable)
        else:
            self._stack = [defalt] * N
        self.top = -1

    def pop(self):
        if self.top < 0:
            return None
        self.top -= 1
        return self._stack[self.top + 1]

    def push(self, value):
        if self.top + 1 >= self.N:
            return False
        self.top += 1
        self.set_stack(self.top, value)
        return True

    @property
    def length(self):
        return self.top + 1

    @property
    def stack(self):
        return self._stack

    def set_stack(self, i, v):
        self._stack[i] = v


if __name__ == "__main__":
    s = Stack(10)

    # print(s.pop()) # under flow

    for i in range(10):
        s.push(i)  # s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # s.push(10) # over flow
    print("s의 길이:", s.length)

    # 스택 출력
    print("스택 출력")
    for _ in range(10):
        print(s.pop(), end=" ")  # 9 8 7 6 5 4 3 2 1 0
    print()

    print("s의 길이:", s.length)
