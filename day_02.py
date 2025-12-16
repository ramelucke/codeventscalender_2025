def part_one():
    invalid_ids = 0
    f = open('data/02_input.txt')
    content = f.read()
    ranges = content.split(',')
    for item in ranges:
        a, b = item.split('-')
        for x in range(int(a), int(b) + 1):
            if check_val(x):
                invalid_ids += x
    print(invalid_ids)

def part_two():
    invalid_ids = 0
    f = open('data/02_input.txt')
    content = f.read()
    ranges = content.split(',')
    for item in ranges:
        a, b = item.split('-')
        for x in range(int(a), int(b) + 1):
            if check_complex_val(x):
                invalid_ids += x
    print(invalid_ids)

def check_val(test_id):
    string = str(test_id)
    h_length = int((len(string)) / 2)
    fh = string[:h_length]
    sh = string[h_length:]
    if fh == sh:
        return True
    else:
        return False

def check_complex_val(test_id):
    string = str(test_id)
    length = int(len(string))
    divisors = [i for i in range(1,length) if length % i == 0]
    for x in divisors:
        comp_set = set()
        y = int(length/x)
        for i in range(y):
            chunk=(string[(i*x): ((i+1)*x)])
            comp_set.add(chunk)
            if len(comp_set) !=1:
                break
        if len(comp_set) == 1:
            return True
    return False

if __name__ == '__main__':
    part_one()
    part_two()