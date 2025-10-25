numeros = ('zero', 'um', 'dois','três', 'quatro', 'cinco',
'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'catorze', 'quinze',
'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = ''
while resp != 'n':
    pedido = int(input('Digite um número entre 0 e 20: '))
    if 0 < pedido > 20:
        while pedido < 0 or pedido > 20:
            pedido = int(input('Valor invalido. Digite novamente: '))
    print(numeros[pedido])
    resp = str(input('Deseja continuar?[S/N]: ')).lower()
    if resp == 'n':
        break
