"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""

def fn_hack_10(arr):
    array = []
    i = 1
    for item in arr:
        new_item = {}
        for key, value in item.items():
            new_item[str(i)] = str(i + 1)
            i += 2
        array.append(new_item)
    return array