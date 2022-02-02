import sys
from io import BytesIO

from PIL import Image

from find_geocoder import *
from find_organisation import *

toponym_to_find = " ".join(sys.argv[1:])
long, lat, delta1, delta2 = find_geocoder(toponym_to_find)

count = 10
response = find_organisation(long, lat, delta1, delta2, count)

Image.open(BytesIO(
    response.content)).show()