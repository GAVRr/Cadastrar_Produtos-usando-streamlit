all_numberr_list = []
pair_list = []
odd_list = []

while True:
    number = int(input('Write a number: '))
    all_numberr_list.append(number)

    keep = ''

    while keep not in ['S','N']:
        keep = str(input('do you want keep? [S/N] ')).strip().upper()
        if keep not in ['S','N']:
            print('this option not exist, Try again')
    if keep in ['N']:
         break
    if number % 2 == 0 :
        pair_list.append(number)

    if number % 2 == 1:
        odd_list.append(number)



print('-='*30)
print(f'The all number written {all_numberr_list}')
print('-='*30)
print(f'the pair numbers written {pair_list}')
print('-='*30)
print(f'the odd numbers written {odd_list}')