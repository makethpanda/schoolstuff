from PIL import Image
new_im = Image.open("liberty.jpg")
exif_data = new_im._getexif()
#ouvrir l'explorateur de variables