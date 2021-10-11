
def powerSum(X, N, i = 1):
    print(X,N,i)
    val = X -(i**N)
    if val == 0:
        return 1
    elif val < 0:
        return 0
    else:
        return powerSum(val, N, i+1) + powerSum(X, N, i+1)




print(powerSum(10,2))