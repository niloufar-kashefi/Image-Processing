import numpy as np
import numpy.linalg as li
c=10
a=np.array([1,1,1,1])
print("a=",a)
b=np.array([2,2,2,2])
print("b=",b)
print("a+b=",a+b)
print("a-b",a-b)
print("a*b",a*b)
print("a/b",a/b)
print("a.dot(b)",a.dot(b))
print("c*a=",c*a)
print("transpos a is: ", a.T)


a=np.array([[1,1,8,1],[1,5,1,3],[1,9,7,1],[1,2,1,6]])
print("a=",a)
b=np.array([[2,2,2,2],[6,1,3,1],[6,1,9,1],[1,4,1,1]])
print("b=",b)
print("a+b=",a+b)
print("a-b",a-b)
print("a*b",a*b)
print("a/b",a/b)
print("a.dot(b)",a.dot(b))
print("c*a=",c*a)
print("transpos a is: ", a.T)
print("det a is: ", li.det(a))
print("inv a is: ", li.inv(a))