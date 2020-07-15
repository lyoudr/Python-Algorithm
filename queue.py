# Queue 
# apply FIFO
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

# Priority Queue
class QueueElement:
  def __init__(self, element, priority):
    self.element = element
    self.priority = priority

class PriorityQueue:
  def __init__(self):
    self.items = []
  def enqueue(self, element, priority):
    queue_ele = QueueElement(element, priority)
    if self.isEmpty():
      self.items.append(queue_ele)
    else:
      added = False
      for index, item in enumerate(self.items):
        if priority <= item.priority :
          self.items.insert(index, queue_ele)
          break
      if not added:
        self.items.append(queue_ele)
  def dequeue(self):
    return self.items.pop(0)
  def isEmpty(self):
    return len(self.items) == 0
  def front(self):
    return self.items[0]
  def clear(self):
    self.items.clear()
  def print_out(self):
    print('items is =>',[(item.element, item.priority) for item in self.items])

p_queue = PriorityQueue()
p_queue.enqueue('Ann', 2)
p_queue.enqueue('John', 1)
p_queue.enqueue('Judy', 4)
p_queue.enqueue('Mark', 3)
p_queue.print_out()
