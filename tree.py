class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  def insert(self, key):
    node = Node(key)
    if self.root == None:
      self.root = node
    else :
      self.insertNode(self.root, node)
  def insertNode(self, node, new_node):
    if new_node.key < node.key:
      if node.left == None:
        node.left = new_node
      else :
        self.insertNode(node.left, new_node)
    else :
      if node.right == None:
        node.right = new_node
      else:
        self.insertNode(node.right, new_node)
  def inOrderTraverse(self, node, callback):
    if node != None: 
      self.inOrderTraverse(node.left, callback)
      callback(node.key)
      self.inOrderTraverse(node.right, callback)
  def preOrderTraverse(self, node, callback):
    if node != None:
      callback(node.key)
      self.preOrderTraverse(node.left, callback)
      self.preOrderTraverse(node.right, callback)
  def postOrderTraverse(self, node, callback):
    if node != None:
      self.postOrderTraverse(node.left, callback)
      self.postOrderTraverse(node.right, callback)
      callback(node.key)
  def minNode(self, node):
    if node:
      while node and node.left != None:
        node = node.left
      print('min is =>', node.key)
      return node.key
  def min(self, node):
    if node:
      while node and node.left != None:
        node = node.left
      return node
  def maxNode(self, node):
    if node:
      while node and node.right != None:
        node = node.right
      print('max is =>', node.key)
      return node.key
  def searchNode(self, node, key):
    if key < node.key and node.left:
      self.searchNode(node.left, key)
    elif key > node.key and node.right:
      self.searchNode(node.right, key)
    elif key == node.key :
      print('found is => {}'.format(node.key))
    else :
      print('Not found')
  def remove(self, node, key):
    if key < node.key:
      node.left = self.remove(node.left, key)
      return node
    elif key > node.key:
      node.right = self.remove(node.right, key)
      return node
    else:
      if node.left == None and node.right == None:
        node = None
        return node
      
      if node.left == None:
        node = node.right
        return node
      elif node.right == None:
        node = node.left
        return node
      
      aux = self.min(node.right)
      node.key = aux.key
      node.right = self.remove(node.right, aux.key)
      return node

tree = BinarySearchTree()
def printNode(value):
  print(value)

tree.insert(7)
tree.insert(15)
tree.insert(5)
tree.insert(3)
tree.insert(9)
tree.insert(8)
tree.insert(10)
tree.insert(13)
tree.insert(12)
tree.insert(14)
tree.insert(20)
tree.insert(18)
tree.insert(25)
# tree.inOrderTraverse(tree.root, printNode)
# tree.preOrderTraverse(tree.root, printNode)
# tree.postOrderTraverse(tree.root, printNode)
tree.minNode(tree.root)
tree.maxNode(tree.root)
tree.searchNode(tree.root, 13)
# tree.remove(tree.root, 14)
tree.inOrderTraverse(tree.root, printNode)
    
