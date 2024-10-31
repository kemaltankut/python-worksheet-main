# how_much = int(input("How much money do you have in your account?: "))

# real_estate = int(input("How many house do you have in kötekli?:"))

# car = input("do you have a car?: ")


# threshold_money = 100000

# threshold_house = 5

# if how_much > threshold_money and real_estate > threshold_house and car == "yes":

#     print("you dont have to work all day long :)")






# elif how_much > 50000 and (car == "yes" or car =="Yes"):
#     print("you have to work 1 day in a week")

# else:
#     print("you have to work all day long :(")    


horsePower = int(input("how much hp does your car have?: "))
if horsePower<60:
    print("your car doesnt costs anything") 


elif 60 < horsePower < 76 :
    print("your car costs 200.000")

elif  75 < horsePower < 91 :
    print("your car costs 350.000")


elif 90<horsePower < 111 :
    print("your car costs 500.000")

elif 110<horsePower < 151 :
    print("your car costs 700.000")            


elif 150<horsePower < 201 :
    print("your car costs 1.200.000")


else:
    print("your car costs 2.000.000")            