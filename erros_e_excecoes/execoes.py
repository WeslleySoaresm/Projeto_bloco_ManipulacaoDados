print("Digite dois numeros, e eu os dividirei: ")
print("Digite 'q' para sair.")
      
while True:
    first_number = input("\nPrimeiro número: ")
    if str(first_number).lower() == 'q':
        break
    second_number = input("Seggundo número: ")
    if str(second_number).lower() == 'q':
        break
    try:
        answer = float(first_number)/float(second_number)
    except ZeroDivisionError:
        print("Nã é possivel dividir por zero. por favor repita a operação")
    except ValueError:
        print("Os valores precisam ser reais. Por favor repita a operação.")
    else:
        print(answer)