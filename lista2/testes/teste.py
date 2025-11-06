dado = list()
dado.append('llll')
dado.append(43)
galeria = []
galeria.append(dado[:])
dado[0] = 'suzie'
dado[1] = 98
galeria.append(dado[:])
print(galeria[0 ][0])