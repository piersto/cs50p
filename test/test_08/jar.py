import emoji


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        if not isinstance(capacity, int):
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return (emoji.emojize(':cookie:', language='alias')) * self._size

    def deposit(self, n):
        self._size = self.size + n
        if self._size > self._capacity:
            raise ValueError
        else:
            return self._size

    def withdraw(self, n):
        if self._size < n:
            raise ValueError
        else:
            self._size = self.size - n
        return self._size

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @size.setter
    def size(self, size):
        self._size = size


jar = Jar(capacity=12)
jar.deposit(11)
jar.withdraw(1)

print(jar)
