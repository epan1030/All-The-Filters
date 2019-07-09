# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image


# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(file_name):
    return Image.open(file_name, mode = 'r')


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(abc):
    img.show(title = None)

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(image_file, new_file_namefile):
    Image.save(new_file_name, "JPEG")

img = load_img("totoro.jpg")
show_img(img)
save_img(img)
# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
# def obamicon():
