
from PIL import Image, ImageOps
from my_func.img_operation import open_image
def gray_scale(image):
    image_copy=Image.new(image.mode, image.size)
    width, height = image.size
    for i in range(0, width):
            for j in range(0, height):
                pixel=image.getpixel((i,j))
                red= pixel[0]
                green= pixel[1]
                blue= pixel[2]
                gray = int((red + green + blue)/3.0)
                image_copy.putpixel((i,j),(gray,gray,gray))
    return image_copy


def overlay(image,logo):
    
    logo_img = open_image(logo).convert('RGBA')
    image.paste(logo_img,(0,0), logo_img)
        
    return image

def rotate_img(img,angle):
    
    img = img.rotate(angle)
    
    return img


def mirror_img(img):
    return ImageOps.mirror(img)