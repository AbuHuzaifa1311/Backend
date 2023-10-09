num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
 #question 1
for num in num_list:
    print(num)
 #question 2
for num in num_list:
     if(num > 45):
        print(num)
 #question 3
for num in num_list:
    if(num > 45):
        print("over 45:",num)
    else:
        print("under 45:",num)
    #question 4
    for index,num in enumerate(num_list):
        if(num ==36):
            print("number found at pos",index)
    #question 5,6,7,8
    for index, num in enumerate(num_list):
        if(num ==36):
            count += 1
            print("number found at pos",index)
            break
        print("totl value of count=" ,count)


# i am checing the commit



 
