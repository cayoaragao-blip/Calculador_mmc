# Função para descobrir o MDC (maior divisor comum)
def mdc(n1, n2):
    while n1%n2 != 0:
        n1, n2 = n2, n1%n2
    return n2


# Função para descobrir o MMC de dois ou mais números 
def mmc(*args):
    mmc = args[0]
    for i in range(len(args)):
        mmc = mmc*args[i]//mdc(mmc, args[i])
    return mmc



# Ex: print(mmc(42, 74, 88, 92)) - O menor múltiplo comum deste conjunto é 1.572.648