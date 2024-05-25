"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""

def fn_hack_7(arr):
    if not arr:
        return [0]
    elif len(arr) == 1:
        return [0]
    else:
        result = [str(i + 1) for i in range(len(arr))]
        i = 1
        while i < len(arr):
            result[i] = int(result[i])
            i += 2
        return result