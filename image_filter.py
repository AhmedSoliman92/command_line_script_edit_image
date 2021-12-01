import sys
from PIL import  Image, ImageOps
from my_func.filters import  gray_scale, overlay, mirror_img, rotate_img
from my_func.img_operation import open_image, save_image


try:
    my_files = []
    for arg in range(1,len(sys.argv)):
        if sys.argv[arg].endswith('.png') or sys.argv[arg].endswith('.jpg'):
            my_files.append(sys.argv[arg])
    input = my_files[0]
    output = my_files[1]
    try:
        logo = my_files[2]
    except:
        pass
    image = open_image(input)

except:
    "image is not exist or is not added"
    
try:
    for arg in range(3, len(sys.argv)):
        try:
            degree = float(sys.argv[arg])
        except:
            degree = 0.0
        if sys.argv[arg] == "gray_scale":
            image = gray_scale(image)
        
        elif sys.argv[arg] == 'overlay':

            try:
                overlay(image,logo)

            except:
                print("logo image is not exist or is not added")

        elif degree > 0.0:
            angle = int(sys.argv[arg])
            image= rotate_img(image,angle)
        
        
        
        elif sys.argv[arg] == 'mirror':
            image=mirror_img(image)
            
        # elif sys.argv[arg] == "....":
        #     do some filters
        #     . 
        #     . 
        #     . 
        #     . 
        #     .        
    save_image(image,output)
except:
    pass
    