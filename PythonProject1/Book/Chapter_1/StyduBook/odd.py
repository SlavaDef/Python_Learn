from datetime import datetime
import time
import random

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
 21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
 41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

t = 0

#while t<5: also aviable with while
for i in range(5):
   right_this_minute = datetime.today().minute

   time.sleep(random.randint(0, 10))

   if right_this_minute in odds:
     print("This minute seems a little odd.")
   else:
     print("Not an odd minute.")

  # t+=1