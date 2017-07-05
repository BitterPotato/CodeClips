# one_line comment
"""Multiline strs, ofen as documentation
"""

# ========== 1. primitive datatypes ===========
print(5 / 3)
print(5.0 / 3.0)
print(5.0 / 3)
# 向下取整
print(5 // 3)
print(5.0 // 3.0)

# 幂运算
print(2**3)

# 大写
a = True
a = False

# 逻辑运算符
print(0 and 1)
print(0 or 1)
print(not 0)

print(0 == False)
print(1 == True)
print(2 == True)

print(True and False)
print(True or False)

# 所有假值
print('')
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(()))
print('')
# 除此以外其他值均为真

# 连锁比较
print(2 < 3 < 2)
print(2 < 3 > 1)

# is和==区别
# is比较同个对象；==比较值是否相同
b = [1, 2, 3]
c = [1, 2, 3]
print(b == c)
print(b is c)

# None是一个对象
# 使用is进行比较，而非==
print(1 is None)

# 字符串""和''均可
# 字符串可被是做字符列表
print("string"[2])
print(len('string'))
# 格式化字符串
print("{} can be {}, and {}, and {}".format('string', 0, True, 0.5))
print("{0} can be {0}, and {1}, and {2}".format('string', 0, True))
print("{key}'value is {value}".format(key='a key', value='a value'))

# ========== 2. variables and Collections ===========
# 默认的print会换行，使用end参数进行修改
print("hello, world", end='')

# 变量名一般使用字母+下划线
# input_str = input("Please enter:")
# print(input_str)

# if-else expression
print("big" if 3 > 2 else "small")

# a. List
li = []
li = [1, 2]
li.append(3)
print(li.pop())
# 返回最后一个元素
print(li[-1])
print(li[-2])

# out of bounds
# print(li[-3])
# print(li[3])

# 深复制（前闭后开）
print(li[0:1])
print(li[0:])
print(li[:1])
print(li[::-1])
# 每两个进行一次复制
li.append(3)
print(li[::2])

# 按照索引删除、插入
del li[2]
print(li)
li.insert(2, 3)

# 按照内容删除、取索引
li.remove(3)
print(li.index(2))

# 检查存在？
print(2 in li)

# list合并
li.extend([6, 7])
print(li)

# b. 元组类似list，但不可变
tup = (1, 2, 3)
# 元组解包
d, *e, f = (1, 2, 3, 4, 5)
print(e)
# 轻松交换
d, f = f, e
print(d)

# c. Dictionaries
empty_dict = {}
filled_dict = {"name": "Red", "age": 18}
# key必须为不可变类型，如int, float, string, tuples
# value可以为任意数据类型，比如list，dict

# 不保证key的顺序
print(list(filled_dict.keys()))
print(18 in filled_dict.values())
# without keyError
# filled_dict.get("test")
# filled_dict.update({"age": 10})
# filled_dict.update({"birth": 2000})
# -- get --
# filled_dict["test"] = 100
# filled_dict["age"] = 10

# with keyError
# filled_dict["test"]

# d. Set
empty_set = set()
filled_set = {1, 2, 4, 5}
# set中元素必须为不可变，可hash
valid_set = {(1, ), 1}
# supported operation
other_set = {3, 4}

print(filled_set & other_set)
print(filled_set - other_set)
print(filled_set ^ other_set)
print(filled_set | other_set)
print({1, 2} >= {1, 2, 3})

# ========== 3. control flow ===========
# range(number)遍历从0到给定数字的那些数字
for i in range(5):
    print(i)
# 变种
# range(lower, upper)
# range(lower, upper, step)

# 异常捕获
try:
    # 抛出异常
    raise IndexError("to say something")
except IndexError as e:
    # no-op
    pass
# can handle errors together
except (TypeError, NameError):
    pass
else:
    print("no exceptions raised")
finally:
    print("called in all circumstances")

# Iterable: can be treated as a sequence
# for example:filled_dict.keys()/ range(5)

# create iterator from iterable
our_iterator = iter(filled_dict.keys())
# 针对iterator的操作
print(next(our_iterator))

# ========== 4. functions ===========
def add(x, y):
    return x+y

# call function
add(5, 6)
# or with keyword arguments
add(y=6, x=5)

# *args: number of positional arguments
# *kwargs: number of keyword arguments
def all_args(*args, **kwargs):
    print(args)
    print(kwargs)

print(all_args(1, 2, a=3, b=4))
# 相对的，可以使用*来扩展元组
# 使用**来扩展dicts
args = (1, 2)
kwargs = {"a": 3, "b": 4}
print(all_args(*args, **kwargs))

def swap(x, y):
    return y, x
    # 可以有多个返回值（as a tuple），圆括号可忽略
    # return (y, x)

# 变量作用域
x = 5

def set_localx(num):
    # refer to local x
    # print(x)
    x = num
    print(x)

set_localx(6)

def set_globalx(num):
    global x
    # then it refer to global x
    print(x)
    x = num
    print(x)

set_globalx(6)

# 函数为一等公民
def create_adder(x):
    def adder(y):
        return x+y
    return adder

adder_10 = create_adder(10)
print(adder_10(3))

# 匿名函数使用
print((lambda x, y: x**2 + y**2)(2,1))

# List/ set/ dict comprehensions
print([adder_10(i) for i in [1, 2, 3]])
print(*(x for x in [3, 4, 5, 6, 7] if x > 5))

print({x for x in 'abcdef' if x not in 'abc'})
print({x: x**2 for x in range(5)})

# ========== 5. modules ===========
# 导入模块
import math
print(math.ceil(3.7))
# 导入模块并起别名
import math as m
print(m.ceil(3.7))
# 打印模块中定义的属性和方法
print(dir(m))
print(m.__doc__)
# 导入模块中的特定函数
from math import ceil
# from math import * 不推荐
print(ceil(3.7))

# Python的模块只是普通的Python文件。我们可以导入我们自己的文件，模块名称也就是文件名称。如果在当前目录下有同样命名为math.py的文件，那么它会被导入而不是build-in Python module.当前目录有更高的优先级

# ========== 6. Classes ===========
class Human:
    # 类属性
    species = "H. sapiens"

    # 形如__method__的方法（对象或属性）被称作特殊方法（对象或属性）
    # 由Python定义及使用，我们不应该创建这种名字的方法（对象或属性）
    # 初始化方法
    def __init__(self, name):
        self.name = name
        self._age = 0

    # 实例方法，self都会作为第一个参数
    # one instance, one method
    def say(self, msg):
        print("{0}: {1}".format(self.name, msg))

    # class method: all instances, one class, one method
    # calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    #static method: without a class or instance reference
    # no instances, no class , one method
    @staticmethod
    def grunt():
        return "*grunt*"

    # make property read-only; implicit getter
    @property
    def age(self):
        return self._age

    # allow the property to be set
    # 如果将下列代码段进行注释，那么'can't set attribute'
    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age

# 当python读代码文件时它会执行所有代码，
# 而对__name__的检查能够确保只有当该module为主程序时才会执行以下的代码段
if __name__ == '__main__':
    i = Human("Johnny")
    j = Human("Joe")
    print(i.get_species)
    print(j.get_species)

    print(Human.grunt())
    # print(i.grunt()) cause error

    i.age = 40
    i.say(i.age)
    del i.age

# ========== 6.1 Multiple Inheritance ===========
class Bat:
    species = 'Baty'

    def __init__(self, can_fly=True):
        self.fly = can_fly

# 多重继承(父类的顺序会影响方法解析的搜索顺序)
class Batman(Human, Bat):
    species = 'Superhero'

    def __init__(self, *args, **kwargs):
        # 显式调用父类初始化方法
        Human.__init__(self, 'anonoymous', *args, **kwargs)
        Bat.__init__(self, can_fly=True, *args, **kwargs)

if __name__ == '__main__':
    sup = Batman()

    if isinstance(sup, Human):
        print("I am human")
    if isinstance(sup, Bat):
        print("I am bat")
    if type(sup) is Batman:
        print('I am Batman')

    # (<class '__main__.Batman'>, <class '__main__.Bat'>, <class '__main__.Human'>, <class 'object'>)
    print(Batman.__mro__)

# ========== 7. Advanced ===========
# Iterable将所有值存储在内存中，当有大量数值的时候它并不总是我们想要的
# Generator只能使用一次，它不将所有值存储在内存中，它生成值on the fly
# yield类似return，但它返回一个Generator

# 将Iterable转换为Generator
# Notice: when you call the function ,the code you have written in the function body does not run, it only returns the generator object.see https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
def double_numbers(iterable):
    for i in iterable:
        yield i+i

for i in double_numbers(range(1, 900000000)):
    print(i)
    if i>= 30:
        break

# generator comprehensions
values = (-x for x in [1, 2, 3, 4, 5])
# 可以将Generator转换为list
values2list = list(values)
print(values2list)

# python装饰器（包装函数的函数，返回修改后的函数对象）使用场景：
# 面向切面编程，可用于插入日志、性能测试等，
# 重用装饰器代码，抽离与函数功能本身无关的代码从而形成
from functools import wraps

def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} trace for performance".format(msg)
        return msg

    return wrapper

@beg
def say(say_please=False):
    msg = "start do somthing"
    return msg, say_please

print(say(say_please=True))