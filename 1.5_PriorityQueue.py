#主要这个例子中要知道的知识是：
#1:python heapq模块的堆的是最小堆的概念
#2:heapq.heappush()一个元组时，以第一个元素为准，并按堆的概念排列（不等于从小到大）
#3：heapq.heappop()返回的是最小的元素
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue=[]
        self._index=0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        print(self._queue)
        self._index+=1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)

print(q.pop())
print(q.pop())


