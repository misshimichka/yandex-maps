import sys
from io import BytesIO

from PIL import Image

from find_geocoder import *
from find_organisation import *

toponym_to_find = " ".join(sys.argv[1:])
long, lat, delta1, delta2 = find_geocoder(toponym_to_find)

response = find_organisation(long, lat, delta1, delta2)

Image.open(BytesIO(
    response.content)).show()