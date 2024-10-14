import sys
import os

# add path to my directory
local_module_path = os.path.abspath("/Users/marianna/PycharmProjects/demo/Lesson_2-GitHub-/lesson_17/randominfo-master")
sys.path.insert(0, local_module_path)

import randominfo

person = randominfo.Person()
print(person.full_name, person.gender, person.country, person.address)

