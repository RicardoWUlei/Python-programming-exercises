# Python笔记

## 简介

Python优点：

- 轻量化
- 简洁
- 易读

缺点：

- 运行速度慢，执行过程中翻译
- 代码无法加密，解释型语言的问题

### Python解释器

解释器：负责把符合语法的程序代码转换成CPU能够执行的**机器码**

- CPython - 官方解释器
  - 提示符：`>>>`
- IPython - 交互式解释器
  - 提示符：`In[0]`
- PyPy - 动态编译
- Jython - Java平台的解释器

> 如果要在Java或.Net平台交互，最好的办法是通过网络调用交互，保证各模块之间的独立性。

### 命令行和交互模式

- 使用`exit()`退出交互模式

- 命令行模式用来调用`.py`文件

> 用Python开发程序，完全可以一边在文本编辑器里写代码，一边开一个交互式命令窗口，在写代码的过程中，把部分代码粘到命令行去验证，事半功倍！

### 输入和输出

#### 输出

`print()` 每遇到一个逗号，输出一个空格

```python
>>> print('The quick brown fox', 'jumps over', 'the lazy dog')
```

默认直接换行，不换行的话加入option项：`, end=''`

#### 输入

```python
>>> name = input('please enter your name: ')
```

以回车为结尾

> input()返回的是`str`

## Python基础

Python采用缩进分隔区域：

- 格式化代码
- 强迫程序员减少代码块的行数
- 复制-粘贴不友好

> 缩进通常是4个空格

#### 数据类型

##### 整数

- 十六进制：`0x`前缀

- 数字中间可以用`_`作分隔符--和Java一样

##### 浮点数

- `2e1`表示20
- 存储方式导致运算有误差

##### 字符串

- 转义字符
- 单引和双引，首尾保持一致

```python
'I\'m \"OK\"!'
```

- `r''`表示字符串不转义，使用原始内容
- 多行字符串使用`'''...'''`

```python
print('''
a
b
c
''')
```

##### 布尔值

- True/False
- 逻辑运算的结果

##### None

- 空值

##### 变量

- 变量名必须是大小写英文、数字和`_`的组合，且不能用数字开头
- 变量类型不固定 -- 动态语言
- 都是reference-based，用于指向数据对象
- 对变量的赋值就是把数据和变量给关联起来

```python
a = 'ABC'
b = a
a = 'XYZ'
print(b) # 'ABC'
```

> 与Java类似，可以理解`str`是immutable。

##### 常量

- 全大写
- 实际上就是一个变量

整数除法：

```python
>>> 10//3
3
```

只取整数的部分

#### 字符串和编码

Unicode：把所有语言都统一到一套编码里，通常是1个字符对应两个字节

ASCII：只包含英文，1个字符对应1个字节

UTF-8：把Unicode字符根据情况编码成1-6字节。适用于有大量英文的情况。

- 英文字母为1个字节，汉字通常是3个
- 可以兼容ASCII编码
- 节省存储空间

在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

> 网页的源码上会有类似`<meta charset="UTF-8" />`的信息，表示该网页正是用的UTF-8编码。

##### Python字符串

Python3中字符串用**Unicode**编码（放在内存里），因此支持多种语言。

```Python
>>> ord('A')
65
>>> chr(65)
'A'
```

如果放在硬盘或网路上传输时，需要用以字节为单位的`bytes`类型。

```python
x = b'ABC'
```

- `bytes`类型：字符串前加`b`

- `encode()`将`str`编码为指定的`bytes`
- `decode()`把`bytes`解码为`str`

```python
>>> 'ABC'.encode('ascii')
b'ABC'
>>> b'ABC'.decode('ascii')
'ABC'
```

- `bytes`中的字节如果是英文的，会被自动显示为对应的英文

- 中文没法编码为ascii，会报错，可以编码为UTF-8

- `decode()`遇到没法解码的字节会报错

> `len()`函数：
>
> 1. 参数是`str`：返回包含字符个数
> 2. 参数是`bytes`：返回字节个数

```python
>>> len(b'ABC')
3
>>> len('中文'.encode('utf-8'))
6
```

如上所示，英文字母为1个字节，汉字通常是3个。

> 为了避免乱码问题，应当始终坚持使用UTF-8编码对`str`和`bytes`进行转换。

##### 格式化字符串

###### %实现

```python
>>> 'Hello, %s' % ('world')
```

占位符和内容的关系：

| 占位符 |     内容     |
| :----: | :----------: |
|   %d   |     整数     |
|   %f   |    浮点数    |
|   %s   |    字符串    |
|   %x   | 十六进制整数 |

添加格式：

- `%4d`：该整数占四个空格
- `%04d`：该整数前面补一个0，一共占四个空格
- `%7.2f`：该浮点数保留两位小数，一共占7个空格

> 如果字符串中有%符号，用`%%`表示

###### format()

占位符依次按照顺序，{0}, {1}, ...

```python
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'
```

###### f-string()

不使用占位符，直接放入变量

```python
>>> r = 2.5
>>> s = 3.14 * r ** 2
>>> print(f'The area of a circle with radius {r} is {s:.2f}')
The area of a circle with radius 2.5 is 19.62
```

#### List

性质：

- list是一种有序的集合，可以随时添加和删除其中的元素，size可变
- 初始化：`classmates = ['Michael', 'Bob', 'Tracy']`
- list内元素可以是不同类型，也可以是list
- 空数组`l = []`，长度为0

操作：

- 索引访问元素，从0开始，超出范围会报错`IndexError`
- 最后一个元素的索引可以用`-1`表示
- 末尾添加元素：`list.append(item)`
- 指定位置添加元素：`list.insert(index, item)`
- 删除指定位置元素：`list.pop(i=-1)`
  - 缺省为末尾元素
- 更新指定位置元素：直接赋值

#### Tuple

- 元组：有序列表，一旦初始化后，就无法修改
- 元组更加安全
- 初始化：`classmates = ('Michael', 'Bob', 'Tracy')`
- 空元组：`t = ()`

只有一个元素的元组初始化：

```python
a = (2,)
```

> `a = (1)` 表示a是整数1.

如果元组的元素是一个list时，该元素永远指向该list，但是该list是可以修改的。

```python
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
```

#### Dict

key-value存储方式，一个key只对应一个value，key是unique的

dict用空间换取时间，可以高速查找、插入数据，但是内存占用大

- 初始化：`d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}`
- 空字典：`d = {}`

- 取值：`d[key]`

- 更新值：`d[key]=new_value`

  > 如果key不存在就会报错

- 判断key是否存在：

  - `key in d`，不存在时返回False
  - `get()`，不存在时返回None

- 删除key：`pop(key)`

  - key不存在时会报错

> key必须是不可变对象--保证可以hash计算找到该键值对。

#### Set

key的无序集合，key不可重复

- 初始化：`s = set([1, 2, 3])`
  - 自动过滤重复的元素
- 添加元素：`add(key)`
  - 可以重复添加
- 删除元素：`remove(key)`
  - 不存在的元素会报错
- 元素是否在集合中：
  - in语句

> Set和Dict的key都必须是immutable元素，因为都是用hash运算。因此list不能被放入。

## 函数

> 代码抽象/模块化的工作

#### 定义函数

数据类型转换：`int()`

函数名是对函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

```python
>>> a = abs # 变量a指向abs函数
>>> a(-1) # 所以也可以通过a调用abs函数
1
```

函数默认的返回值为`None`，所以`return None`可以写为`return`

空函数：什么都不做，用pass作为占位符，用于没想好怎么写，用作dummy code

```python
def nop():
	pass
```

参数的检查：

- 个数不对可以自动检查
- 参数类型不对，需要额外操作
  - 用`isinstance()`实现，异常处理

```python
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
```

返回多个值：

- 可以实现，但是实质上返回了一个tuple
- tuple可以省略括号，按照位置赋值

```python
x, y = def1(1, 1)
```

#### 函数参数

##### 默认参数

缺省值（便于incremental programming）

- 当不按顺序提供部分默认参数时，需要加上参数名，其他的默认参数正常使用
- 默认参数必须指向不变对象

```python
def add_end(L=[]):
    L.append('END')
    return L
```

重复调用`add_end`会出错，需要更改为：

```python
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

> Python函数在定义的时候，默认参数`L`的值就被计算出来了，即`[]`，因为默认参数`L`也是一个变量，它指向对象`[]`，每次调用该函数，如果改变了`L`的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的`[]`了。

##### 可变参数

传入0个或任意个参数，参数长度不确定，作为一个tuple或list传入，可以用可变参数：

```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

- 在参数前加一个`*`号
- 如果实参是一个list或tuple，可以在传入时加一个`*`

```python
>>> nums = [1, 2, 3]
>>> calc(*nums)
14
```

##### 关键字参数

关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```

- 在虚参前加`**`

```python
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
```

- 同样，可以将一个dict实参加上`**`输入，作为关键字参数

##### 命名关键字参数

- 指定传入的关键字参数的名字，用`*`分隔，后面的参数即为命名关键字参数

```python
def person(name, age, *, city, job):
    print(name, age, city, job)
```

- 同样可以提供缺省值

```python
  def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
```

> 对于任意函数，都可以通过类似`func(*args, **kw)`的形式调用它，无论它的参数是如何定义的。

#### 递归函数

尾递归：理论上可以解决栈溢出的问题，但是Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

> 事实上尾递归和循环的效果是一样的

## 高级特性

#### 切片

选取指定索引范围的元素，适用于`list`、`tuple`和`str`，返回值是原类型。

```python
>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
>>> L[:3]
['Michael', 'Sarah', 'Tracy']
```

- 起始位置缺省为0，终止位置缺省为末尾
- 支持倒数切片
- 支持间隔取数

```python
>>> L[:10:2]
[0, 2, 4, 6, 8]
```

> 每两个取一个元素

- 复制：`L[:]`

#### 可迭代

for循环用于**可迭代对象**：list、dict、tuple、str

判断是否可迭代：`isinstance(object, Iterable)`

```python
>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
```

下标循环：得到**索引-元素对**

```python
>>> for i, value in enumerate(['A', 'B', 'C']):
```

#### 列表生成式

- 快速生成列表

- 可以加`if`判断，用作筛选元素，放在`for`后面

```python
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
```

- `for`循环可以使用多个参数

```python
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']
```

- 使用`if...else`，需要放在`for`前面的表达式中

```python
>>> [x if x % 2 == 0 else -x for x in range(1, 11)]
[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
```

#### 生成器

列表生成式，会受到内存限制。而生成器一边循环一边计算，节省空间。

```python
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>
```

使用方法1：把`[]`换成`()`

- 用next()取值
- enhanced for loop取值

使用方法2：函数内用yield定义生成器

- 在每次调用`next()`的时候执行，遇到`yield`语句返回，再次执行时从上次返回的`yield`语句处继续执行
- 用`yield`语句代替`print`

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
```

如果取出返回值，需要捕获错误，获取`value`：

```python
>>> g = fib(6)
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
```

#### 迭代器

定义：可以被`next()`函数调用并不断返回下一个值，直到没有数据时抛出`StopIteration`错误

`isinstance()`判断：

```python
>>> from collections.abc import Iterator
>>> isinstance((x for x in range(10)), Iterator)
```

> **生成器**都是`Iterator`对象，但`list`、`dict`、`str`虽然是`Iterable`，却不是`Iterator`。
>
> `Iterable`: 可以用enhanced for循环迭代

可以用`iter()`函数把`list`、`dict`、`str`等`Iterable`变成`Iterator`

> 迭代器是一种有序的数据流，但是*长度不确定*。表示一种惰性计算的序列，只有需要取值的时候才会计算。

## 函数式编程

允许把函数本身作为参数传入另一个函数，还允许返回一个函数

#### 高阶函数

定义：传入参数可以是函数的函数

##### map

参数：

1. 函数
2. `Iterable`

返回结果：用传入函数作用到`Iterable`的每个元素中，作为`Iterator`结果返回

```python
map(f, [1,2,3])
```

由于`Iterator`是*惰性序列*，可以使用`list()`将其变为一个list：

```python
list(map(f, [1,2,3]))
```

##### reduce

`reduce`把一个函数作用在一个序列`[x1, x2, x3, ...]`上，这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积计算

```python
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

例子1，将`str`转换为`int`：

```python
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> def char2num(s):
...     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
...     return digits[s]
...
>>> reduce(fn, map(char2num, '13579'))
13579
```

> map返回一个`iterator`，可以作为reduce的第二个参数。

等价于lambda函数：

```python
reduce(lambda x,y: 10*x+y, map(char2num, s))
```

##### filter

过滤序列，接受一个函数和序列

- 函数返回值是bool值
- 根据True or False决定是否保留元素
- 返回一个`Iterator`，一个惰性序列

```python
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]
```

例子：求素数 - 埃式筛法

```python
# 生成奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
# filter的判断函数
def _not_divisible(n):
    return lambda x: x % n > 0
# 定义器 生成下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
```

> 利用iterator的惰性，可以表示”全体素数“

错题：判断一个`int`是否为回数

```python
def is_palindrome(n):
    return str(n) == str(n)[::-1]
```

> 利用切片翻转str

##### sorted

- 对list进行排序，接受一个`key`函数来定义排序的规则
- 函数作用于每个元素上，根据函数返回的结果进行排序
- 反向排序：`reverse=True`

```python
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
['about', 'bob', 'Credit', 'Zoo']
```

按照小写**形式**进行排序，排序后的元素还是原始的元素

#### 返回函数

将函数作为返回值

```python
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
```

外部函数返回内部函数，参数和变量存在返回的函数中，称为**闭包**。

- 局部变量还被新函数引用
- 返回的函数**不会立即执行！！**
- 只有调用了才开始执行

例子：

```python
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
```

调用的结果都是9。因为返回的函数引用了`i`，但不是立即执行，执行的时候`i`已经是3了。

> 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

如果要用循环变量，就*在闭包函数外再套一个函数*，用这个函数的参数来绑定循环变量当前的值。

```python
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
```

> 注意，立即执行`f`函数，此时参数是确定的循环变量。也可以用`lambda`函数简单实现。

**错题：**利用闭包返回一个计数器函数，每次调用它返回递增整数

1. 用`nonlocal`声明变量

```python
def createCounter():
    i = 0
    def counter():
        nonlocal i
        i = i + 1
        return i
    return counter
```

2. 用`list`

```python
def createCounter():
    c = [0]
    def counter():
        c[0] = c[0] + 1
        return c[0]
    return counter
```

3. 写一个生成器

```python
def createCounter():
    def number():
        i = 0
        while True:
            i += 1
            yield i
    g = number()
    def counter():
        return next(g)
    return counter
```

#### 匿名函数

不显式的定义函数

- 关键字`lambda`表示匿名函数
- 冒号前为函数参数，冒号后的表达式就是返回值

- 限制：只能有一个表达式

#### 装饰器

https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584

#### 偏函数

将一些函数的某些参数固定下来，设为**默认值**(调用时仍然可以用别的值)

```python
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
```

当函数的参数个数太多，需要简化时，使用`functools.partial`可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

## 模块

为什么？：便于维护代码

- 一个py文件对应一个模块
- 避免函数名冲突
- 引入包，避免模块名冲突
- 每一个包目录下面都会有一个`__init__.py`的文件，这个文件是必须存在的
- `__init__.py`本身就是一个模块，模块名就是包名

> 自定义的包名字尽量要和系统自带的模块不同。

#### 使用模块

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'
```

标准开头：

1. 编译方式
2. 编码方式
3. 任何模块代码的第一个字符串都被视为模块的文档注释
4. 作者

```python
if __name__=='__main__':
    test()
```

只有我们用命令行运行程序时，`__name__`为`__main__`。而从别的程序中调用该模块，`if`判断无法通过。

可以用于写测试代码。

#### 作用域

- 公开：正常的函数名和变量名
- 特殊变量：如`__name__`，`__author__`
- 私有：`_name`或`__name`的形式，不建议直接引用

> 不**建议**不代表**不能**。
>
> 这样做是为了进行封装，外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

## 面向对象编程

在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。

面向对象的设计思想是抽象出Class，根据Class创建Instance。

三个特点：

1. 数据封装
2. 继承
3. 多态

> 类是抽象的模板，实例是根据类创建出来的具体的对象。

- 定义一个特殊的`__init__`方法，在创建实例的时候，强制输入属性。
  - `__init__`方法第一个参数就是self，调用时解释器自动传入
  - 调用和`constructor`类似

#### 数据封装

- 成员函数从内部调用数据，把数据封装起来。
- 类中的函数定义，第一个参数是`self`，其他的和普通函数一样
- 调用函数不需要知道内部的实现细节

> Python*允许对实例变量绑定任何数据*，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同。

#### 访问限制

**私有变量**：实例的变量名以`__`开头，只有内部可以访问，外部不能访问

- 如果希望修改私有变量，需要添加内部函数作为接口，更改变量
- 保障修改数据的安全性，可以做类型检查

**特殊变量**：以双下划线开头，并且以双下划线结尾的，可以直接访问

- 以一个下划线开头的实例变量名，外部可以访问，但是不建议直接访问
- 双下划线开头的实例变量其实也可以从外部访问，只是解释器修改了变量名

例子：

```python
>>> bart = Student('Bart Simpson', 59)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'
```

> 这种情况只是设置了一个新的`__name`变量，并没有改变内部的私有变量`__name`。

#### 继承

定义方式：`class subclass(superclass):`

- 子类可以继承父类的全部功能
- 子类可以添加自己的方法
- 子类也可以重写父类的方法 - override

> 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行。用于赋值和参数传入
>
> 和Java类似，object是所有类的父类。

#### 多态

- 新增子类，不需要对依赖父类作为参数的函数做修改就可以运行
- 开闭原则：
  - 对扩展开放：允许新增`Animal`子类；
  - 对修改封闭：不需要修改依赖`Animal`类型的`run_twice()`等函数。

- 对于动态语言，传入对象只要能运行所需要的函数就可以
- 不要求严格的继承体系 - python无法约束传入参数的类型

> 鸭子类型：一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子

#### 对象的信息

- `type()`函数

  - 返回对应的Class类型
  - 判断一个变量是否为函数：`type(fn)==types.FunctionType`

- `isinstance()`函数

  - 判断对象的类型
  - 单个类型：`isinstance('a', str)`
  - 多类型判断：`isinstance([1, 2, 3], (list, tuple))`

- `dir()`函数

  - 返回了list，包含对象所有的属性和方法

- `getattr()`、`setattr()`以及`hasattr()`

  - 获取或更改对象的状态

  - ```python
    hasattr(obj, 'x') # 有属性'x'吗？
    ```

  - ```python
    getattr(obj, 'y', default=404) # 获取属性'y'，若不存在，返回缺省值404
    ```

  - ```python
    setattr(obj, 'y', 19) # 设置一个属性'y'
    ```

#### 类属性

- 属于类本身的属性，直接在class中进行定义
- 使用`类名.类属性名`访问

- 所有的实例都可以访问

实例属性：定义在`__init__`中

> 如果实例属性和类属性同名，优先展示实例属性

```python
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student
```

## 高级面向对象编程

#### slots变量

用特殊的`__slots__`变量，来限制该class实例能添加的属性

- 不在slots变量里的属性名，无法进行绑定
- `__slots__`定义的属性**仅对当前类**实例起作用，*对继承的子类是不起作用*的

- 子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

#### @property

1. 将setter和getter变成属性表示
2. 可以定义只读属性和可读写的属性

#### 多重继承

- 一个子类就可以同时获得多个父类的所有功能

- 定义的时候括号里写多个父类名
- 属于mixIn的设计，无需复杂的继承关系

> Java只允许单一继承，不能使用MixIn的设计

#### 类的定制函数

1. `__str__()`：返回一个字符串，用于print函数的调用（给用户看）
2. `__repr__()`：返回程序开发者看到的字符串
3. `__iter__()`：返回一个迭代对象，用`for in`循环对象
4. `__next__()`：不断调用该迭代对象的`__next__()`方法拿到循环的下一个值，直到遇到`StopIteration`错误时退出循环

EX：

```python
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
```

5. `__getitem__()`：类似list的random access

EX：

```python
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
Fib()[5]
```

如果是切片的话，需要判断n的类型是否为切片，然后返回一个list。

6. `__getattr__()`：当我们调用不存在的属性时，可以返回一个default值，不throw error。
   1. 已有的属性不会再`__getattr__()`中查找
   2. 可以用于只相应特定属性，其余的抛出error

7. `__call__()`：调用对象本身的函数

```python
>>> s = Student('Michael')
>>> s() # self参数不要传入
My name is Michael.
```

#### 枚举类

#### 元类



## 错误、调试和测试

如果错误是程序编写错误，也就是coder的问题 ，那就是bug，bug是必须修复的。

如果是用户的输入造成的，那就让用户检查自己的输入

如果是运行过程中无法预测的错误，成为异常，需要做异常处理。

### 错误处理

- 内置了一套`try...except...finally...`的错误处理机制
- 当我们认为某些代码可能会出错时，就可以用`try`来运行这段代码，如果执行出错，则**后续代码不会继续执行**，而是直接跳转至错误处理代码，即`except`语句块，执行完`except`后，如果有`finally`语句块，则执行`finally`语句块。
- 没有错误发生，所以`except`语句块不会被执行，但是`finally`如果有，则一定会被执行（可以没有`finally`语句）。
- 一个`try`语句后，可以捕捉多个`exception`，按照排列的顺序依次检查，因此排列时应注意子类在前，大类在后，避免覆盖。
- 同时 ，`try`语句中函数抛出的`exception`也可以检测到。
- 对应的，如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。
- 也可以自己接住`exception`，用`logging`记录错误信息，然后继续执行程序。

```python
import logging
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
```

#### 主动抛出错误

使用raise语句主动抛出错误。

EX：

```python
# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
```

`except`接住错误后，接着`raise`。`raise`语句如果不带参数，就会把当前错误原样抛出。如果这个问题自己无法解决，就将问题继续向上一级抛。

### 调试

#### assert断言

```python
assert n != 0, 'n is zero!'
## 等价于
if not n != 0:
    raise AssertionError('n is zero!')
```

如果此处表达式不为`True`，就`raise`一个`AssertionError`。

#### logging

类似于print，但是可以进行分组输出 ，也可以打印到文本中 。

#### pdb

Python的调试器，用参数`-m pdb`运行，单步运行程序，查看变量的状态。

类似于Java的gdb调试器。

#### IDE

添加断点，进行调试。

### 单元测试



[to be continued](https://www.liaoxuefeng.com/wiki/1016959663602400/1017604210683936)



