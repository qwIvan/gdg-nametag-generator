from PIL import Image, ImageDraw, ImageFont

template_img = Image.open('template.png')
width = template_img.width
height = template_img.height

def gen(template, name, role, number=''):
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
    font = ImageFont.truetype("FZXH1K.TTF", width // 30)
    w, h = draw.textsize(name, font)
    draw.text((width * .9, height * .8),
              number, (90, 90, 90), font)
    # image.save('test/'+name+'.png')
    return image

tags = (gen('template.png', *line.rsplit(maxsplit=2)) for line in open('namelist'))

count = 0
last = False
while not last:
    img = Image.new('RGBA', (width * 4, height * 7))
    for w in range(4):
        for h in range(7):
            try:
                tag = next(tags)
            except StopIteration:
                tag = gen('template.png', '', 'Member')
                last = True
            img.paste(tag, (width * w, height * h))
    count += 1
    img.save('page-%d.png' % count)
