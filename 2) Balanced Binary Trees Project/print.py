import os

def printList():
  os.system('cls')
  print(f'(1) Insert contact')
  print(f'(2) Search contact')
  print(f'(3) Remove contact')
  print(f'(4) List all contacts')
  print(f'(5) Tree height')
  print(f'(6) Show Tree Structure')
  print(f'(7) Exit program')


def printTree(tree):
  print(f'Root: {tree.name} {tree}')
  if(tree.left):
    print(f'Left: {tree.left.name or None} {tree.left}')
  if(tree.right):
    print(f'Right: {tree.right.name or None} {tree.right}')

  #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  #-=-=-=-=-=-=-=-=-=-=LEFT SUBTREE-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  print(f'\nLeft subtree')
  if(tree.left):
    print(f'Root: {tree.left.name} {tree.left}')
    if(tree.left.left):
      print(f'Left: {tree.left.left.name or None} {tree.left.left}')
    if(tree.left.right):
      print(f'Right: {tree.left.right.name or None} {tree.left.right}')

  print(f'\nLeft left subtree')
  if(tree.left.left):
    print(f'Root: {tree.left.left.name} {tree.left.left}')
    if(tree.left.left.left):
      print(f'Left: {tree.left.left.left.name or None} {tree.left.left.left}')
    if(tree.left.left.right):
      print(f'Right: {tree.left.left.right.name or None} {tree.left.left.right}')

  print(f'\nLeft right subtree')
  if(tree.left.right):
    print(f'Root: {tree.left.right.name} {tree.left.right}')
    if(tree.left.right.left):
      print(f'Left: {tree.left.right.left.name or None} {tree.left.right.left}')
    if(tree.left.right.right):
      print(f'Right: {tree.left.right.right.name or None} {tree.left.right.right}')





 #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  #-=-=-=-=-=-=-=-=-=-=RIGHT SUBTREE-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  print(f'\nRight subtree')
  if(tree.right):
    print(f'Root: {tree.right.name} {tree.right}')
    if(tree.right.left):
      print(f'Left: {tree.right.left.name or None} {tree.right.left}')
    if(tree.right.right):
      print(f'Right: {tree.right.right.name or None} {tree.right.right}')   

  print(f'\nRight left subtree')
  if(tree.right.left):
    print(f'Root: {tree.right.left.name} {tree.right.left}')
    if(tree.right.left.left):
      print(f'Left: {tree.right.left.left.name or None} {tree.right.left.left}')
    if(tree.right.left.right):
      print(f'Right: {tree.right.left.right.name or None} {tree.right.left.right}')

  print(f'\nRight right subtree')
  if(tree.right.right):
    print(f'Root: {tree.right.right.name} {tree.right.right}')
    if(tree.right.right.left):
      print(f'Left: {tree.right.right.left.name or None} {tree.right.right.left}')
    if(tree.right.right.right):
      print(f'Right: {tree.right.right.right.name or None} {tree.right.right.right}')
