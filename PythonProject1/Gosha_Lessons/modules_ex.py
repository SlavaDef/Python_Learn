import time

import datetime as d # as d  - це ніби псевдонім через який тепер можемо звертатися до datetime
import sys
import os
import  platform
#import math # математ функції, це імпорт всієї бібліотеки

from math import sqrt, ceil # це імпорт окремих функцій з бібліотеки



time.sleep(1) # затримка виконання програми
# print(datetime.datetime.now())
print(d.datetime.now())
print(d.datetime.now().year)
print(d.datetime.now().month)

print(sys.path)
print(os.name)
print(platform.system()) # Windows

#print(math.sqrt(25)) # квадратний корінь 5.0
#print(int(math.sqrt(25))) # квадратний корінь 5
#print(math.ceil(math.sqrt(25))) # округлення резалт 5

print(sqrt(25)) # квадратний корінь 5.0
print(int(sqrt(25))) # квадратний корінь 5
print(ceil(sqrt(25))) # округлення резалт 5