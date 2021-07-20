class human:
  def __init__(self,name):
    self.name=name

class student(human):
  def __init__(self, name,math_score,eng_score):
      super().__init__(name)
      self.math_score=math_score
      self.eng_score=eng_score
  def print_avg(self):
    self.avg=(self.math_score+self.eng_score)/2
    print("%s의 두 과목의 평균 = %.2f"%(self.name,self.avg))      

name=input("이름을 입력하세요 : ")
math_score=int(input("수학 점수는? : "))
eng_score=int(input("영어 점수는? : "))

ojc=student(name,math_score,eng_score)
ojc.print_avg()
