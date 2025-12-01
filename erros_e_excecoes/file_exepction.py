filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Desculpa, o arquivo " + filename + " não foi encontrado."
    print(msg)

