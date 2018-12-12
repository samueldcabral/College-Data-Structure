import time, os

### COLOR STYLES FOR TERMINAL ########
Style_blueColor = '\x1b[2;37;44m'
Style_blueColorText = '\x1b[0;34;40m'
Style_redColor = '\x1b[0;37;41m'
Style_redColorText = '\x1b[1;31;40m'
Style_greenColor = '\x1b[6;37;42m'
Style_End = '\x1b[0m'
#######################################

class Node:
  def __init__(self, name='None', email=None, phone=None, left=None, right=None, bFactor=None):
    self.name = name
    self.email = email
    self.phone = phone
    self.left = left
    self.right = right
    self.bFactor = bFactor

def searchTree(tree, name):
  if(tree is not None):
    if(tree.name == name):
      return tree
    elif(tree.name > name):
      return searchTree(tree.left, name)
    elif(tree.name < name):
      return searchTree(tree.right, name)
  return None

def insert(tree, node):
  if (tree is None):
    print(f'\n\t    {Style_greenColor} Sucess! {Style_End}')
    return node
  elif (tree.name == node.name):
    print(f'{Style_redColor}\tName already exists!!{Style_End}')
  elif (tree.name > node.name):
    tree.left = insert(tree.left, node)
  elif (tree.name < node.name):
    tree.right = insert(tree.right, node)
  return tree

def remove(tree, name):
  if (tree is None):
    return tree
  elif(tree.name == name):
    print('Delete successful!')

    #First case - node is leaf
    if(isLeaf(tree)):
      return None

    #Second case - node has 1 child
    elif(hasOneChild(tree)):
      if(tree.left): #is the child left ?
        tree = tree.left
        tree.left = None
        return tree
      else:
        tree = tree.right
        tree.right = None
        return tree

    #Third case - node has 2 children
    else:
      result = lefty(tree.right)
      [tree.name, tree.email, tree.phone] = [result.name, result.email, result.phone]
      tree.right = remove(tree.right, result.name)
      return tree

  elif(tree.name > name):
    tree.left = remove(tree.left, name)
  elif(tree.name < name):
    tree.right = remove(tree.right, name)
  return tree


def inOrder(tree):
  if(tree is not None):
    inOrder(tree.left)
    print(f'{tree.name}')
    inOrder(tree.right)

def lefty(tree):
  leftyNode = tree
  while(leftyNode.left is not None):
    leftyNode = leftyNode.left
  return leftyNode

def isLeaf(tree):
  if(tree.left == None and tree.right == None):
    return True
  
def hasOneChild(tree):
  if((tree.left is None and tree.right is not None) or (tree.left is not None and tree.right is None)):
    return True

def treeHeight(tree):
  if(tree is not None):
    leftHeight = treeHeight(tree.left)
    rightHeight = treeHeight(tree.right)
    return leftHeight + 1 if(leftHeight > rightHeight) else rightHeight + 1
  return 0

def balanceInOrder(tree):
  if(tree is not None):
    balanceInOrder(tree.left)
    tree = balanceFator(tree)
    balanceInOrder(tree.right)

def balanceFator(tree):
  leftTreeHeight = treeHeight(tree.left)
  rightTreeHeight = treeHeight(tree.right)
  tree.bFactor = leftTreeHeight - rightTreeHeight
  return tree

def checkBalanceWithRotation(tree):
  if(tree is not None):

    tree.left = checkBalanceWithRotation(tree.left)
    
    if(tree.bFactor > 1):
      if(tree.left.bFactor == None):
        print(f'{Style_greenColor}\tSimple Right Rotation{Style_End}')
        os.system('pause')
        tree = rightRotation(tree)
        return tree
      else:
        if(tree.left.bFactor > 0):
          print(f'{Style_greenColor}\tSimple Right Rotation{Style_End}')
          os.system('pause')
          tree = rightRotation(tree)
          return tree

        elif(tree.left.bFactor < 0):
          print(f'{Style_greenColor}\tDouble Right Rotation{Style_End}')
          os.system('pause')
          tree.left = leftRotation(tree.left)
          tree = rightRotation(tree)
          return tree
        else:
          return tree

    elif(tree.bFactor < -1):
      if(tree.right.bFactor == None):
        print(f'{Style_greenColor}\tSimple Left Rotation{Style_End}')
        os.system('pause')
        tree = leftRotation(tree)
        return tree
      else:
        if(tree.right.bFactor <= 0):
          print(f'{Style_greenColor}\tSimple Left Rotation{Style_End}')
          os.system('pause')
          tree = leftRotation(tree)
          return tree
          
        elif(tree.right.bFactor > 0):
          print(f'{Style_greenColor}\tDouble Left Rotation{Style_End}')
          os.system('pause')
          tree.right = rightRotation(tree.right)
          tree = leftRotation(tree)
          return tree
        else:
          return tree
    else:
      return tree

    tree.right = checkBalanceWithRotation(tree.right)


def rightRotation(tree):
  temp = Node()
  temp.right = tree.left.right 
  temp.left = tree.left.left 
  temp.name = tree.left.name

  nodeRotated = temp
  if(tree.left.right == None):
    tree.left = None
  else:
    tree.left = nodeRotated.right
  nodeRotated.right = tree
  return nodeRotated

def leftRotation(tree):
  temp = Node()
  temp.left = tree.right.left 
  temp.right = tree.right.right
  temp.name = tree.right.name
  
  nodeRotated = temp
  if(tree.right.left == None):
    tree.right = None
  else:
    tree.right = nodeRotated.left
  nodeRotated.left = tree
  return nodeRotated