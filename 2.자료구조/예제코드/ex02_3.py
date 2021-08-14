class Queue:
    #리스트를 이용한 큐 구현
    def __init__(self):
        self.top = []
        self.rear=0
        self.front=0
    
    #큐에 원소 삽입
    def enqueue(self, item):
        self.top.append(item)
        self.rear+=1

    #큐에 가장 앞에 있는 원소를 삭제하고 반환   
    def dequeue(self):
        if not self.isEmpty():
            result=self.top[self.front]
            #원소를 삭제했단 의미로 0삽입
            self.top[self.front]=0
            self.front+=1
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

