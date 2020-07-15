# Stack
class Stack:
  def __init__(self):
    self.items = []
  def append(self, element):
    self.items.append(element)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[len(self.items) - 1]
  def isEmpty(self):
    return len(self.items) == 0
  def size(self):
    return len(self.items)
  def clear(self):
    self.items.clear()
  def print(self):
    print('items is =>', self.items)
    return self.items

stack = Stack()
stack.append(1)
stack.append(5)
stack.append(3)
stack.append(6)
stack.pop()
stack.print()

# Decimal to Binary
def divide_by_two(num):
  d_list = Stack()
  b_str = ''
  if num == 0:
    return 0
  else:
    while num > 0:
      d_list.append(num % 2)
      num = num // 2
    while d_list.size() > 0:
      b_str += str(d_list.pop())
    print('binary is =>', int(b_str))
    return int(b_str)

divide_by_two(23)
