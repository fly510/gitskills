
def TopThree(filename):

    Word = open(filename)
    words = Word.readline()
    num = words.strip().split(',')
    #print num
    for i in range(0, len(num)):
        if '-' in num[i]:
            (x, y) = num[i].split('-')
            z = x + '.' + y
            #print x
            #print y
            #print z
            num[i] = float(z)
        elif ':' in num[i]:
            (x, y) = num[i].split(':')
            z = x + '.' + y
            num[i] = float(z)
        else:
            num[i] = float(num[i])

    num.sort()
    return(num[0:3])
    WOrd.close()    
    
James = TopThree('james.txt')
Julie = TopThree('julie.txt')
Mikey = TopThree('mikey.txt')
Sarah = TopThree('sarah.txt')

N = {'James': James, 'Julie': Julie, 'Mikey': Mikey, 'Sarah': Sarah}

name = raw_input('> ')
print "%s's Top Tree Times:" % name,
print " ".join(str(n) for n in N[name])


