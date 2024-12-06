"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1, 2, 3]
    lista_nueva = []
    index = 0 

    while index < len(result):
        lista_nueva.append(result[index])
        lista_nueva.append('@')
        index += 1

    return lista_nueva

print(fn_hack_9())