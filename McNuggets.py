Succession = 0
last_store = 0
minm = 0

def readVal(valType, requestMsg, errorMsg):
    while True:
        val = raw_input(requestMsg)
        val = list(val.split(','))
        try:
            val[0] = valType(val[0])
            try:
                val[1] = valType(val[1])
                try:
                    val[2] = valType(val[2])
                except:
                    print(errorMsg)
            except:
                print(errorMsg)
            return val
        except:
            print(errorMsg)
       
val = readVal(int, "Please input the available packs ", "Oops! You made a boo boo. McDonalds sells only full nuggets. (This is code language for enter a integer :P)")
[x,y,z] = val
if (x < y and x < z):
    minm = x
else:
    if (y < x and y < z):
        minm = y
    else:
         minm = z
    
for n in range(1,200):
    solution = False
    if Succession == minm:             #Print out the last stored number once succession reaches 6
        print "The largest number of nuggets that can not be bought in packs of", x,y,z, "is", last_store
        break
    for a in range(0, (n/x) + 1):
        for b in range(0, ((n-x*a)/y)+1):
            if ((n - x*a - y*b)%z) == 0:
                solution = True
                break
        if solution == True:    #Increase Succesion Value if solution is found and break the outer loop.    
            Succession += 1
            break
    else:                       # Reset the succession if no solution has been found
        Succession = 0
        last_store = n

