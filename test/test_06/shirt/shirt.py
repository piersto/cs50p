import sys
from PIL import Image
from PIL import ImageOps


def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        before = sys.argv[1].strip().lower()
        after = sys.argv[2].strip().lower()

        # before = "before.jpeg"
        # after = "after.jpg"

        if not before.endswith(".png") \
                and before.endswith(".jpg") \
                and before.endswith(".jpeg"):
            sys.exit("Invalid input")

        elif not after.endswith(".png") \
                and not after.endswith(".jpg") \
                and not after.endswith(".jpeg"):
            sys.exit("Invalid input")

        if before.endswith(".png") and not after.endswith(".png") \
                or before.endswith(".jpg") and not after.endswith(".jpg") \
                or before.endswith(".jpeg") and not after.endswith(".jpeg"):
            sys.exit("Input and output have different extensions")
        else:
            # shirt = Image.open("C:\PROJECTS\PYTHON\CX50P\shirt.png")
            size = (1200, 1600)

            with Image.open(before) as img:
                after_resized = ImageOps.fit(img, (600, 600))
                after_resized.save("apter_resized.jpg")

            with Image.open("shirt.png") as s_i, Image.open("after_resized") as a_r:
                Image.Image.paste(s_i, a_r)

                after_resized.save("out.jpg")
                print(after_resized.size)

    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == '__main__':
    main()
