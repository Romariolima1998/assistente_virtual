from reconhecimento_de_voz import microfone
from Chatgpt import chatgpt
from sintetizador_de_voz import voz
import aprender
import reprodutor
import random


biblioteca_aprender = aprender.ler({})

comando_fechar = ['fechar', 'Fechar assistente virtual', 'tchau']

abrir_reprodutor = ['Abrir reprodutor', 'reproduzir música',
                    'tocar música', 'música', 'tocar', 'tocar som',
                    'reproduzir']
pause_play = ['Play', 'pause', 'continuar',
              'continuar música', 'pausar música', 'pausar']
proxima = ['próxima', 'próximo', 'pular', 'próxima música', 'pular música']
anterior = ['voltar', 'anterior', 'voltar música', 'música anterior']
fechar = ['fechar reprodutor', 'parar', 'parar música', 'parar reprodutor']

while True:
    # chama a funçao microfone----------------------
    reconhecimento_de_voz = microfone('pt-br')
    print(reconhecimento_de_voz)

    # interaçao com o usuario -----------------------------------
    if reconhecimento_de_voz == None:
        probabilidade = random.randrange(0, 5)
        if probabilidade == 2:
            reconhecimento_de_voz = 'me faça outra pergunta com base nos assuntos anteriores, mas nao me diga claro antes de fazer a pergunta apenas faça a pergunta'

        # retorna a funçao microfone para o caht nao pesquisar por none
    if reconhecimento_de_voz == None:
        continue

        # pesquisa os comandos salvos no json pelo usuario
    if reconhecimento_de_voz.replace(' ', '_') in biblioteca_aprender:
        voz(biblioteca_aprender[reconhecimento_de_voz.replace(' ', ('_'))])
        continue

        # aprende novos comandos e slva no json
    if reconhecimento_de_voz == 'aprender':
        voz('formule a pergunta do que devo aprender')
        chave = microfone('pt-BR').replace(' ', '_')
        print(chave)

        voz('agora a resposta dezejada')
        valor = microfone('pt-BR')
        print(valor)

        if chave == None or valor == None:
            voz('falha ao salvar, tente novamente.')
            continue

        biblioteca_aprender.update({chave: valor})

        aprender.salvar(biblioteca_aprender)
        voz('comando salvo com sucesso')
        continue

        # funçao reprodutor de musica ----------------------
    if reconhecimento_de_voz in abrir_reprodutor:
        reprodutor.reproduzir()
        continue

    if reconhecimento_de_voz in pause_play:
        reprodutor.play_pause()
        continue

    if reconhecimento_de_voz in proxima:
        reprodutor.proxima()
        continue

    if reconhecimento_de_voz in anterior:
        reprodutor.anterior()
        continue

    # funçao traduzir
    if reconhecimento_de_voz == 'traduzir':
        voz('fale a frase que vosse dezeja traduzir')
        reconhecimento_de_voz_ingles = microfone('en-US')
        reconhecimento_de_voz = 'traduza ' + reconhecimento_de_voz_ingles

    if reconhecimento_de_voz in fechar:
        reprodutor.fechar()
        continue

        # fecha o programa-------------------------------------
    if reconhecimento_de_voz in comando_fechar:
        voz('fechando assistente virtual')
        break

        # funçao chat gpt do modulo chatgpt e retorna a resposta
    chat = chatgpt(reconhecimento_de_voz)
    print(chat)
    voz(chat)
