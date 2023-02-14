# 스택 클래스 만들기
class Stack:
    def __init__(self,size):
        self.size = size
        self.items = [None] * size
        self.top = -1
        # 파이썬만 [-1] 이 맨 뒤에값임

    # 값이 비었는지 확인 하는 메서드
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    # 값을 추가 하는 메서드
    def push(self, item):
        # 값이 가득 차지 않았을 때만 추가
        if self.is_full():
            print('스택이 가득 차서 추가 불가')
        else:
            self.top += 1
            self.items[self.top] = item

    def peek(self):
        if self.is_empty():
            raise Exception('스택이 비었다.')
        else:
            return self.items[self.top]

    # 가득 찼는지 확인하는 메서드
    def is_full(self):
        if self.top + 1 == self.size:
            return True
        else:
            return False

    # 값을 제거
    def pop(self):

        if self.is_empty():

            pass
        # 스택이 비어있지 않으면
        else:
            Value = self.items[self.top]
            self.top -= 1
            return Value
# 길이가 5인 스택 생성하기
s1 = Stack(5)
print(s1.items)
print(s1.top)
print(s1.is_empty())
print('='*3, '# s1에 값 A를 추가','='*3)
s1.push('A')
print(s1.items)
print(s1.top)
print(s1.peek())
print('='*3, '# stack이 비어있을때 PEEK은?','='*3)
# s2 = Stack(5)
# print(s2.peek())
print('='*3, '# s1에 rkqt B, C, D,  E를 추가','='*3)
s1.push('B')
s1.push('C')
s1.push('D')
s1.push('E')
print(s1.items)
print(s1.top)
print(s1.peek())
print('='*3, '# s1이 가득 찼을때 값을 추가','='*3)
s1.push('F')
print('='*3, '# s1에서 값을 하나 제거','='*3)
print(s1.pop())
print(s1.items)
print(s1.top)
print(s1.peek())
print('='*3, '# s1에서 다시 값을 추가','='*3)
s1.push('가')
print(s1.items)
print(s1.top)
print(s1.peek())