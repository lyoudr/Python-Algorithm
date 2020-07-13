class Dictionary:
  def __init__(self):
    self.items = {}
  def has(self, key):
    return key in self.items
  def add(self, key, value):
    self.items[key] = value
  def remove(self, key):
    if self.has(key):
      self.items.pop(key)
      return True
    return False
  def get(self, key):
    if self.has(key):
      return self.items[key]
    else:
      return None
  def values(self):
    values = [item for item in self.items.items()]
    return values

dictx = Dictionary()
dictx.add('name', 'Ann')
dictx.add('hobby', 'Piano')
dictx.add('age', '26')
dictx.values()
dictx.get('name')

class HashTable: 
  def __init__(self): 
    self.table = {} 
  # loseloseHashCode to generate key
  def loseloseHashCode(self, key): 
    hash = 0 
    for i in range(0, len(key)): 
        hash += ord(key[i]) 
    return hash % 37 
  def put(self, key, value): 
    position = self.loseloseHashCode(key) 
    try: 
      self.table[position].append({key: value}) 
    except:  
      self.table[position] = list() 
      self.table[position].append({key: value}) 
    return self.print() 
  def get(self, key): 
    position = self.loseloseHashCode(key) 
    if self.table[position]: 
      for item in self.table[position]: 
        for x, y in item.items(): 
          if x == key: 
            return y 
  def remove(self, key): 
    position = self.loseloseHashCode(key) 
    if self.table[position]: 
      for item in self.table[position]:  
        for x, y in item.items():  
          if x == key:  
            self.table[position].remove(item) 
            if len(self.table[position]) == 0: 
              self.table[position] = None 
  def print(self): 
    for i in self.table: 
      if self.table[i] != None:
        print(i, self.table[i])

# Resolve Conflicts
class HashTable2: 
  def __init__(self): 
    self.table = {} 
  # loseloseHashCode to generate key
  def loseloseHashCode(self, key): 
    hash = 0 
    for i in range(0, len(key)): 
        hash += ord(key[i]) 
    return hash % 37  
  def put(self, key, value, position):  
    try:  
      if self.table[position]:
        position += 1
        self.put(key, value, position)
    except:  
      self.table[position] = {key: value}
  def get(self, key, position): 
    if self.table[position]: 
      for x, y in self.table[position].items():
        if x == key:
          print('{}-{}'.format(position, y))
        else:
          position += 1
          self.get(key, position)
  def remove(self, key, position):
    if self.table[position]: 
      for x, y in self.table[position].items():
        if x == key:
          self.table.pop(position)
        else :
          position += 1
          self.remove(key, position)
  def print(self): 
    for i in self.table: 
      if self.table[i] != None:
        print(i, self.table[i])

hash2 = HashTable2()
hash2.put('Tyrion', 'tyrion@gmail.com', hash2.loseloseHashCode('Tyrion'))
hash2.put('Aaron', 'aaron@gmail.com', hash2.loseloseHashCode('Aaron'))
hash2.get('Tyrion', hash2.loseloseHashCode('Tyrion'))
hash2.put('Jonathan', 'jonathan@gmail.com', hash2.loseloseHashCode('Jonathan'))
hash2.put('Jamie', 'jamine@gmail.com', hash2.loseloseHashCode('Jamie'))
hash2.put('Sue', 'sue@gmail.com', hash2.loseloseHashCode('Sue'))
hash2.remove('Sue', hash2.loseloseHashCode('Sue'))
hash2.print()