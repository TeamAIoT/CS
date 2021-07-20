class account:
  num_accounts=0
  def __init__(self,name):
    self.name=name
    account.num_accounts+=1
    #self.num_accounts+=1
    
oh=account("oh")
kim=account("kim")

print(oh.name)
print(kim.name)

print(oh.num_accounts)
print(kim.num_accounts)
