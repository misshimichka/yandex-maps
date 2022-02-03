import sys

from find_geocoder import *

toponym_to_find = " ".join(sys.argv[1:])
district = find_district(toponym_to_find)

print(district)