# мы можем импортировать


# import mymodule
import mymodule
import math
# но не можем импортировать наш модуль например на диске С:
#

# как питон находит модули?
import sys

print(sys.path)
print(type(sys.path))  # <class 'list'>

for p in sys.path:
    print(p)

sys.path.append('D:')
