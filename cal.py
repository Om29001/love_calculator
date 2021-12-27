global k4
k4 = []
# string to list
def step1(a, m):
    x = "loves"
    k = [a, x, m]
    l = []
    for i in k:
        for j in i:
            l.append(j)
    return l


# coumt
def step2(l):
    k2 = []
    k3 = []
    for i in l:
        if i in k2:
            pass
        else:
            k2.append(i)
            k3.append(l.count(i))
    return k3


# add
def step3(k3):
    l = len(k3)
    while l != 2:
        if l % 2 == 0:
            s = int(l / 2)
            for i in range(s):
                # print("if part",get_digit(k3[i] , 0),get_digit(k3[-(i + 1)],0),k3)
                a = k3[i] + k3[-(i + 1)]
                if a >= 10:
                    a = str(a)
                    for j in a:
                        k4.append(int(j))
                else:
                    k4.append(k3[i] + k3[-(i + 1)])
        else:
            s = int(l / 2)
            for i in range(s):
                c = k3[i] + k3[-(i + 1)]
                # print("else part",get_digit(k3[i] , 0), get_digit(k3[-(i + 1)],0),k3)
                if c >= 10:
                    c = str(c)
                    for j in c:
                        k4.append(int(j))
                else:
                    k4.append(k3[i] + k3[-(i + 1)])
            # print("else ke 2",get_digit(k3[s],0))
            k4.append(k3[s])

        k3 = k4.copy()
        k4.clear()
        l = len(k3)
    else:
        # print(str(k3[0]),str(k3[1]))
        return str(k3[0]) + str(k3[1])


def Calmain(a="ooollll", m="lllloooo"):
    l = step1(a, m)
    k3 = step2(l)
    return step3(k3)
