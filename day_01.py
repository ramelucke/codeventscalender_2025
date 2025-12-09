def part_one():
    f = open('data/01_input.txt')
    content = f.read()
    codes = content.split('\n')
    x = 0
    position = 50
    for rotation in codes:
        number = int(rotation[1:])
        if rotation[0] == "R":
            position += number
        if rotation[0] == "L":
            position -= number
        if position % 100 == 0:
            x += 1
    print(x)


def part_two():
    f = open('data/01_input.txt')
    content = f.read()
    codes = content.split('\n')
    x = 0
    position = 50
    for rotation in codes:
        number = int(rotation[1:])
        if rotation[0] == "R":
            for i in range(number):
                position += 1
                if position % 100 == 0:
                    x += 1
        if rotation[0] == "L":
            for i in range(number):
                position -= 1
                if position % 100 == 0:
                    x += 1
    print(x)
