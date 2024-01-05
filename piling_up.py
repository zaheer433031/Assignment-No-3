t = int(input())

for _ in range(t):
    num, cubes = int(input()), list(map(int,input().split()))
    answer = "Yes"
    
    while len(cubes) > 1:
        if cubes[0] >= cubes[-1]:
            large = cubes[0]
            cubes.pop(0)
        else:
            large = cubes[-1]
            cubes.pop(-1)  
        if large < cubes[0] or large < cubes[-1]:
            answer = 'No'
            break
            
    print(answer)