# Fibbonacci Sequence - pracicepython.org

fibSeq = []
def fib():
    fibLen = int(input("How long should the sequence be?"))
    if fibLen == 0:
        fibSeq = []
    elif fibLen == 1:
        fibSeq = [0]
    elif fibLen == 2:
        fibSeq = [0, 1]
    else:
        i = 1
        fibSeq = [0,1] 
        while i < (fibLen-1):
            fibSeq.append(fibSeq[i] + fibSeq[i-1])
            i+=1
    print(fibSeq)

fib()   