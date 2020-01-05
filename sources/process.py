class Process(object):
  def __init__(self, name):
    self.name = name
    self.needs = {}
    self.results = {}

  def need(self, name, quantity):
    self.needs[name] = quantity
    return self

  def result(self, name, quantity):
    self.results[name] = quantity
    return self
