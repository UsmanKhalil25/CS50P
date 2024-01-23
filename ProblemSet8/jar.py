class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size
    
    def deposit(self, n):
        if self.size + n > self.capacity:
            raise(ValueError("Cannot add more cookies"))    
        self.size = self.size + n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self,capacity):
        if capacity < 0:
            raise(ValueError("Capacity cannot be negative"))
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,size):
        self._size = size


def main():
    jar = Jar(5)
    print(jar)
    jar.deposit(4)
    print(jar)
    jar.withdraw(2)
    print(jar)
    jar.withdraw(2)
    print(jar)


if __name__ == "__main__":
    main()
