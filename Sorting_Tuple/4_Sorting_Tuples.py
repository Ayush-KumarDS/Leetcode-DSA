def sorting (techs):
    n = len(techs)
    l1 = list(techs)
    
    for i in range(n):
        j = i+1
        while j < n:
            if l1[i] > l1[j]:
                l1[i], l1[j] = l1[j], l1[i]
            j += 1
    return tuple(l1)

techs = ('python','aws', 'java', 'sql', 'nodejs', 'pandas')

print(sorting(techs))