import re


def main():
    t = input("")
    talk = wdm(t)
    print(talk)


def wdm(talk):
    cleaned_up_talk = ''

    for i in talk:
        if i == "puke":
            cleaned_up_talk = re.sub(r"puke", "", talk)
        if i == "hiccup":
            cleaned_up_talk = re.sub(r"hiccup", "", talk)
        else:
            cleaned_up_talk = talk

    return cleaned_up_talk





main()
