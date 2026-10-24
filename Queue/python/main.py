from queue import Queue

if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    q.display()          # 10 20 30
    print(q.dequeue())   # 10
    q.display()          # 20 30