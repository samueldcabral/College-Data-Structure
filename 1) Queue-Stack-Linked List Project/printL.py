#lists to print, saves lines on the main program. Theses basically offer a menu with options to selec, eg: insert or remove

def printList(head):
  print("\nThe complete linked list:")
  p = head
  while(p != None):
    print(p) if p.get_data() == None else print(p.get_data().get_name())
    p = p.get_nextNode()
    
def printStack(head):
  print("\nThe complete Stack list\n<---------------------/")
  p = head
  while(p != None):
    print(p, end= '') if p.get_data() == None else print(p.get_data().get_name(), end=' ')
    p = p.get_nextNode()
    
def printQueue(head):
  print("\nThe complete Queue list\n<---------------------/")
  p = head
  while(p != None):
    print(p, end= '') if p.get_data() == None else print(p.get_data().get_name(), end=' ')
    p = p.get_nextNode()
    
def optionLinked():
  option = input("\nEnter your option: \n1- Insert \n2- Remove \n3- is Empty? \n4- Show element \n5- Size of linked list \nEnter 'exit' to finish: > ")
  return option
  
def optionQueue():
  option = input("\n\nEnter your option: \n1- Add \n2- Remove \n3- is Empty? \n4- Size \n5- Top \nEnter 'exit' to finish: > ")
  return option
  
def optionStack():
  option = input("\n\nEnter your option: \n1- Push \n2- Pop \n3- is Empty? \n4- Size \n5- Top \nEnter 'exit' to finish: > ")
  return option