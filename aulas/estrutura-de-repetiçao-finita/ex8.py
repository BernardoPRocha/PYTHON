primo = 0
for i in range(2,101,1):       
    for j in range(2, i, 1):
        resto = i % j 
        if resto == 0:
            primo += 1
    if primo == 0:
        print(i)
    primo = 0
    