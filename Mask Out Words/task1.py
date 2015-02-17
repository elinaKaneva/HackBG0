import re


def maskOutWords(words, text):

    txt = re.split("(\W+)", text)
    txt_low = [x.lower() for x in txt]
    print(txt_low)

    for word in words:
        while word.lower() in txt_low:
            index = txt_low.index(word.lower())
            asterisk = "*" * len(word)
            txt_low[index] = asterisk
            txt[index] = asterisk
            print(txt_low)
            print(txt)

    result = "".join(txt)
    print(result)
    return result

maskOutWords(["E", "jorko", "super"], "Jorko e super e!")
