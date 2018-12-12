from node import *
from print import *
import os

### COLOR STYLES FOR TERMINAL ########
Style_blueColor = '\x1b[2;37;44m'
Style_blueColorText = '\x1b[0;34;40m'
Style_redColor = '\x1b[0;37;41m'
Style_redColorText = '\x1b[1;31;40m'
Style_greenColor = '\x1b[6;37;42m'
Style_End = '\x1b[0m'
#######################################

printList()
option = int(input("\nEnter your option: "))
print('\n')
tree = None

while(option != 7):

  if(option == 1):
    print(f'\t{Style_blueColor} Insert Contact {Style_End}')
    node = Node()
    node.name = input(f'Enter the name of the contact: ')

    while(not node.name):
      print(f'{Style_redColor}This Field can\'t be blank!{Style_End}')
      node.name = input(f'Enter the name of the contact: ')

    node.email = input('Insert the email of your contact: ')
    node.phone = input('Insert your contact\'s phone no: ')
    tree = insert(tree, node)
    #print('\n')
    #inOrder(tree)
    os.system('pause')
    balanceInOrder(tree)
    tree = checkBalanceWithRotation(tree)
    
  elif(option == 2):
    print(f'\t{Style_blueColor} Search Contact {Style_End}')
    nameSearch = input('Enter the name of the contact to search: ')
    result = searchTree(tree, nameSearch)
    if(result):
      print(f'\n{Style_greenColor}Name:{Style_End} {result.name} ')
      print(f'\n{Style_greenColor}Email:{Style_End} {result.email} ')
      print(f'\n{Style_greenColor}Phone No.:{Style_End} {result.phone} ')
      os.system('pause')
    else:
      print(f'{Style_redColor}The contact doesn\'t exist!{Style_End}')
      os.system('pause')

  elif(option == 3):
    print(f'\t{Style_redColor}Remove Contact{Style_End}')
    nameSearch = input('Enter the name of the contact to remove it: ')
    tree = remove(tree, nameSearch)
    inOrder(tree)
    balanceInOrder(tree)
    tree = checkBalanceWithRotation(tree)
      
  elif(option == 4):
    print(f'\t{Style_blueColor}List of all contacts in alphabetical order {Style_End}')
    inOrder(tree)
    os.system('pause')
  
  elif(option == 5):
    height = treeHeight(tree)
    print(f'\t{Style_blueColor} the height of this tree is {height} {Style_End}')
    os.system('pause')

  elif(option == 6):
    printTree(tree)
    os.system('pause')
  
  else:
    print(f'\t{Style_redColor}Please enter a valid option! {Style_End}')
    os.system('pause')

  print('\n')
  printList()
  option = int(input("\nEnter your option: "))
  print('\n')
else:
  print(f'{Style_greenColor}Exited the program!{Style_End}')
