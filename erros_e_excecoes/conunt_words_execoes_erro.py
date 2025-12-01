def count_words(filename):
    """Conta o número de palarvas em um arquivo.

    Args:
        filename (txt): usando o try exception, caso o arquivo não abrir lançamos uma exeções amigavel para o usuario o desenvolvedor.
    """
    
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg   = "Desculpa, o arquivo " + filename + " não existe."
        print(msg)
    except FileExistsError:
        msg = "Não foi possivel abrir o arquio" + filename
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("O arquivo " + filename + " tem cerca de " + str(num_words) + " palavras.")

filenames = ["text.tex", "moby_dick.txt", "little_woman.txt"]
for filename in filenames:
    count_words(filename)
                