"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""

def fn_hack_2(s):
    result = ''
    for c in s:
        if c.isalpha() and c.lower() not in 'aeiou':
            result += c
    return result