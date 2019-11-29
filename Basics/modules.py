#core modules
import datetime
from datetime import date
import time

#pip module
from camelcase import CamelCase

#today = datetime.date.today()
today = date.today()
timestamp = time.time()

c = CamelCase()
print(c.hump("hello there"))

# print(today)
# print(timestamp)