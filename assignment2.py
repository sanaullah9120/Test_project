def sum_of(a,b):
    c = a+b
    return c
#calling a function and print result
print(sum_of(7,9))

# list comprehension
list2= [1,2,3,4,5]
new_list2 = [i for i in list2 if i%2==0]
print(new_list2)