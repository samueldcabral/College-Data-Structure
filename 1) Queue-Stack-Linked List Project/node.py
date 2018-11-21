class node:
  def __init__ (self, data=None, nextNode=None):
    self._data = data
    self._nextNode = nextNode
    
  def get_data (self):
    return self._data    
    
  def set_data (self, newData):
    self._data = newData
    
  def get_nextNode (self):
    return self._nextNode
    
  def set_nextNode (self, other):
    self._nextNode = other
    
  def __str__ (self):
    return " {} ".format(self._data)