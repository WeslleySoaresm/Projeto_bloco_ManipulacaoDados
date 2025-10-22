import json

def invert(dicionario_original):
    """Inverte chaves e valores de um dicionário, agrupando chaves com o mesmo valor."""
    dicionario_invertido = {}
    for chave, valor in dicionario_original.items():
        if valor not in dicionario_invertido:
            dicionario_invertido[valor] = []
        dicionario_invertido[valor].append(chave)
    return dicionario_invertido

def desinvert(dicionario_invertido):
    """Reconstrói o dicionário original a partir do invertido."""
    original = {}
    for valor, lista_chaves in dicionario_invertido.items():
        for chave in lista_chaves:
            original[chave] = valor
    return original

def salvar_json(dados, nome_arquivo):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return {}
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return {}

# --- Menu interativo ---
while True:
    print("\n📘 MENU - Inversor de Dicionários")
    print("1 - Criar dicionário e salvar")
    print("2 - Inverter dicionário")
    print("3 - Ver dicionário invertido")
    print("4 - Reverter para original")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\nDigite pares chave:valor (ex: nome:Ana). Digite 'fim' para encerrar.")
        dicionario = {}
        while True:
            entrada = input("Par: ")
            if entrada.lower() == 'fim':
                break
            try:
                chave, valor = entrada.split(":")
                dicionario[chave.strip()] = valor.strip()
            except:
                print("Formato inválido. Use chave:valor.")
        salvar_json(dicionario, "dados.json")

    elif opcao == '2':
        original = ler_json("dados.json")
        invertido = invert(original)
        salvar_json(invertido, "invertido.json")

    elif opcao == '3':
        invertido = ler_json("invertido.json")
        print("\n📂 Dicionário invertido:")
        print(invertido)

    elif opcao == '4':
        invertido = ler_json("invertido.json")
        original = desinvert(invertido)
        print("\n📂 Dicionário reconstruído:")
        print(original)

    elif opcao == '0':
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
