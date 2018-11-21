from printL import *
from Stack import Stack
from node import node
from Queue import Queue
from LinkedList import linkedList
from team import footballTeam
import os 
import time

listtype = 0
while(listtype != 'exit'):
  os.system('clear')
  listtype = input("\n1- Linked list \n2- Queue \n3- Stack\nEnter 'exit' to finish\nWhat do you want to create: ")
  
  if(listtype == '1' or listtype == 'list'):
    head = node()
    linkedList = linkedList()
    option = 0 
    while option != 'exit':
      printList(head)
      option = optionLinked()
      
      if option == '1':
        pos = input("Insert position: ")
        [name, titles] = input('Enter team and their titles e.g. (name, titles): ').split(', ')
        data = footballTeam(name, titles)
        os.system('clear')
        #the next if statement is to allow for head = linkedList
        #instead of linkedList.method
        if(pos == '1' or pos == 'beginning' or not pos):
          head = linkedList.insert(head, pos, data)
          os.system('clear')
        else:
          linkedList.insert(head, pos, data)
          os.system('clear')
      
      elif option == '2':
        if(head.get_nextNode() == None):
          head = node()
          os.system('clear')
        else:
          pos = input("Remove position: ")
          if(pos == '1' or pos == 'beginning' or not pos):
            head = linkedList.remove(head, pos)
            os.system('clear')
          else:
            linkedList.remove(head, pos)
            os.system('clear')
      
      elif option == '3':
        os.system('clear')
        print(f'\nIs the list empty? {linkedList.isEmpty(head)}')
      
      elif option == '4':
        show = linkedList.show(head)
        os.system('clear')
        print(f'\nItem: {show}')
        
      elif option == '5':
        os.system('clear')
        print(f'\nThe size is: {linkedList.size(head)}')
      else:
        break;
        
  elif(listtype == '2' or listtype == 'queue'):
    head = node()
    queue = Queue()
    option = 0 
    while option != 'exit':
      printQueue(head)
      option = optionQueue()
      
      if option == '1':
        [name, titles] = input('Enter team and their titles e.g. (name, titles): ').split(', ')
        data = footballTeam(name, titles)
        head = queue.add(head, data)
        os.system('clear')
      
      elif option == '2':
        head = queue.remove(head)
        os.system('clear')
      
      elif option == '3':
        os.system('clear')
        print(f'\nIs the Queue empty? {queue.isEmpty(head)}')
      
      elif option == '4':
        os.system('clear')
        print(f'\nSize of the current Queue is {queue.size(head)}')
      
      elif option == '5':
        os.system('clear')
        print(f'\nThe current top of the Queue is {queue.top(head)}')
      else:
        break;
        
  elif(listtype == '3' or listtype == 'stack'):
    head = node()
    stack = Stack()
    option = 0 
    while option != 'exit':
      printStack(head)
      option = optionStack()
      
      if option == '1':
        [name, titles] = input('Enter team and their titles e.g. (name, titles): ').split(', ')
        data = footballTeam(name, titles)
        head = stack.push(head, data)
        os.system('clear')
      
      elif option == '2':
        head = stack.pop(head)
        os.system('clear')
      
      elif option == '3':
        os.system('clear')
        print(f'\nIs the stack empty? {stack.isEmpty(head)}')
      
      elif option == '4':
        os.system('clear')
        print(f'\nSize of the current stack is {stack.size(head)}')
      
      elif option == '5':
        os.system('clear')
        print(f'\nThe current top of the Stack is {stack.top(head)}')
      else:
        break;
