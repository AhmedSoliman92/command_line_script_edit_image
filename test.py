from my_func.img_operation import open_image
from my_func.filters import gray_scale, rotate_img, mirror_img, overlay
import pytest



def test_error_open_image(image_input):
    img = open_image(image_input[1])
    assert img == 'choose input image please!!'


def test_open_image(image_input):
    img = open_image(image_input[0])
    assert  img.mode in ['RGB','L','RGBA','1']
    
    
def test_gray_scale(image_input):
    image = open_image(image_input[0])
    output = gray_scale(image)
    assert [
        output.getpixel((i,j))[0]*3 for i in range(0, output.width) for j in range(0, output.height)
        ] == [
            (output.getpixel((i,j))[0]+output.getpixel((i,j))[1]+output.getpixel((i,j))[2]) for i in range(0, output.width) for j in range(0, output.height)
            ]
        
        
def test_rotate_img(image_input):
    image = open_image(image_input[0])
    output = rotate_img(image,180)
    output = rotate_img(output,180)
    assert [
        output.getpixel((i,j)) for i in range(0, output.width) for j in range(0, output.height)
        ] == [
            image.getpixel((i,j)) for i in range(0, image.width) for j in range(0, image.height)
            ]


def test_mirror_img(image_input):
    image = open_image(image_input[0])
    output = mirror_img(image)
    assert [
        output.getpixel((i,j)) for i in range(0, output.width) for j in range(0, output.height)
        ] == [
            image.getpixel((i,j)) for i in range(image.width-1,-1,-1) for j in range(0, image.height)
            ]
        
        
def test_overlay(image_input):
    image = open_image(image_input[0])
    logo = open_image(image_input[2])
    output = overlay(image,image_input[2])
    diff = [
        output.getpixel((i,j)) for i in range(0, logo.width) for j in range(0, logo.height)
        ] == [
            logo.getpixel((i,j)) for i in range(0,logo.width) for j in range(0, logo.height)
            ]
    assert not diff