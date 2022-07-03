from PIL import Image, ImageFont, ImageDraw


async def write_on_photo(message):
    img = Image.open('temp/img.jpg')
    img.resize((1, 1), resample=Image.LANCZOS, box=None)
    pix = img.getpixel((1, 1))
    fill = 'white'
    shadowcolor = 'black'
    if (pix[0] + pix[1] + pix[2]) // 3 > 127:
        fill = 'black'
        shadowcolor = 'white'
    font = ImageFont.truetype("fonts/Kashima+RUS.otf", int(img.width / 15))
    draw_text = ImageDraw.Draw(img)
    x = int(img.width / 50)
    y = int(img.height / 4)
    draw_text.text((x - 1, y - 1), message, font=font, fill=shadowcolor)
    draw_text.text((x + 1, y - 1), message, font=font, fill=shadowcolor)
    draw_text.text((x - 1, y + 1), message, font=font, fill=shadowcolor)
    draw_text.text((x + 1, y + 1), message, font=font, fill=shadowcolor)
    draw_text.text((x, y), message, font=font, fill=fill)
    img.save('temp/img.jpg')
    img.close()
