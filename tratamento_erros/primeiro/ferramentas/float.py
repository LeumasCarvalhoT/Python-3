def ver_float(va):
        while True:
            try:
                inic = float(input(va))
            except (ValueError, TypeError):
                print(f'\033[31mERRO: digite um número inteiro válido!\033[m')
                continue
            except (KeyboardInterrupt):
                 print('Sistema interrompido pelo usuário!')
                 break
            return inic
          
            

