#!/usr/bin/env python
# coding: utf-8

# ## Первые шаги

# In[1]:


print('ку-ку')


# In[2]:


h = 0
while h< 10:
    h +=1


# In[3]:


x = 2


# In[4]:


x


# In[5]:


x + 12


# In[6]:


x = 11
y = 22
x + y


# In[7]:


def fib(n):
    if n <= 1:
        return 1 
    else:
        return fib(n - 1) + fib(n - 2)


# In[8]:


fib(12)


# In[9]:


li = []
for i in range(1,10):
    li.append(i)
li


# In[10]:


fibs = [(n, fib(n)) for n in range(1,10)]
fibs


# ## Квадратные уравнения

# In[11]:


from math import sqrt

def solve(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return (x1, x2)
    else:
        return 'Вещественных корней нет'


# In[12]:


solve(0.5, 0.125, 0)


# In[13]:


solve(1, 2, 3)


# In[14]:


z1 = complex(1, 2)
z2 = complex(3, 5)
z1, z2
# (z1, z2)


# In[15]:


'z1 = ({}, {})'.format(z1.imag, z2.real)


# In[16]:


import cmath

def csolve(a, b, c):
    d = b**2 - 4*a*c
    x1 = (-b + cmath.sqrt(d)) / (2 * a)
    x2 = (-b - cmath.sqrt(d)) / (2 * a)
    return (x1, x2)


# In[17]:


csolve(1, 2, 5)


# ## Пример использования Map 

# In[18]:


f = lambda x: x**3
list(map(f, range(1, 5)))


# ##  [PIP](https://pypi.org/)

# In[19]:


import matplotlib.pyplot as plt


# In[20]:


import random

random.randint(1, 10)


# In[21]:


f = lambda x: random.randint(1, 10)
points = list(map(f, range(1, 10)))
points


# In[22]:


p = plt.plot(points, 'b.') 


# In[23]:


plt.plot(points)
plt.show()


# In[24]:


x = list(map(f, range(1, 10)))
y = list(map(f, range(1, 10)))
print(x)
print(y)
# ., , , o, v, ^, <	, >, 1, 2, 3, 4, 8, s, p, P, *, h, H, +, x, X, D, d, |, _, 
plt.plot(x, y, 'rD')
plt.show()


# In[25]:


x = list(range(1,200))
fx = [i*i for i in x]

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot#
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes

plt.axes(facecolor='white')
plt.plot(x,fx)
plt.show()


# In[ ]:





# ### Настройки
# https://matplotlib.org/stable/tutorials/introductory/customizing.html

# In[26]:


import matplotlib.pyplot as plt
import matplotlib as mpl

x = list(range(-200, 200))
fx = [i**2 + 2*i - 3 for i in x]

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html?highlight=pyplot#
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axes.html#matplotlib.pyplot.axes

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '-.' #'--'
mpl.rcParams['lines.color'] = 'C0'

plt.axes(facecolor='white')
plt.plot(x,fx)
plt.show()


# In[27]:


import matplotlib.pyplot as plt
plt.plot([1,2],[1,-1], 'ro', markerfacecolor = 'red')
plt.show()


# In[28]:


import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

x = list(range(0, 500, 2))
y = list(map(lambda a: sqrt(a),x))

fig, ax = plt.subplots()

ax.plot(x, y)
ax.grid()

#  Наименование осей
ax.set_xlabel('x')
ax.set_ylabel('sqrt(x)')
  
plt.show()


# In[29]:


import matplotlib.pyplot as plt
import random

# random.randint(1, 10)

vx = [1.0,2.0,3.0]
vy = [1.0,2.0,1.0]

sx = vx[0]
sy = vy[0]

px = []
py = []

for i in range(1,1000):
    r = random.randint(0, 2)
    sx = (sx + vx[r]) / 2
    sy = (sy + vy[r]) / 2    
    px.append(sx)
    py.append(sy)
  
plt.plot(px, py, 'o')
plt.show()


# In[30]:


import random
import matplotlib.pyplot as plt

x = [1.0,2.0,3.0]
y = [1.0,2.0,1.0]

sx = x[0]
sy = y[0]

px = []
py = []

for i in range(1,100000):
    r = random.randint(0, 2)
    sx = (sx + x[r]) / 2
    sy = (sy + y[r]) / 2    
    px.append(sx)
    py.append(sy)

fig, ax = plt.subplots()

# маркеры цветов 'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w' , RGB: #00ff00
ax.scatter(px, py, c = 'red', s = 1)
ax.set_facecolor('black')

# ax.grid()
# ax.set_xlabel('')
# ax.set_ylabel('')
fig.set_figwidth(15)
fig.set_figheight(10)
plt.show()


#  ![ку-ку](https://static.turbosquid.com/Preview/001207/528/WB/600.jpg "описание при наведении")

# In[31]:


import random
import matplotlib.pyplot as plt

count = 10000
x = list(range(1, 7))
y = [0 for i in x]

fig, ax = plt.subplots()

for _ in range(count):
    y[random.randint(0, 5)] += 1

ax.bar(x, y)
# 
y.sort()
#print('{}%'.format(round((y[5] - y[0]) / count * 100, 3)))
stat = [f'{i+1}: {round(y[i] / count * 100)}%' for i in range(0,6)]
print(stat)
plt.show()


# In[32]:


from sympy import *
from sympy.plotting import plot
init_printing()


# In[33]:


x = Symbol('x')


# In[34]:


f = x + 2022
f


# In[35]:


f.subs(x, -77)


# In[36]:


f.subs(x,-210)


# In[37]:


plot(f)
print(f)


# In[38]:


g = sin(x+x)/x
plot(g)
print(g)


# In[39]:


h = x**2
h


# In[40]:


plot(h)
h


# In[41]:


h=-h


# In[42]:


plot(h)
h


# In[43]:


a = 1
b = 0
c = 0
h = a*x**2 + b*x+c
h


# In[44]:


plot(h)
h


# In[45]:


a = 1
b = 3
c = 4
h = a*x**2 + b*x+c
h


# In[46]:


plot(h)
h


# In[47]:


solve(h, x)


# In[48]:


q = x/(x+2)
q


# In[49]:


plot(q)


# In[50]:


fun1 = plot(q,(x,-10,-2.1), show=False)
fun2 = plot(q,(x,-1.9,10), show=False)
fun1.append(fun2[0])
fun1.show()


# In[51]:


x = Symbol('x')
y = 1*x**2 + 2*x - 10
solve(y)


# In[52]:


res = plot(y,(x,-5, 5))

