
inputNum = input("Input the value of the coins in here: ")
n = int(inputNum)

coinValue = [25, 10, 5, 1]
output = {25:",", 10:",", 5 :",", 1:""}

sizeofCoin = len(coinValue)

def makeChange(left, i, combination, add):

    if add: combination.append(add)

    if (left == 0) or ((i+1) == sizeofCoin):
        if ((i+1) == sizeofCoin) and (left > 0):
            substitution = (left/coinValue[i], coinValue[i])
            combination.append(substitution)
            i += 1

        while i < sizeofCoin:
            combination.append((0, coinValue[i]))
            i += 1

        print(" ".join("%d %s" % (n,output[c]) for (n,c) in combination))
        return 1

    value = coinValue[i]
    cont = sum(makeChange(left-num*value, i+1, combination[:], (num,value)) for num in range(0, int(left/value)+1))
    return cont

makeChange(n, 0, [], None)
