

text = "dette kan være en string eller en text"

capitalized_string = text.title()
no_space = text.strip()
print(capitalized_string)
print(no_space.replace(" ",""))

return(text)

def to_camel_case(text):
    camel_text = ""
    text_list = text.split(" ") #det som kommer ut er [word1, word2,...]
    for word in text_list: #word = en string ""
        camel_text = camel_text + word[0].upper()+word[1:].lower()
    return(camel_text)
to_camel_case("heisann dette er en test")


def to_camel_case(text):
    camel_text = ''
    text_list = text.split(' ') # ['word1', 'word2', ...]
    for word in text_list: # word = 'word1'
        camel_text = camel_text + word[0].upper()+word[1:].lower()
    return(camel_text)
to_camel_case('heisann dette er en test')
to_camel_case('heisann dEtTe eR eN Test')


def to_camel_case(text):
    camel_text = ''
    caps_lock = True
    for char in text:
        if char==' ':
            caps_lock = True
        elif caps_lock:
            camel_text = camel_text + char.upper()
            caps_lock = False
        else:
            camel_text = camel_text + char
            caps_lock = False
    return(camel_text)
to_camel_case('heisann  dette er en test')
to_camel_case('heisann dEtTe eR eN Test')

