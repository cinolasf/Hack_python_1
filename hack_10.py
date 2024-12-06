"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    output = []

    for char in result:
        if char == 'o':
            output.append('0')
        elif char == 'i':
            output.append('1')
        elif char == 'a':
            output.append('@')
        else:
            output.append(char.upper())

    return output

print(fn_hack_10())