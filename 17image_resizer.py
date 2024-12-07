from PIL import Image

def resized_image(size1,size2):

  image = Image.open('IMG-20220510-WA0053.jpg')
  print(f"Current size : {image.size}")
#   resized_image=image.resize((500,500)) # fixed hai 
  resized_image=image.resize((500,500))  # esime fixed karege 
  resized_image.save('IMG-20220510-WA0053-' + str(size1) +'.jpg')

size1 =int(input("enter width : ")) 
size2 =int(input("enter lenght : ")) 
resized_image(size1,size2)