Candidates = range(1,10000,2)
i = 2
for TestPrime in range(1,10000,2):
    Dvsr = 2
    while Dvsr <= (TestPrime/Dvsr):
        if TestPrime%Dvsr != 0:
            Dvsr = Dvsr + 1
            if Dvsr >= (TestPrime/(Dvsr-1)):
                i = i + 1
        else: Dvsr = TestPrime + 1
    if i == 1000:
        print ('The 1000th Prime Number is ', TestPrime)
        break
