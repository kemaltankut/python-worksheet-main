# def myAbs(num):
#     if num < 0:
#         return -num
#     else:
#         return num
#         print("ali")

# absValue = myAbs(5)
# print(absValue)



# def equal (a,b,c,d,e):
#     if  a == b or a == c or a == d or a == e or b == c or b==d or b==e or c==d or c==e or d==e:
#         return("your number have at least 2 equal numbers")
        
#     else:
#         return("there is no equal numbers in that numbers")
        


  
# print(equal(1,2,3,4,5))
# print(equal(1,1,3,4,5))
# print(equal(1,1,1,4,5))
# print(equal(1,1,1,1,5))
# print(equal(1,1,1,1,1))




number1 = 5
number2 = 4
total = number1 + number2



notFormattedString = str(number1) + "+" + str(number2) + "=" + str(total)
print(notFormattedString)
formattedString = f"{number1} + {number2} = {total}"
print(formattedString)
secondFormatted = "{} + {} + = {}".format(number1,number2,total)



# Ternary conditionals

a = 10
if a >10:
    print("greater")

elif a>5:
    print("5")

else:
    print("smaller")

print("greater" if a > 10 else "5" if a>5 else "smaller")    





