def part_one():
    f = open('data/04_input.txt')
    content = f.read()
    rows = content.split('\n')
    r_id = len(rows)
    c_id = len(rows[0])
    reachable = 0
    for x in range(r_id):
        for y in range(c_id):
            rolls =0
            for a in (x-1,x,x+1):
                for b in (y-1,y,y+1):
                    if (a>=0 and b>=0) and ((a<r_id and b< c_id) and ( a!= x or b != y)):
                            if rows[a][b] == "@":
                                rolls+=1
            if rolls <4:
                reachable +=1
    print(reachable)
    # read as two d array
    # for each @: check if there are up to three @s in x+-1, y+-1
    # if yes, add to sum
if __name__ == '__main__':
    part_one()

# 2134 is too high