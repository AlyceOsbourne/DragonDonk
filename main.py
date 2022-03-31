from core import *

for i in registries:
    print(i.registry.cls)
    for j in i.registry.get_all():
        print("\t->", j)



# todo, write dynamic type creature that can load up dicts from gson,
#  and then create a bunch of types from the abstract classses extending classes
#  take a weapon for instance, an extending class might be polearm, sword, etc
#  so, if we define a way so that we can call material types etc etc fom json we can dynamically create 1000s
#  of items with a few lines of code

