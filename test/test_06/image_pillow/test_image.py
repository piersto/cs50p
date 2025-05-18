from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
from PIL import Image

def main():
    b = Image.open("before.jpg")
    s = Image.open("shirt.png")
    r_b = ImageOps.fit(b, [600, 600])
    Image.Image.paste(r_b, s, (200,200), 255)
    r_b.save("after.jpg")



if __name__ == '__main__':
    main()
