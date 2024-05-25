"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

def fn_hack_3(text):
    mapping = {
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v'
    }
    text = text.lower()
    result = ''

    for char in text:
        if char in mapping:
            result += mapping[char]
        elif char.isdigit():
            result += char.upper()
        else:
            result += char

    result = result[0].upper() + result[1:]
    
    result = result[:-1] + result[-1].upper()

    if len(result) == 2:
        if result[0].isalpha() and result[1].isdigit():
            result = result[0].upper() + result[1]
        elif result[0].isalpha() and result[1].isalpha():
            result = result[0].upper() + result[1].lower()
    return result