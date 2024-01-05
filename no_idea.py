if __name__ == "__main__":
    happy = 0
    n, m = map(int, input().strip().split(' '))
    elements_arr = list(map(int, input().strip().split(' ')))
    
    A = set(map(int, input().strip().split(' ')))
    B = set(map(int, input().strip().split(' ')))
    
    for i in elements_arr:
        if i in A:
            happy += 1
        elif i in B:
            happy -= 1
    print(happy)