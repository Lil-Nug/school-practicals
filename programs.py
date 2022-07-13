# PROGRAM 1
# Write an algorithm to accept item code, item name, quantity sold, price per unit and calculate the cost of sales. Also add 12%
# GST to the price. If the final cost after gst comes out to be above 2000/-, give a 5% discount. After that add an option to
# enter the amount of money paid by costumer and return how less or more the customer has paid from the actual price.

def marks_percentage():
    i_code = input("Enter item code: ")
    i_name = input("Enter item name: ")
    q_sold = int(input("Enter quantity sold: "))
    p_unit = int(input("Enter price per unit: "))

    f_cost = 112/100*(q_sold*p_unit)

    if f_cost > 2000:
        n_cost=95/100*f_cost
    else:
        n_cost=f_cost

    print(f"The customer has to pay {round(n_cost, 2)}")

    c_money = int(input("Enter how much the customer paid:  "))

    if c_money >= n_cost:
        print(f"You have to return {round(c_money-n_cost, 2)}")
    elif c_money<n_cost:
        print(f"Customer has paid {round(n_cost-c_money, 2)} less")


# PROGRAM 2
# Simulate a python program to calculate entry ticket of amusement park. Accept No. of adults, and No, of children. Amount to
# be paid is Rs 150/- per child and Rs 250/- per adult. If the ticket amount is more than 5000 Rs, give a 5% discount. Print 
# the ticket on the screen.

def amusement_ticket():
    print("bhelcum to mai amoosmant paruk")
    n_child = int(input("Enter number of children:  "))
    n_adult = int(input("Enter the number of adults:  "))

    c_child = 150*n_child
    c_adult = 250*n_adult

    f_cost = c_child+c_adult

    disccost = 0

    if f_cost>5000:
        f_cost = 95/100*f_cost
        disccost = 5/100*f_cost

        
    print("\tTICKET")
    print(f"No. of children: {n_child}\nNo. of adults: {n_adult}\nTotal cost: {f_cost}\nDiscount: {disccost}")


# PROGRAM 3
# Accept three numbers and find the greatest number.

def max_3():
    nums = input("Enter three numbers seperated by a comma: ").split(',')
    int_nums = []

    for i in nums:
        int_nums.append(int(i))
    
    result = int_nums[0]

    for i in int_nums:
        if i > result:
            result = i
    
    print(f"The largest number is {result}")


# PROGRAM 4
# Accept 5 numbers and find how many are divisible by just 3, just 5, and by both 3 and 5.

def divisible_3_5():
    list_1 = input("Enter 5 numbers seperated by a comma: ").split(",")
    list_2 = []

    for i in list_1:
        list_2.append(int(i))

    div_3 = 0
    
    for num in list_2:
        if num%3==0:
            div_3+=1
    print(f"{div_3} numbers are divisble by 3")

    div_5 = 0
    
    for num in list_2:
        if num%5==0:
            div_5+=1
    print(f"{div_5} numbers are divisible by 5")

    div_3_5 = 0

    for num in list_2:
        if num%3==0 and num%5==0:
            div_3_5+=1
    print(f"{div_3_5} numbers are divisble by both 3 and 5")


# PROGRAM 5
# Given two variables a and b with integer values, replace the values without using a,b = b,a

def replace():
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    a = a+b
    b = (a-b)
    a = (a-b)
    
    print(a)
    print(b)

amusement_ticket()
