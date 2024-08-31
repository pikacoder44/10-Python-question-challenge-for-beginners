# Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. The function should return a list with only the integers in the original list in the same order.

def just_list(l1=[]):
    final_list =[]
    for i in l1:
        if(type(i)==int):
            final_list.append(i)
        
    return final_list

l1=[1,"Hashir",2,3,7,"pika","Ashar",9]
print(just_list(l1))