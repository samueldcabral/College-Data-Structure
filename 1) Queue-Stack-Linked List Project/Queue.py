from node import node
import time 

class Queue:
  def top(self, head):
    if(head == None):
      return 'None'
    return head.get_data()
  
  def add(self, head, value):
    if(head != None):
      if(head.get_data() == None):
        head = node(value)
        return head
      p = head
      while(p.get_nextNode() != None):
        p = p.get_nextNode()
      p.set_nextNode(node(value))
      return head
    else:
      head = node(value)
      return head
    
  def remove(self, head):
    #After inserting an item, once I delete everything, my head is NoneType
    if(head == None):
      print("Can't remove from empty Queue")
      time.sleep(2)
    else:
      head = head.get_nextNode()
      return head  
  
  def isEmpty(self, head):
    #After inserting an item, once I delete everything, my head is NoneType
    if(head == None):
      return True
    else:
    #using ternary operator in python
      return True if(head.get_data() == None) else False 
    
  def size(self, head):
    count = 0
    #if the head itself is of Nonetype is diferent than it having a data of None
    if(head == None or head.get_data() == None):
      return count
    else:
      count += 1
      p = head
      while(p.get_nextNode() != None):
        count += 1
        p = p.get_nextNode()
      return count