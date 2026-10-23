from stack import Stack

if __name__ == "__main__":
    s = Stack(5)
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)

    s.display()                 # [10, 20, 30, 40, 50]
    print(s.pop())              # 50
    print(s.peek())             # 40
    print(s.peek_from_top(2))   # 20
    s.display()                 # [10, 20, 30, 40]
    