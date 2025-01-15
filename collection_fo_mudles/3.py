from PIL import Image 
imge = Image.open(r"C:\Users\tabi\Desktop\pip.png")
cr = 400 ,0 , 800 ,400
crope = imge.crop(cr).convert('L')
# crope.show()
cr2 = 0 , 400 , 1200 , 800   
crope2 = imge.crop(cr2).convert("L").rotate(180)
crope2.show()