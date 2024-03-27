from rembg import remove
from PIL import Image


#Удаление фона на фото, по средствая нейросети!

input_path = "input.png"
output_path = "output.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)