import re

name = input("What's yoru name? ").strip()

# Verify that name follows the pattern of the re
# () to catch this group

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello {name}")



# if re.search returns right format so if matches == True
# if matches:
    # groups -- the staff in ()
    # last, first = matches.groups()
    # last = matches.group(1)  # group 1 as it's first in the re.
    # first = matches.group(2)  # group 2 as it's second in the re
    # name = f"{first} {last}"
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello {name}")

# print(f"hell {name}")
# if "," in name :
#     last, first = name.split(", ")
#     name = f"hello, {first} {last}"
#
# print(name)
