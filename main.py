import random

display_messages = [
    'Seja Feliz :)',
    'Fique tranquilo, tudo vai dar certo!',
    'aasaasdsdsadsa'
]

while True:
    resposta = input('Deseja receber um conselho? S/N: ')
    if resposta == 'S' or resposta == 's':
        mensagem = random.choice(display_messages)
        print(mensagem)
        print()
