import musicbrainzngs as mb
from PIL import Image
import os

result_file = 'result_file'

with open(result_file, 'wb') as file_handler:
    file_handler.write(artwork)

Image.open(result_file).save(result_file + '.png', 'PNG')

os.remove(result_file)