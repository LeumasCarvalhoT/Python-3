def ver_int(va):
        t_f = True
        while t_f:
                inic = str(input(va))
                if inic.strip() == '':
                    return f'\033[31mO usuário preferiu não informar o valor!\033[m'
                elif inic.strip().isalpha():
                    print(f'\033[31mERRO: "{inic}", digite um número inteiro válido!  \033[m')
                else:
                    t_f = False
                    return f'O valor inteiro está como: {int(inic)}'