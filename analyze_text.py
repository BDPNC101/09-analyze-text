def analyze_text(text):
#preliminaries
    n = 0
    e_n = text.count("e") + text.count("E") #gives count of instantiations of 'e' or "E" in text
#analysis of text
    for char in text: #gives count of alphabetic characters
        if char.isalpha() == True:
            n += 1
        else:
            pass
#convert to percentage
    e_p = 100 * n / e_n
    str(round(e_p, 2))
#return
    string = "The text contains " + str(n) + " alphabetic characters, of which " + str(e_n) + " (" + str(e_p) + "%) are 'e'."
    return string
