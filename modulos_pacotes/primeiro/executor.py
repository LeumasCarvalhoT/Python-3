from dindim.equações import meu_modulo
from dindim.formatação import util

valor = util.anti_dor(('Digite um valor: '))
taxa = int(input('Qual o valor da taxa? '))
meu_modulo.reduzidor(valor, taxa)