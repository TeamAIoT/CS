#오버라이딩
class university:
  def show(self):
    print("대학교 클래스 입니다.")
    
class student(university):
  def __init__(self,name,uni_name):
    self.name=name
    self.university_name=uni_name
  def show(self):
    print(self.name)
    print(self.university_name)

uni=university()
uni.show()

ojc=student("ojc","sejong")
ojc.show()