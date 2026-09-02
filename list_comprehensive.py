list = [1,2,3,4,5]
result= []
print(list)
for i in list:
    if i%2==0:
        result.append(i)
print(result)

#list comprehensive
result = [i for i in list if i%2==0]
print(result)



#a = [1,2,3,4,5]->[1,4,9,16,5]
#condition: list item jodi 2 dara vag hoy tahole oi item er square nibo, na hole oi item ke thik thakbe.

a = [1,2,3,4,5]
result =[]
for i in a:
    if i%2==0:
        result.append(i**2)
    
    else:
        result.append(i)
print(result)         


#list comprehensive 
result = [i**2 if i%2==0 else i for i in a]   
print(result)          