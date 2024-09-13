from PIL import Image, ImageDraw



def twist_image(input_file_name, output_file_name):
    im = Image.open(input_file_name)
    x, y = im.size

    left_half = im.crop((0, 0, x // 2, y))
    rigt_half = im.crop((x // 2, 0, x, y))

    im2 = left_half.transpose(Image.FLIP_LEFT_RIGHT)
    im3 = rigt_half.transpose(Image.FLIP_LEFT_RIGHT)

    dev = Image.new('RGB', (x, y))
    ogo = ImageDraw.Draw(im)
    ogo.r

    dev.paste(im2, (0, 0, x // 2, y))
    #dev.paste(im3, (x // 2, 0, x, y))
    dev.save(output_file_name)


twist_image('mage.jpg', 'output.jpg')
