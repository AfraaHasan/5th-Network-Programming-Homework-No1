while True:
    try:
        decimal =int(input("enter decimal number: "))
        if decimal ==0:
            print("the equivalent binary number is:",0)
            break

        binary =[]
        while decimal>=1:
            if decimal % 2==0 :
                binary .append('0')
            else :
                binary .append('1')

            decimal = decimal // 2

        binary.reverse()
        str_binary= "".join(binary)
        print("the equivalent binary number is:",str_binary)
        break

    except:
        print("you did not enter an intger number,try again ")
