import sys
import os
from PIL import Image 


source_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
	os.makedirs(output_folder)


for file in os.listdir(source_folder):
	img = Image.open(f'{source_folder}{file}')
	cleaned_img = os.path.splitext(file)[0]
	img.save(f'{output_folder}{cleaned_img}.png','png')

	print('Conversion complete!')