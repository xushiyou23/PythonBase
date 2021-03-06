"""m面向对象高级编程"""

'''class Student(object):
    pass

s = Student()
s.name = 'xiaoming' #给实力绑定属性
print(s.name)

def printname(self,age):
    print('name-age',age)
from types import MethodType
s.printname = MethodType(printname,s)  #给类 绑定实例 方法 对其他对实例是不管作用对
s.printname(345)

t = Student()
#t.prin对其他对实例是不管作用对

#为了都有用可以给class 绑定
Student.age = printname
tt = Student()
tt.age(455)

class students():
    __slots__ = ('name','age')#用tuple老限制属性名称  只对当前类有作用，对于继承对子类没有作用的


"""限制参数输入范围"""

class stu(object):
    sorce = 0
    def getStu(self):
        print(self.sorce)

    def setsorce(self,value):
        if not isinstance(value,int):
            raise ValueError('sorce must be an interger!')
        if value <0 or value >100:
            raise ValueError('score must between 0~100')
        self.sorce = value

st = stu()
st.setsorce(33)
st.getStu()

'''
'''class student():
    def __init__(self,name):
        self.name = name
    def pri(self):
        print(self.name)
aa = student('xushiyou')
aa.pri()'''

"""使用枚举类型"""
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191235886950998592cd3e426e91687cdae696e64b000
class enuming():
    from enum import Enum
    Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
    for name in Month:
        print(name)

    from enum import Enum, unique
    @unique  # 装饰器帮我们检查没有重复值   进行自定义枚举
    class Weekday(Enum):
        sun = 0
        mon = 1
        tue = 2
        wed = 3
        thu = 4
        fri = 5
        sat = 6

    day = Weekday.mon.value  # 输出当前的值
    print(day)  # 1
    print(day == Weekday.tue)  # Flase  输出的是True 或者 Flase

#enuming()


"""使用元类"""
class Hello(object):
    def hello(self,name='worde'):
        print(name)

# h = Hello()
# print(type(Hello))
# print(type(h))