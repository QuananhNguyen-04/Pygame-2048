import copy
mark=[[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]

def Cloning(list1):
    list_copying = copy.deepcopy(list1)
    return list_copying

tempMark = Cloning(mark)

def compareList(mark, tempMark):
    for i in range (4):
        for j in range(4):
            if mark[i][j] != tempMark[i][j]:
                return False
    return True

def p_Left():
    for i in range(4):
        empty = 0
        pre = 0
        for j in range(4):
            if mark[i][j] != 0:
                if pre == mark[i][j]:
                    empty = empty + 1
                    mark[i][j - empty] = mark[i][j] + 1
                    pre = 0
                else:
                    pre = mark[i][j]
                    mark[i][j - empty] = mark[i][j]
            else:
                empty = empty + 1
        while empty > 0:
            mark[i][4 - empty] = 0
            empty = empty - 1
    print("is n diff?", compareList(mark, tempMark))
    

def isLose():
    check = True
    for i in range(4):
        if i == 3:
            for j in range (4):
                if (j < 3 and mark[i][j] == mark[i][j + 1]):
                    check = False
        else:
            for j in range(4):
                if j == 3:
                    if (mark[i][j] == mark[i + 1][j]):
                        check = False
                else:
                    if (mark[i][j] == mark[i][j + 1]):
                        check = False
                    if (mark[i][j] == mark[i + 1][j]):
                        check = False
    return check

def countAppear():
    count = 0
    for i in range(4):
        for j in range(4):
            if (mark[i][j]):
                count = count + 1
    return count == 16


def p_Right():
    for i in range(4):
        empty = 0
        pre = 0
        for j in range(0, 4):
            if mark[i][3 - j] != 0:
                if pre == mark[i][3 - j]:
                    empty = empty + 1
                    mark[i][3 - j + empty] = mark[i][3 - j] + 1
                    pre = 0
                else:
                    pre = mark[i][3 - j]
                    mark[i][3 - j + empty] = mark[i][3 - j]
            else:
                empty = empty + 1
        while empty > 0:
            mark[i][empty - 1] = 0
            empty = empty - 1
    print("is n diff?", compareList(mark, tempMark))
    
def p_Up():
    for j in range(4):
        empty = 0
        pre = 0
        for i in range(0, 4):
            if mark[i][j] != 0:
                if pre == mark[i][j]:
                    empty = empty + 1
                    mark[i - empty][j] = mark[i][j] + 1
                    pre = 0
                else:
                    pre = mark[i][j]
                    mark[i - empty][j] = mark[i][j]
            else:
                empty = empty + 1
        while empty > 0:
            mark[4 - empty][j] = 0
            empty = empty - 1
    print("is n diff?", compareList(mark, tempMark))

def p_Down():
    for j in range(4):
        empty = 0
        pre = 0
        for i in range(0, 4):
            if mark[3 - i][j] != 0:
                if pre == mark[3 - i][j]:
                    empty = empty + 1
                    mark[3 - i + empty][j] = mark[3 - i][j] + 1
                    pre = 0
                else:
                    pre = mark[3 - i][j]
                    mark[3 - i + empty][j] = mark[3 - i][j]
            else:
                empty = empty + 1
        while empty > 0:
            mark[empty - 1][j] = 0
            empty = empty - 1
    print("is n diff?", compareList(mark, tempMark))


def checkRandValue(x, y, mark, rand_val): 
    if mark[x][y] != 0:
        return True
    else:
        mark[x][y] = rand_val
        print ("in check rand",mark)
        return False

def convert(rand_pos):
    x = int(rand_pos / 4) - 1
    y = 3 - rand_pos % 4
    return x, y