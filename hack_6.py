"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""

def fn_hack_6(arr):
    if not arr: 
        return ["0"]
    else:
        result = [str(i + 1) for i in range(len(arr))]
        for i in range(1, len(arr), 2): 
            result[i] = "-"
        return result