#덧셈,뺄셈이 가능한 계산기 class
class calculator:
  def add(self,a,b):
    return a+b
  def minus(self,a,b):
    return a-b
  
a=calculator()

print(a.add(3,4))
print(a.minus(5,4))
