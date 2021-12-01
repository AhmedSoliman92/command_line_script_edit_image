from PIL import Image


def open_image(filename):
    try:
        img_path = 'input/{}'.format(filename)
        input_img = Image.open(img_path)
        return input_img
    except:
        return 'choose input image please!!'

def save_image(image, filename = 'example.jpg'):
    img_path = 'output/{}'.format(filename)
    try:
        image.save(img_path)
    except:
        pass
