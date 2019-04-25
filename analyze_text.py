def analyze_text(text):
#preliminary
    n = 0
    e_n = text.count("e") + text.count("E")
#analyze
    for char in text: 
        if char.isalpha() == True:
            n += 1
        else:
            pass
#convert to percentage
    e_p = 100 * (e_n / n)
    e_p = format(e_p, '.2f')
#return
    string = "The text contains " + str(n) + " alphabetic characters, of which " + str(e_n) + " (" + e_p + "%) are 'e'."
    return string
