import sys
from PIL import Image

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_filename = sys.argv[1]
output_filename = sys.argv[2]

images = []
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)


if not (input_filename.endswith(".png") or input_filename.endswith(".jpg") or input_filename.endswith(".jpeg")) or  not (output_filename.endswith(".png") or output_filename.endswith(".jpg") or output_filename.endswith(".jpeg")):
    sys.exit("Not a image file")


