import random

#M = [2, 2, 2]
nu = raw_input('How many people are involved in the game?\n(within 5)> ')
num = int(nu)

x =  raw_input('How much do you bet?\n(within 5)> ')
y = int(x)


M = num*[y]
print  M
print "\n-------------------------------"

g = raw_input("What number do you bet?\n> ")
guess = int(g)

while num > 5 or y > 5:
    print "You are gambling! Please reduce your bet or number of entries." 
    nu = raw_input('How many people are involved in the game?\n(within 5)> ')
    num = int(nu)

    x =  raw_input('How much do you bet?\n(within 5)> ')
    y = int(x)


    M = num*[y]
    print  M
    print "\n-------------------------------"

    g = raw_input("What number do you bet?\n> ")
    guess = int(g)



L = []
#i = 0
while True:
    
    X = range(0, len(M))
    for l in L:
        X.remove(l)  # deprive the qualification of the persons who did not pay in last round
        
    id = random.sample(X, 1)
    print id[0]
    
        
  
    k = 0

    for n in X:
        if M[n] -1 < 0:    # keep the person who has no money as 0 yuan
            M[n] = 0
            L.append(n)
        else:
            M[n] = M[n] - 1
            k += 1
      
            
    
    if id[0] in L:     # Those who lost there last 1 yuan may has a good luck won in this round, 
        L.remove(id[0])    #  this is their last chance.
    print L
    
    if len(L) == len(M) - 1:     # only leave one winner have money and qualification
        M[id[0]] = M[id[0]] + k 
        print "game over", M     # game over
        print "The winner is: ", id[0] + 1
        if id[0] + 1 == guess:
            print "Congratulation! You won the game."
            print "And you have won: %d yuan." % M[id[0]]
        else:
            print "I'm sorry you lost."
        break;
    else:
        
                
        M[id[0]] = M[id[0]] + k 
    
        print M        
    
    #i += 1
    
    
