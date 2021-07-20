class student:
  def __init__(self,name,classnumber,score):
    self.name=name
    self.classnumber=classnumber
    self.score=score
  def print_student(self):
    print(self.name)
    print(self.classnumber)
    print(self.score)
    
student1=student("ojc",2,100)

student1.print_student()