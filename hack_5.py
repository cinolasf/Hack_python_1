"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    output = ""

    for char in result:
        if char == 'o':
            output += '0'
        elif char == 'i':
            output += '1'
        elif char == 'a':
            output += '@'
        else:
            output += char

    return output

print(fn_hack_5())