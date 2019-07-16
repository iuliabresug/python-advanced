class Butoi(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size

butoi1 = Butoi('red', 'big')
butoi2 = Butoi('red', 'big')

print(butoi1==butoi2)
print(id(butoi1))
print(id(butoi2))


class Ball(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __eq__(self,other): #equal
        """Override the default equal operator"""
        if isinstance(other, self.__class__):
            return self.color == other.color and self.size == other.size
        return False

    def __ne__(self,other): #not equal
        return self.color != other.color or self.size != other.size




class Box(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __eq__(self,other): #equal
            """Override the default equal operator"""
            return self.color == other.color and self.size == other.size


    def __ne__(self,other): #not equal
        return self.color != other.color or self.size != other.size


ball1 = Ball('red', 'big')
ball2 = Ball('red', 'big')
ball3 = Ball('blue', 'big')

print(ball1==ball2)
print(ball1!=ball3)

box1 = Box('red', 'big')

print("asdfghjk")
print(ball1==box1)
print(box1==ball1)

#shalow and hard copy
import copy

a=[[1,2,3],[4,5,6]]
b=a

print(a)
print(b)

a[0][1]=0

print("a modified - copy")
print(a)
print(b)

c = copy.deepcopy(a)
a[1][2]=100

print("a modified - hard copy")
print(a)
print(c)