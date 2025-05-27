def remove_duplicate_words(s):
    new_s = ""
    for word in s.split():
        if not word in new_s:
            new_s += word + " "
    return new_s.strip()
