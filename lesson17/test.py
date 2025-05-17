import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "randominfo")))

import randominfo

person = randominfo.Person()
print(person.full_name, person.gender, person.country, person.address)
