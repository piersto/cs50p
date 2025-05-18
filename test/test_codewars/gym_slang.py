import re


def main():
    s = input("")
    print(gym_slang(s))


def gym_slang(phrase):

    phrase = re.sub("probably", "prolly", phrase)
    phrase = re.sub("i am", "i'm", phrase)
    phrase = re.sub("instagram", "insta", phrase)
    phrase = re.sub("do not", "don't", phrase)
    phrase = re.sub("going", "gonna", phrase)
    phrase = re.sub("combination", "combo", phrase)
    phrase = re.sub("Probably", "Prolly", phrase)
    phrase = re.sub("I am", "I'm", phrase)
    phrase = re.sub("Instagram", "Insta", phrase)
    phrase = re.sub("Do not", "Don't", phrase)
    phrase = re.sub("Going", "Gonna", phrase)
    phrase = re.sub("Combination", "Combo", phrase)
    return phrase


main()

# AI code:

text = "I am probably going to Instagram, but I do not know if it's the best combination."

replacements = {
    "probably": "prob",
    "do not": "don't",
    "Instagram": "***",
    "going to": "***",
    "combination": "***"
}

# Iterating over each word in the dictionary and replacing it using re.sub()
for word, replacement in replacements.items():
    # Replace occurrences of 'word' with 'replacement' in 'text', ensuring whole-word
    # matching using \b (word boundaries)
    text = re.sub(r'\b' + word + r'\b', replacement, text)

print(text)

