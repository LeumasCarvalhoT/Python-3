def anti_dor(s):
        t_f = False
        while not t_f:
                comeco = str(input(s)).replace(',','.')
                if comeco.strip() == '':
                    print(f'\033[31mERRO: "{comeco}", preço inválido\033[m')    
                elif comeco.strip().isalpha():
                    print(f'\033[31mERRO: "{comeco}", preço inválido\033[m')
                else:
                        t_f = True
                        return float(comeco)
               
                
                
                