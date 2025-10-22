import json

def invert(dicionario_original):
    # Cria um novo dicionário vazio
    dicionario_invertido = {}

    # Para cada chave e valor no dicionário original
    for chave, valor in dicionario_original.items():
        # Se o valor ainda não existe como chave no novo dicionário
        if valor not in dicionario_invertido:
            dicionario_invertido[valor] = []  # Cria uma lista vazia
        # Adiciona a chave original à lista
        dicionario_invertido[valor].append(chave)

    return dicionario_invertido


def salvar_em_json(dados, nome_arquivo):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")


# --- Exemplo de uso ---
dicionario = {1: 2, 3: 4, 5: 6, 7: 2}
invertido = invert(dicionario)

print("Dicionário invertido:")
print(invertido)

salvar_em_json(invertido, "invertido.json")
