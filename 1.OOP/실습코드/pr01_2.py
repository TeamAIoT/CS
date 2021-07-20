class person:
  def getGender(self):
    return "Unknown"

class male(person):
  def getGender(self):
      return "male"
    
class female(person):
  def getGender(self):
      return "female"
a=person()
b=male()
c=female()
print(a.getGender())
print(b.getGender())
print(c.getGender())