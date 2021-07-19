#오류가 뜬다 
#파이썬에서 오버로딩 밑에와 같은 방식으로는 불가능

class student:
  def show(self):
    print("학생")
  def show(self,name):
    self.name=name
    print(self.name)
  def show(self,name,uni_name):
    self.name=name
    self.university_name=uni_name
    print("이름 : {} 대학 이름 : {}".format(self.name,self.university_name))
  def show(self,name,uni_name,student_id):
    self.name=name
    self.university_name=uni_name
    self.student_id=student_id
    print("이름 : {}, 대학 이름 : {}, 학번 : {}".format(self.name,self.university_name,self.student_id))
    
ojc=student()
ojc.show()
ojc.show("ojc")
ojc.show("ojc","sejong")
ojc.show("ojc","sejong","17011700")