class Queue:
  def __init__(self):
    self.items = []
  def enqueue(self, element):
    self.items.append(element)
  def dequeue(self):
    return self.items.pop(0)
  def isEmpty(self):
    return len(self.items) == 0
  def front(self):
    return self.items[0]
  def clear(self):
    self.items.clear()
