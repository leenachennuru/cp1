from math import *
n = int(raw_input('Please enter the value of n '))
Candidates = range(1,n,2)
PrimeNumbers = [0]*n
i = 2
PrimeNumbers[0] = 2
PrimeNumbers[1] = 3
for TestPrime in Candidates[2:]:
    Dvsr = 2
    while Dvsr <= TestPrime/Dvsr:
        if TestPrime%Dvsr != 0:
            Dvsr = Dvsr + 1
            if Dvsr >= (TestPrime/(Dvsr-1)):
                PrimeNumbers[i] = TestPrime
                i = i + 1
        else:
            Dvsr = TestPrime + 1
        if i == n: break
Log_Sum = 0
for j in PrimeNumbers:
    if j != 0:
        Log_Sum = Log_Sum + log(j)
print 'The logarithmic sum to number ratio is at a distance of', abs(Log_Sum/n - 1) ,"away from 1"
