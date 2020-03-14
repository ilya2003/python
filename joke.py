from random import randint

while True:
    file_name = ''
    for digit in range(randint(1, 9)):
        file_name += str(randint(1, 9))

    file_name += ".txt"

    with open(file_name, 'w') as f:
        f.write('Это был Илья')
