class Node:
  def __init__(self, c, power):
    self.c = c
    self.power = power
    self.prev = None
    self.next = None

class List:
  def __init__(self):
    self.head = Node(None, None)
    self.head.next = self.head
    self.head.prev = self.head
    self.n = 0
  def insert_after(self, x, c, power):
    if self.size() == 0:
      raise Exception("List is empty.")
    y = Node(c, power)
    self.n += 1
    y.prev = x
    y.next = x.next
    x.next = y
    y.next.prev = y
    return y
  def insert(self, c, power):
    self.n += 1
    x = self.head.next
    while x != self.head and x.power > power:
        x = x.next
    self.insert_after(x.prev, c, power)
  def get(self, ind):
    if ind >= self.size():
      raise Exception("Out of list")
    x = self.head.next
    for i in range(ind):
      x = x.next
    return f"c : {x.c}, power : {x.power}"
  def find(self, c, power):
    x = self.head.next
    for i in range(self.size()):
      if x.c == c:
        if x.power == power:
          return x
      x = x.next
    raise Exception("Doesn't exist")
  def delete(self, x):
    if self.size() == 0:
        raise Exception("List is empty")
    self.n -= 1
    x.prev.next = x.next
    x.next.prev = x.prev
    return x
  def size(self):
    return self.n
  def add(self, c1, power1, c2, power2):
    node1 = self.find(c1, power1)
    node2 = self.find(c2, power2)
    node1.c += node2.c
    self.delete(node2)
    return None
  def mul(self, c1, power1, c2, power2):
    node1 = self.find(c1, power1)
    node2 = self.find(c2, power2)
    if node1.power == node2.power:
      result_c = node1.c * node2.c
      result_power = node1.power
      self.delete(node1)
      self.delete(node2)
      self.insert(result_c, result_power)
    elif node1.c == node2.c:
      result_c = node1.c
      result_power = node1.power + node2.power
      self.delete(node1)
      self.delete(node2)
      self.insert(result_c, result_power)
    else:
      raise Exception("multiply operation can't be done!")
    
lst = List()
while True:
  print("1-Input")
  print("2-Summation")
  print("3-Multiply")
  print("4-Exit")
   
  s = int(input("Enter Order Number: "))

  if s == 1:
    C1 = int(input("Enter C1: "))
    Power1 = int(input("Enter Power1: "))
    lst.insert(C1, Power1)
    C2 = int(input("Enter C2: "))
    Power2 = int(input("Enter Power2: "))
    lst.insert(C2, Power2)
  elif s == 2:
    lst.add(C1, Power1, C2, Power2)
    print(lst.get(0))
  elif s == 3:
    lst.mul(C1, Power1, C2, Power2)
    print(lst.get(0))
  elif s == 4:
    break
  else:
    print("Invalid Order number")
