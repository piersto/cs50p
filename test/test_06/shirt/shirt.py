import sys
from PIL import Image
from PIL import ImageOps


def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        before = sys.argv[1]
        after = sys.argv[2]

        # before = "before.jpg"
        # after = "after.jpg"

        if before.endswith(".png"):
            pass
        elif before.endswith(".jpg"):
            pass
        elif before.endswith(".jpeg"):
            pass
        else:
            sys.exit("Invalid input")

        if after.endswith(".png"):
            pass
        elif after.endswith(".jpg"):
            pass
        elif after.endswith(".jpeg"):
            pass
        else:
            sys.exit("Invalid input")

        if before.endswith(".png") and not after.endswith(".png"):
            sys.exit("Input and output have different extensions")
        elif before.endswith(".jpg") and not after.endswith(".jpg"):
            sys.exit("Input and output have different extensions")
        elif before.endswith(".jpeg") and not after.endswith(".jpeg"):
            sys.exit("Input and output have different extensions")
        else:
            # shirt = Image.open("C:\PROJECTS\PYTHON\CX50P\shirt.png")
            # size = (1200, 1600)

            with Image.open(before) as img:
                before = ImageOps.fit(img, (600, 600))
                before.save("after_resized.jpg")

            with Image.open(r"C:\PROJECTS\PYTHON\CX50P\after_resized.jpg") as a_r, \
                    Image.open(r"C:\PROJECTS\PYTHON\CX50P\shirt.png") as s_i:
                a_r.paste(s_i, mask=s_i)
                a_r.save(after)

    except FileNotFoundError:
        sys.exit("File not found")


if __name__ == '__main__':
    main()
