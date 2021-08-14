from pr02_1_1 import Stack

def calc_postfix(data):
    s=Stack()
    for i in data:
        if i != '+' and i !='-' and i !='*' and i !='/':
            s.push(i)
            print(s.peek())
        else:
            second=int(s.pop())
            first=int(s.pop())
            if i=='+':
                result=first+second
            elif i=='-':
                result=first-second
            elif i=='*':
                result=first*second
            elif i=='/':
                result=first/second
            s.push(result)
    final_result=s.pop()
    return final_result


print(calc_postfix("234*+"))
