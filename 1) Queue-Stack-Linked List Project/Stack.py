from node import node
import time 

class Stack:
  def top(self, head):
    if(head == None):
      return 'None' 
    return head.get_data()
  
  def push(self, head, value):
    if(head != None):
      if(head.get_data() == None):
        head = node(value)
        return head
      p = node(value)
      p.set_nextNode(head)
      head = p
      return head
    else:
      head = node(value)
      return head
    
  def pop(self, head):
    #After inserting an item, once I delete everything, my head is NoneType
    if(head == None):
      print("Can't remove from empty Stack")
      time.sleep(2)
    else:
      head = head.get_nextNode()
      return head
    
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
  
  def isEmpty(self, head):
    #After inserting an item, once I delete everything, my head is NoneType
    if(head == None):
      return True
    else:
    #using ternary operator in python
      return True if(head.get_data() == None) else False 