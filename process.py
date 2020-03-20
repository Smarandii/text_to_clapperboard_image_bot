from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def create_image(typeofw, name, fi, group, chron):
    img = Image.open("input.jpg")
    typeofw = typeofw.strip()
    name = name.strip()
    fi = fi.strip()
    group = group.strip()
    chron = chron.strip()

    group_number = group[2::]
    group = group[:2:]

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("verdana.ttf", 30)
    font_bold = ImageFont.truetype("verdana_bold.ttf", 30)

    draw.text((630 - (len(typeofw) // 2 * 17), 255), typeofw, (255, 255, 255), font=font)

    draw.text((630 - (len(name) // 2 * 17), 360), name, (255, 255, 255), font=font)

    draw.text((630 - (len(fi) // 2 * 17), 481), fi, (255, 255, 255), font=font)

    draw.text((405, 595), group, (255, 255, 255), font=font)
    draw.text((445, 595), group_number, (255, 255, 255), font=font_bold)

    draw.text((875, 595), chron, (255, 255, 255), font=font_bold)
    result = img.save("result.jpg")


def formating(text):
    l = ""
    for i in range(len(text) - 1):
        if text[i] + text[i + 1] == ", ":
            l = l + ","
        else:
            l = l + text[i]
    text = l + text[-1]
    return text


def check(text):
    n = 4
    for i in text:
        if i == ",":
            n = n - 1
    return n == 0
