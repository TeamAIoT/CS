class university:
  name=""
  def show(self):
    print("대학교 클래스 입니다.")
    print("대학 이름 : {}".format(self.name))
    
class sejong_university(university):
  def __init__(self,name):
    self.name=name

sejong=sejong_university("sejong")
sejong.show()