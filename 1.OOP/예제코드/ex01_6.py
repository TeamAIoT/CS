class human:
  def __init__(self,name):
    self.name=name
    
class student(human):
  def __init__(self, name,score):
      super().__init__(name)
      self.score=score
      
ojc=student("ojc",100)
print(ojc.name)
print(ojc.score)