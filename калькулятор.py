# norm kalkulator
kalrulator=input("выберите действие (+,-,*,/): " )
a=float(input("введите 1 число : "))
b=float(input("введите 2 число : "))

if kalrulator == "+":
    f=a+b
    print("произведение ваших чисел : "+ str(f))

elif kalrulator == "-":
    c=a-b
    print("разность  ваших чисел :"+ str(c))    

elif kalrulator == "*":
    c=a*b
    print("сумма ваших чисел :"+ str(c))  

elif kalrulator == "/":
    c=a/b
    print( "частное  ваших чисел :"+ str(c))

else :
    print("выбрано неверное действие")
