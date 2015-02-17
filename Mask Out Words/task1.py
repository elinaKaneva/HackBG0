import re


def maskOutWords(words, text):
    txt = re.split("(\W+)", text)
    txt_low = [x.lower() for x in txt]

    for word in words:
        while word.lower() in txt_low:
            index = txt_low.index(word.lower())
            asterisk = "*" * len(word)
            txt_low[index] = asterisk
            txt[index] = asterisk

    result = "".join(txt)
    return result
