def part_one():
    f = open('data/03_input.txt')
    content = f.read()
    banks = content.split('\n')
    overall = 0
    for bank in banks:
        d1 = int(0)
        d2 = int(0)
        index = 0
        for i, x in enumerate(bank[:-1]):
            if int(x) > d1:
                d1 = int(x)
                index = i
        for y in bank[index+1:]:
            if int(y) > d2:
                d2 = int(y)
        number = 10*d1+d2
        overall+=number
    print(overall)

def part_two():
    f = open('data/03_input.txt')
    content = f.read()
    banks = content.split('\n')
    overall = 0
    for bank in banks:
        digit_list =[0,0,0,0,0,0,0,0,0,0,0,0]
        d=0
        index = -1
        for n in range(-11,0):
            for i, x in enumerate(bank[:n]):
                if i<index+1:
                    continue
                if int(x) > digit_list[d]:
                    digit_list[d] = int(x)
                    index = i
            d+=1
        for i, x in enumerate(bank): #final iteration because :0 does not make sense
            if i < index + 1:
                continue
            if int(x) > digit_list[d]:
                digit_list[d] = int(x)
                index = i
        bank_sum = ''.join(str(num) for num in digit_list)
        overall+=int(bank_sum)
    print(overall)

if __name__ == '__main__':
    part_two()
