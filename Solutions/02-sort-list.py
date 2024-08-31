def sortlist():
    List = []
    range1 = int(input("Enter number of elements for list = "))
    print("Enter the numbers for List-")
    for i in range(range1):
        user = int(input("Enter number: "))
        List.append(user)
        
    print("Now you want to order the List in ascending or descending order?")
    print("reply by asc or desc")

    sort = input("-> ")
    
    if(sort=="asc"):
        List.sort()
        print(List)
    elif(sort == "desc"):
        List.sort(reverse=True)
        print(List)
    else:
        print("Invalid response...")
        print("Break........")
        
        

sortlist()



