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
