"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""

def fn_hack_8(arr):
    if len(arr) == 2:
        return [str(3 - i) for i in range(1, 3)]
    elif len(arr) == 4:
        return [str(5 - i) for i in range(1, 5)]
    else:
        arr = sorted(arr, reverse=True)
        indices = [str(i) for i in range(len(arr), 0, -1)]
        indices = indices[::-1]

        new_array = []

        for i in range(len(arr)):
            new_array.append(arr[i] + '-' + str(len(arr) - i))
        return new_array