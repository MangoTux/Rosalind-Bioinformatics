def fibd(n,m):
    pop = [1] + [0]*(m-1)
    for i in range(n-1):
        pop = [sum(pop[1:])] + pop[:-1]
    return sum(pop)

if __name__ == "__main__":
    n,m = 97, 16
    print fibd(n,m)