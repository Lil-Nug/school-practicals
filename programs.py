# PROGRAM 1
# Write an algorithm to accept item code, item name, quantity sold, price per unit and calculate the cost of sales. Also add 12%
# GST to the price. If the final cost after gst comes out to be above 2000/-, give a 5% discount. After that add an option to
# enter the amount of money paid by costumer and return how less or more the costumer has paid from the actual price.

def total_cost():
    i_code = input("Enter item code: ")
    i_name = input("Enter item name: ")
    q_sold = int(input("Enter quantity sold: "))
    p_unit = int(input("Enter price per unit: "))

    f_cost = 112/100*(q_sold*p_unit)

    if f_cost > 2000:
        n_cost = 95/100*f_cost
    else:
        n_cost = f_cost

    print(f"The customer has to pay {round(n_cost, 2)}")

    c_money = int(input("Enter how much the customer paid:  "))

    if c_money >= n_cost:
        print(f"You have to return {round(c_money-n_cost, 2)}")
    elif c_money < n_cost:
        print(f"Customer has paid {round(n_cost-c_money, 2)} less")


# PROGRAM 2
# Simulate a python program to calculate entry ticket of amusement park. Accept No. of adults, and No, of children. Amount to
# be paid is Rs 150/- per child and Rs 250/- per adult. If the ticket amount is more than 5000 Rs, give a 5% discount. Print
# the ticket on the screen.

def amusement_ticket():
    print("Welcome to my amusement park!")
    n_child = int(input("Enter number of children:  "))
    n_adult = int(input("Enter the number of adults:  "))

    c_child = 150*n_child
    c_adult = 250*n_adult

    f_cost = c_child+c_adult

    disccost = 0

    if f_cost > 5000:
        f_cost = 95/100*f_cost
        disccost = 5/100*f_cost

    print("\tTICKET")
    print(
        f"No. of children: {n_child}\nNo. of adults: {n_adult}\nTotal cost: {f_cost}\nDiscount: {disccost}")


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
        if num % 3 == 0:
            div_3 += 1
    print(f"{div_3} numbers are divisble by 3")

    div_5 = 0

    for num in list_2:
        if num % 5 == 0:
            div_5 += 1
    print(f"{div_5} numbers are divisible by 5")

    div_3_5 = 0

    for num in list_2:
        if num % 3 == 0 and num % 5 == 0:
            div_3_5 += 1
    print(f"{div_3_5} numbers are divisble by both 3 and 5")


# PROGRAM 5
# Accept two numbers from user and swap their values (without using any other variable or Python built in components)

def replace():
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    print(f"Before swapping-\nNum 1: {a}\nNum 2: {b}")
    a = a+b
    b = (a-b)
    a = (a-b)

    print(f"After swapping-\nNum 1: {a}\nNum 2: {b}")


# PROGRAM 6
# Accept sales done by a sales man in four quarters. Find Total Sales done and calculate commission on the basis
# of following criteria:
# >=250000 --> 7% of total sales
# 100000-250000 --> 5% of total sales
# 50000-100000 --> 2% of total sales
# <50000 --> no commission

def sales():
    sales = input(
        "Enter sales for each quarter seperated by a comma: ").split(',')
    sales = [int(i) for i in sales]
    total = 0

    for i in sales:
        total += i

    print(f"Your total sales for this year are {total}")
    commission = 0

    if total >= 250000:
        commission = 0.07*total

    elif total >= 100000:
        commission = 0.05*total

    elif total >= 50000:
        commission = 0.02*total

    else:
        commission = 0

    print(f"Your annual commission is {commission}")


# PROGRAM 7
# Accept marks scored by a student in 5 subjects. Calculate percentage score and find the grade on the basis of
# the following criteria:-
# >= 95 --> A
# 90-95 --> A-
# 80-90 --> B
# 70-80 --> C
# 60-70 --> D
# <60 --> F

def marks_grade():

    marks = input(
        "Enter your marks for 5 subjects each seperated by a comma: ").split(',')

    marks = [int(i) for i in marks]

    total = 0

    for i in marks:
        total += i

    percentage = total/5

    print(f'You have a total percentage of {percentage}')

    grade = ''

    if percentage >= 95:
        grade = 'A'
    elif percentage >= 90:
        grade = 'A-'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f'Your grade is {grade}')


# PROGRAM 8
# Simulate a mobile billing application. accept the consumer's name and mobile number. Also accept the number
# of local calls, units of data usage(accept in bytes, then convert to gb later), number of sms, number of
# std calls. Calculate bill amount, on the basis of following criteria:-
# - local calls --> 1.5 rs/call
# if no of local calls > 500, then excess calls will be charged at 2 rs/call
# if no. of sms are <50, then no charge. for all sms above 50 charge 0.5 rs/msg
# all std calls --> 3.5 rs
# data - 30 rs/GB
# calculate bill amount, give a surcharge at the rate of 5% on bill amount. Accept mode of payment from the user.
#  If it is cash, then accept cash given by the customer, and calculate the amount to give back to the customer.
#  If payment option is paytm, calculate 2% cashback on bill amount payable. If the payment option is a visa card
# give 5% cashback.

def mobile_bill():
    name = input("Enter your name: ")
    mob_num = input("Enter your mobile number: ")
    n_local_calls = int(input("Enter the number of local calls you've made: "))
    n_data_usage = int(input("Enter your data usage in bytes: "))
    n_sms = int(input("Enter number of sms you've sent: "))
    n_std_calls = int(input("Enter number of std calls you've made: "))

    local_calls_bill = 0
    if n_local_calls <= 500:
        local_calls_bill = 1.5*n_local_calls
    else:
        local_calls_bill = (1.5*500) + ((n_local_calls-500)*2)

    data_usage_gb = n_data_usage/1000000000
    data_usage_bill = (data_usage_gb)*30

    sms_bill = 0
    if n_sms >= 50:
        sms_bill = (n_sms-50)*0.5

    std_calls_bill = 3.5*n_std_calls

    total_bill = local_calls_bill + data_usage_bill + sms_bill + std_calls_bill

    surch_bill = total_bill*105/100

    print(f"The costumer has to pay {surch_bill}")
    payment = (
        input("Enter your mode of payment ('cash'|'paytm'|'visa'): "))

    to_return = 0

    if payment.lower() == 'cash':
        cust_pay = int(input("Enter how much cash the costumer paid: "))
        if cust_pay >= surch_bill:
            print(
                f"You have to return Rs. {cust_pay-surch_bill} to the costumer.")
        else:
            print(f"The costumer has paid Rs. {surch_bill-cust_pay} less.")

    elif payment.lower() == 'paytm':
        to_return = 0.02*surch_bill
        print(f"You have to give a cashback of {to_return}")

    elif payment.lower() == 'visa':
        to_return = 0.05*surch_bill
        print(f"You have to give a cashback of {to_return}")

    else:
        print("That payment method is unacceptable.")
        return False

    when_print = input("Press enter to print bill")

    print(
        f"\tFULL MOBILE BILL\n- Name: {name}\n- Mobile number: {mob_num}\n-"
        f" No. of local calls: {n_local_calls}\n- Local calls charge: Rs. {local_calls_bill}\n-"
        f" Data usage: {data_usage_gb} GBs\n- Data usage charge: Rs. {data_usage_bill}\n- SMS sent: {n_sms}\n-"
        f" SMS charge: Rs. {sms_bill}\n- std calls made: {n_std_calls}\n- std calls charge: Rs."
        f" {std_calls_bill}\n- Total bill before surcharge: Rs. {total_bill}\n- Total bill after surcharge: Rs. "
        f" {surch_bill}\n- Amount of surcharge: Rs. {5/100*total_bill}(5%)"
        f"\n- Payment method: {payment.lower()}")

<<<<<<< HEAD

# PROGRAM 9
# Accept 20 numbers and find the average of even and odd numbers entered
def even_odd_avg():
    nums = []
    for i in range(20):
        num = int(input(f"Enter number {i+1}: "))
        nums.append(num)

    even = []
    odd = []

    for i in nums:
        if i % 2 == 0:
            even.append(i)
        elif i % 2 == 1:
            odd.append(i)

    even_total = 0
    odd_total = 0

    for i in even:
        even_total += i

    for i in odd:
        odd_total += i

    if len(even) == 0:
        even_avg = 0
    else:
        even_avg = even_total/(len(even))

    if len(odd) == 0:
        odd_avg = 0
    else:
        odd_avg = odd_total/(len(odd))

    print(f"""Average of all even numbers is {even_avg}
Average of all odd numbers is {odd_avg}""")


# PROGRAM 10
# Accept 10 numbers and find out the cube of the numbers entered

def cube_10():
    result = []
    for i in range(10):
        num = int(input(f"Enter number {i+1}: "))
        result.append(num**3)

    x = 1
    for i in result:
        print(f"cube of number {x} is {i}")
        x += 1
=======
>>>>>>> f986415588ee2f4accab095c90e57c4804aaf252
