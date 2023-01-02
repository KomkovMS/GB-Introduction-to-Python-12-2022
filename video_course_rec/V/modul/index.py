# задача - импортировать переменные и функции из модуля А и В
import moda
from folderb.modb import foo, bar
# import modc
from modc import foo

print(moda.foo)  # foo A
moda.bar()       # bar A


print(foo)  # foo B
bar()       # bar B
