from node import node
import time 
import os

class linkedList:
  def insert(self, head, pos, data):
    #you can enter 1 or beginning to insert in the first place. If pos(position) is not defined, it defaults to the beginning
    if(pos == '1' or pos == 'beginning' or not pos):
      if(head.get_data() == None):
        head = node(data)
        return head
      r = node(data)
      r.set_nextNode(head)
      head = r
      return head #this method needs to return the head in order to modify it
    elif(pos == 'end' or int(pos) > self.size(head)): #enter end or a position bigger than list size, defaults to end
      r = head
      while(r.get_nextNode() != None):
        r = r.get_nextNode()
      r.set_nextNode(node(data))
    else: #normal behaviour of linked list
      r = node(data)
      p = head
      for i in range(1, int(pos)-1):
        p = p.get_nextNode()
      r.set_nextNode(p.get_nextNode())
      p.set_nextNode(r)
  
  def remove(self, head, pos):
    if(pos == '1' or pos == 'beginning' or not pos): #enter 1 or beginning to remove first item. if pos is not defined, remove first
      head = head.get_nextNode()
      return head
    elif(pos == 'end' or int(pos) > self.size(head)): #enter end or a position bigger than list size, defaults to end
      p = head
      for i in range(1, self.size(head)-1):
        p = p.get_nextNode()
      p.set_nextNode(p.get_nextNode().get_nextNode())
    else:
      p = head
      for i in range(1, int(pos)-1):
        p = p.get_nextNode()
      p.set_nextNode(p.get_nextNode().get_nextNode())
  
  def size(self, head):
    count = 0
    if(head == None or head.get_data() == None): #head == none means that you've added an item and removed the last, head becomes Nonetype
      return count
    else:
      count += 1
      p = head
      while(p.get_nextNode() != None):
        count += 1
        p = p.get_nextNode()
      return count
    
  def isEmpty(self, head):
    #After inserting an item, once I delete everything, head is NoneType
    if(head == None):
      return True
    else:
      #using ternary operator in python
      return True if(head.get_data() == None) else False
    
  def show(self, head):
    pos = input("Digite a posição: ")
    p = head
    if(pos == '1' or pos == 'beginning' or not pos): #pos not defined defaults to the beginning
      return head.get_data()
    elif(pos == 'end' or int(pos) > self.size(head)): #if you enter end or a position that is bigger than the last item, returns last
      p = head
      for i in range(1, self.size(head)):
        p = p.get_nextNode()
      return p.get_data()
    else:
      for i in range(1, int(pos)):
        p = p.get_nextNode()
      return p.get_data()