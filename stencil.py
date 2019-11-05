def laplacian_branch(depth, order, n):
    #returns positive branch
    #[1, 2, ..., order]

    ind = [range(1, order+1)][0]
    if (n == "sym"):
        if (depth == 0):
            return [str(i) for i in ind]
        else:
            return ["N^"+str(depth)] + [str(i) + "N^" + str(depth) for i in ind[1:]]
    else:
        return [i * n**depth for i in ind]

def laplacian(dim, order, n):
    if (dim < 1):
        raise(ValueError('dim must be positive'))
    arr = []
    for d in range(dim):
        arr = arr + laplacian_branch(d, order, n)

    arr_copy = arr.copy()
    arr_copy.reverse()

    if (n == "sym"):
        arr_copy = ["-" + a for a in arr_copy]
        final = arr_copy + ['0'] + arr
    else:
        arr_copy = [-a for a in arr_copy]
        final = arr_copy + [0] + arr
    return(final)


#TODO: Implement version where we alternate between two patterns, one with far read at end,
#one with far read at beginning
def wave(dim, order, n):
    if (dim < 1):
        raise(ValueError('dim must be positive'))
    a = laplacian(dim, order, n)
    if (n == "sym"):
        a = ["-N^"+str(order+1)] + a
    else:
        a = [-(n**(order+1))] + a
    return a

def conv(dim, l, n):
    if (dim < 1):
        raise(ValueError('dim must be positive'))
    a = [0]
    a_last = a.copy()
    for d in range(1,dim):
        a = a + [aa + k**d for k in 
        arr = [ for k in range(n)]
        a_last = a.copy()



if __name__ == "__main__":
    #laplacian(2, 3, "sym")
    #laplacian(2, 3, 10)
    #laplacian(1, 3, "sym")
    #laplacian(1, 3, 10)
    #laplacian(3, 2, "sym")
    #laplacian(3, 2, 10)
    print(wave(3,2,"sym"))
    print(wave(3,2,10))

