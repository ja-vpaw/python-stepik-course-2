class ExtendedStack(list):
    def sum(self):
        # операция сложения
        if len(self) >= 2:
            self.append(self.pop() + self.pop())

    def sub(self):
        # операция вычитания
        if len(self) >= 2:
            self.append(self.pop() - self.pop())

    def mul(self):
        # операция умножения
        if len(self) >= 2:
            self.append(self.pop() * self.pop())

    def div(self):
        # операция целочисленного деления
        if len(self) >= 2:
            self.append(self.pop() // self.pop())


ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
print(ex_stack)

ex_stack.div()
print(ex_stack)
assert ex_stack.pop() == 2

ex_stack.sub()
print(ex_stack)
assert ex_stack.pop() == 6

ex_stack.sum()
print(ex_stack)
assert ex_stack.pop() == 7

ex_stack.mul()
print(ex_stack)
assert ex_stack.pop() == 2

print(ex_stack)
assert len(ex_stack) == 0

