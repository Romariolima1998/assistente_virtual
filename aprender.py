import json

pasta = 'c:\\Users\\Public\\Documents\\assistente_virtual.json'


def ler(biblioteca: dict) -> dict:
    try:
        with open(pasta, 'r', encoding='utf-8') as dicionario:
            biblioteca = json.load(dicionario)
    except FileNotFoundError:
        salvar(biblioteca,)

    return biblioteca


def salvar(biblioteca: dict) -> None:
    with open(pasta, 'w', encoding='utf-8') as dicionario:
        json.dump(biblioteca, dicionario,
                  indent=2, ensure_ascii=False)
    return


if __name__ == '__main__':
    salvar({'nome': 'romario'})

    lista = ler({})

    print(lista)

    apagar = lista.pop('nome')
    print(apagar)

    salvar(lista)
