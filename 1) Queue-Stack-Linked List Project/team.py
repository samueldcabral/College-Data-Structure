class footballTeam:
  def __init__(self, name, titles):
    self._name = name
    self._titles = titles
  def get_name(self):
    return self._name
  def set_name(self, newName):
    self._name = newName
  def get_titles(self):
    return self._titles
  def set_titles(self, newTitles):
    self._titles = newTitles
  def __str__(self):
    return f'{self._name}, {self._titles}'