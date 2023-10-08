import json
import requests
from sintetizador_de_voz import voz


pasta = 'c:\\Users\\Public\\Documents\\key_chave_chatgpt.json'


def key_api():
    voz('vosse ainda não tem uma chave de acesso ao chat g p t.,'
        ' vamos consiguir isso., abra seu navegador e acesse o site abaixo')

    print('\n https://platform.openai.com/account/api-keys \n')

    voz(' clique em loguin, depois faça o loguin com seu emeil .,'
        'clique em criar nova chave, copie a chave, feche seu navegador,'
        'cole a chave abaixo e pressione enter')

    key = input('cole a chave aqui..: ')

    with open(pasta, 'w', encoding='utf8') as arquivo:
        json.dump(key, arquivo, indent=2, ensure_ascii=False)
    voz('chave adicionada com sucesso')
    return


def ler(biblioteca: str) -> str:
    try:
        with open(pasta, 'r', encoding='utf-8') as dicionario:
            biblioteca = json.load(dicionario)
    except FileNotFoundError:
        key_api()

    return biblioteca


key = ler('')
headers = {'Authorization': f'Bearer {key}',
           'content-type': 'application/json'}
id_modelo = 'gpt-3.5-turbo-0613'
link = 'https://api.openai.com/v1/chat/completions'


def chatgpt(pergunta: str) -> str:
    chat = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": pergunta}]
    }
    corpo_do_chat = json.dumps(chat)

    requisicao = requests.post(link, headers=headers, data=corpo_do_chat)
    resposta_bruta = requisicao.json()

    try:
        resposta = resposta_bruta['choices'][0]['message']['content']
    except KeyError:
        if "Incorrect API key provided" in resposta_bruta['error']['message']:
            voz(' sua chave pode estar errada por favor repita o processo')
            key_api()
            resposta = 'oque vosse dezeja'
        else:
            resposta = 'ocorreu um erro'
    return resposta


if __name__ == '__main__':
    print(chatgpt('oque e uma inteligencia artificial'))
