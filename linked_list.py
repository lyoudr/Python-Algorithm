class Node:
  def __init__(self, element):
    self.element = element
    self.next = None

class LinkedList:
  def __init__(self):
    self.length = 0
    self.head = None
  def append(self, element):
    node = Node(element)
    if self.head == None:
      self.head = node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = node
    self.length += 1
  def removeAt(self, position):
    if position > -1 and position < self.length:
      current = self.head
      index = 0
      if position == 0:
        self.head = current.next
      else:
        while index < position:
          previous = current
          current = current.next
          index += 1
        previous.next = current.next # previous.next will equal to current.next to remove current
      self.length -= 1
      return current.element
  def insert(self, position, element):
    if position >= 0 and position <= self.length:
      current = self.head
      node = Node(element)
      index = 0
      if position == 0:
        node.next = current
        self.head = node
      else:
        while index < position:
          previous = current
          current = current.next
          index += 1
        node.next = current
        previous.next = node
      self.length += 1
  def toString(self):
    current = self.head
    string = ''
    while current:
      string += current.element
      current = current.next
    print('linked_list is =>', string)
  def isEmpty(self):
    return self.length == 0
  def size(self):
    return self.length
  def getHead(self):
    return self.head
  def indexOf(self, element):
    current = self.head
    index = 0
    while current:
      if current.element == element:
        print('index is =>', index)
        return index
      current = current.next
      index += 1

linked_list = LinkedList()
linked_list.append('A')
linked_list.append('B')
linked_list.append('C')
linked_list.append('D')
linked_list.toString()
linked_list.removeAt(1)
linked_list.toString()
linked_list.append('E')
linked_list.toString()
linked_list.indexOf('C')