class sports:
  def __init__(self,name):
    self.name=name
  def print_name(self):
    print("sports 입니다.")
  def print_personnel(self):
    print("sports 입니다.")

class soccer(sports):
  def __init__(self,famous_player,personnel):
    self.famous_player=famous_player
    self.personnel=personnel
  def print_name(self):
    print("soccer 입니다.")
    print("유명 선수로는 {}가 있습니다.".format(self.famous_player))
  def print_personnel(self):
    print("PLAY 인원은 {}명 입니다.".format(self.personnel))
    
football=soccer("Heung-min Son",11)
football.print_name()
football.print_personnel()
      


