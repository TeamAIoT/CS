class cQueue:
    #리스트를 이용한 큐 구현
    def __init__(self,size):
        self.top=[]
        for i in range(size):
            self.top.append(None)
        self.rear=0
        self.front=0
        self.size=size
    
    #큐에 원소 삽입
    def enqueue(self, item):
        if(self.isFull()):
            print("Queue is full")
            exit()
        self.rear=(self.rear+1)%self.size
        self.top[self.rear]=item

    #큐에 가장 앞에 있는 원소를 삭제하고 반환   
    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%self.size
            result=self.top[self.front]
            self.top[self.front]=None
            return result
        else:
            print("Queue underflow")
            exit()
    #큐 가장 앞에 있는 원소를 반환
    def peek(self):
        if not self.isEmpty():
            return self.top[self.front]
        else:
            print("underflow")
            exit()
    #스택이 비어있는 지를 bool값으로 반환
    def isEmpty(self) -> bool :
        if self.rear==self.front:
            return True
        else :
            return False
    #스택이 가득찼는 지를 bool값으로 반환
    def isFull(self) -> bool :
        if (self.rear+1)%self.size==self.front:
            return True
        else :
            return False