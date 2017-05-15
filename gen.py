from PIL import Image, ImageDraw, ImageFont

template_img = Image.open('template.png')
width = template_img.width
height = template_img.height

def gen(name, role, template):
    image = Image.open(template)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("FZXH1K.TTF", width // 4)
    w, h = draw.textsize(name, font)
    draw.text(((width - w) / 2, height * .4),
              name, (86, 86, 86), font)
    font = ImageFont.truetype("Roboto-Thin.ttf", width // 10)
    w, h = draw.textsize(name, font)
    draw.text((width * .54, height * .07),
              role, (137, 137, 137), font)
    return image

tags = (gen(*line.rsplit(maxsplit=1), 'template.png') for line in open('namelist'))

count = 0
last = False
while not last:
    img = Image.new('RGBA', (width * 4, height * 7))
    for w in range(4):
        for h in range(7):
            try:
                tag = next(tags)
            except StopIteration:
                tag = gen('', 'Member', 'template.png')
                last = True
            img.paste(tag, (width * w, height * h))
    count += 1
    img.save('page-%d.png' % count)
