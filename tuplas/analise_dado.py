nums = (int(input('Digite o 1º número: ')),
        int(input('Digite o 2º número: ')),
        int(input('Digite o 3º número: ')),
        int(input('Digite o 4º número: ')),)
print('O número 9 apareceu {} vezes.'.format(nums.count(9)))
if 3 in nums:
    print('O número 3 apareceu na {}º posição.'.format(nums.index(3)+1))
else:
    print('Não há 3 na lista.')
print('Os números pares digitados foram: ', end='')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ')