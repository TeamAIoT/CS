class student:
  def __init__(self,kor,mat,eng):
    self.sum=kor+mat+eng
  
  def return_sum(self):
    return self.sum

kor=int(input("국어 점수 : "))
mat=int(input("수학 점수 : "))
eng=int(input("영어 점수 : "))

ojc=student(kor,mat,eng)
print("총점 : %d"%(ojc.return_sum()))



