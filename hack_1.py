"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    result = s
    array = []

    txt_array = [result[i:i+3] for i in range(0, len(result), 3)]

    for txt in txt_array:
        if len(txt) == 3:
            content = f"{txt[0]}{txt[1].upper()}{txt[2]}"
            array.append(content)
        else:
            array.append(txt)

    result = "".join(array)
    return result