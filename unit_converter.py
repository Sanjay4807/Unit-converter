#Length Converter
def length():
    def mm(num,op):
    
        if op ==1 : #mm to mm 
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op == 2: #mm to cm 
            print('\n',num,'millimetres =')
            print('\n',num/10,'cm')
            print("\n****************END****************")
        elif op ==3: #mm to mt
            print('\n',num,'millimetres =')
            print('\n',num/1000,'metres')
            print("\n****************END****************")
        elif op == 4: #mm to km
            print('\n',num,'millimetres =')
            print('\n',num/1000000,'km')
            print("\n****************END****************")
    
    def cm(num,op):

        if op ==1 : #cm to mm 
            print("\n",num,'centimetres =')
            print('\n',num*10,'millimetres')
            print("\n****************END****************")
        elif op == 2: #cm to cm 
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op ==3: #cm to mt
            print('\n',num,'centimetres =')
            print('\n',num/100,'metres')
            print("\n****************END****************")
        elif op == 4: #cm to km
            print('\n',num,'centimetres =')
            print('\n',num/100000,'km')
            print("\n****************END****************")
    
    def mt(num,op):

        if op ==1 : #mt to mm 
            print("\n",num,'metres =')
            print('\n',num*1000,'millimetres')
            print("\n****************END****************")
        elif op == 2: #mt to cm
            print("\n",num,'metres =')
            print('\n',num*100,'centimetres')
            print("\n****************END****************")
        
        elif op ==3: #mt to mt
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op == 4: #mt to km
            print('\n',num,'metres =')
            print('\n',num/1000,'km')
            print("\n****************END****************")

    def km(num,op):

        if op ==1 : #km to mm 
            print("\n",num,'kilometres =')
            print('\n',num*1000000,'millimetres')
            print("\n****************END****************")
        elif op == 2: #km to cm
            print("\n",num,'kilometres =')
            print('\n',num*100000,'centimetres')
            print("\n****************END****************")
        
        elif op ==3: #km to mt
            print("\n",num,'kilometres =')
            print('\n',num*1000,'metres')
            print("\n****************END****************")
        
        elif op == 4: #km to km
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")

    while True:
        print("\n\n\t\tLength Converter\n1.Millimeter\n2.Centimeter\n3.Meter\n4.Kilometer\n5.Go Back")
        fromunit=int(input("\nEnter the unit (1-4) or Enter 5 to Go back to main menu:"))
        if fromunit == 5:
            print("\nExiting Length Converter")
            break
        else:
            ch=[1,2,3,4]
            if fromunit not in ch :
                print('\nInvalid Choice,Please try again')
                continue
            else:
                fromval=float(input("Enter the value:"))
                tounit=int(input("Enter the unit (1-4) to be converted:"))
                if fromunit== 1:
                    mm(fromval,tounit)
                elif fromunit== 2:
                    cm(fromval,tounit)
                elif fromunit== 3:
                    mt(fromval,tounit)
                elif fromunit== 4:
                    km(fromval,tounit)

#Mass Converter            
def mass():
    def mg(num,op):
    
        if op ==1 : #mg to mg 
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op ==2: #mg to gram
            print('\n',num,'milligram =')
            print('\n',num/1000,'grams')
            print("\n****************END****************")
        elif op == 3: #mg to kg
            print('\n',num,'milligram =')
            print('\n',num/1000000,'kilogram')
            print("\n****************END****************")
        elif op == 4: #mg to ton
            print('\n',num,'milligrams =')
            print('\n',num/1000000000,'tonne')
            print("\n****************END****************")
            
    
    def gm(num,op):

        if op ==1 : #gm to mg 
            print("\n",num,'grams =')
            print('\n',num*1000,'milligram')
            print("\n****************END****************")
        elif op ==2: #gm to gm
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op == 3: #gm to kg
            print('\n',num,'grams =')
            print('\n',num/1000,'kilogram')
            print("\n****************END****************")
        elif op == 4: #gm to ton
            print('\n',num,'grams =')
            print('\n',num/1000000,'tonne')
            print("\n****************END****************")
            

    def kg(num,op):

        if op ==1 : #kg to mg 
            print("\n",num,'kilograms =')
            print('\n',num*1000000,'milligrams')
            print("\n****************END****************")
        elif op ==2: #kg to gm
            print("\n",num,'kilograms =')
            print('\n',num*1000,'gram')
            print("\n****************END****************")
        elif op == 3: #kg to kg
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op == 4: #kg to ton
            print("\n",num,'kilograms =')
            print('\n',num/1000,'tonne')
            print("\n****************END****************")
            

    def ton(num,op):
        if op == 1: #ton to mg
            print('\n',num,'tonne =')
            print('\n',num*1000000000,'milligrams')
            print("\n****************END****************")
        elif op == 2: #ton to gm
            print('\n',num,'tonne =')
            print('\n',num*1000000,'grams')
            print("\n****************END****************")
        elif op == 3: #ton to kg
            print('\n',num,'tonne =')
            print('\n',num*1000,'kilograms')
            print("\n****************END****************")
        elif op ==4: #ton to ton
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        
    while True:
        print("\n\n\t\tMass Converter\n1.Milligram\n2.Gram\n3.Kilogram\n4.Tonne\n5.Go Back")
        fromunit=float(input("\nEnter the unit (1-4) or Enter 5 to Go back to main menu:"))
        if fromunit == 5:
            print("\nExiting Mass converter")
            break
        else:
            ch=[1,2,3,4]
            if fromunit not in ch:
                print("\nInvalid Choice,Please try again")
                continue
            fromval=int(input("Enter the value:"))
            tounit=int(input("Enter the unit (1-4) to be converted:"))
            if fromunit== 1:
                mg(fromval,tounit)
            elif fromunit== 2:
                gm(fromval,tounit)
            elif fromunit== 3:
                kg(fromval,tounit)
            elif fromunit== 4:
                ton(fromval,tounit)
            else:
                print('\nInvalid Choice,Please try again')

#Time Converter
def time():
    def sec(num,op):
            if op == 1: #sec to sec
                print("\nSame Unit, Enter another unit and try again")
                print("\n****************END****************")
            elif op == 2: #sec to min
                print('\n',num,'seconds =')
                print('\n',num/60,'minutes')
                print("\n****************END****************")
            elif op == 3: #sec to hr
                print('\n',num,'seconds =')
                print('\n',num/3600,'hours')
                print("\n****************END****************")

    def minu(num,op):
        if op == 1: #min to sec
            print('\n',num,'minutes =')
            print('\n',num*60,'seconds')
            print("\n****************END****************")
        elif op == 2: #min to min
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op == 3: #min to hr
            print('\n',num,'minutes =')
            print('\n',num/60,'hours')
            print("\n****************END****************")
    def hr(num,op):
        if op == 1: #hr to sec
            print('\n',num,'hours =')
            print('\n',num*3600,'seconds')
            print("\n****************END****************")
        elif op == 2: #hr to min
            print('\n',num,'hours =')
            print('\n',num*60,'minutes')
            print("\n****************END****************")
        elif op == 3: #hr to hr
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
    while True:
        print("\n\n\t\tTime Converter\n1.Second\n2.Minute\n3.Hour\n4.Go Back")
        fromunit=int(input("\nEnter the unit (1-3) or Enter 4 to Go back to main menu:"))
        if fromunit == 4:
            print("\nExiting Time converter")
            break
        else:
            ch=[1,2,3]
            if fromunit not in ch:
                print("\nInvalid Choice,Please try again")
                continue
            fromval=float(input("Enter the value:"))
            tounit=int(input("Enter the unit (1-3) to be converted:"))
            if fromunit== 1:
                sec(fromval,tounit)
            elif fromunit== 2:
                minu(fromval,tounit)
            elif fromunit== 3:
                hr(fromval,tounit)
            else:
                print('\nInvalid Choice,Please try again')

#Temperature Converter
def temp():

    def cels(num,op):
        if op == 1: #cels to cels
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op == 2: #cels to fahr
            print('\n',num,'celsius =')
            print('\n',(num*9/5)+32,'fahrenheit')
            print("\n****************END****************")
        elif op == 3: #cels to kelvin
            print('\n',num,'celsius =')
            print('\n',num+273.15,'kelvin')
            print("\n****************END****************")
    def fahr(num,op):
        if op == 1: #fahr to cels
            print("\n",num,'fahrenheit =')
            print('\n',(num-32)*5/9,'celsius')
            print("\n****************END****************")
        elif op == 2: #fahr to fahr
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op == 3: #fahr to kelvin
            print('\n',num,'fahrenheit =')
            print('\n',(num-32)*5/9+273.15,'kelvin')
            print("\n****************END****************")
    def kelv(num,op):
        if op == 1: #kelv to cels
            print('\n',num,'kelvin =')
            print('\n',num-273.15,'celsius')
            print("\n****************END****************")
        elif op == 2: #kelv to fahr
            print('\n',num,'kelvin =')
            print('\n',(num-273.15)*9/5+32,'fahrenheit')
            print("\n****************END****************")
            
    while True:
        print("\n\n\t\tTemperature Converter\n1.Celsius\n2.Fahrenheit\n3.Kelvin\n4.Go Back")
        fromunit=int(input("\nEnter the unit (1-3) or Enter 4 to Go back to main menu:"))
        if fromunit == 4:
            print("\nExiting Temperature converter")
            break
        else:
            ch=[1,2,3]
            if fromunit not in ch:
                print("\nInvalid Choice,Please try again")
                continue
            fromval=float(input("Enter the value:"))
            tounit=int(input("Enter the unit (1-3) to be converted:"))
            if fromunit==1:
                cels(fromval,tounit)
            elif fromunit==2:
                fahr(fromval,tounit)
            elif fromunit==3:
                kelv(fromval,tounit)
            else:
                print('\nInvalid Choice,Please try again')

#Energy Converter
def energy():

    def joule(num,op):
        if op == 1: #joule to joule
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op ==2: #joule to calorie
            print('\n',num,'joule =')
            print('\n',num/4.184,'calorie')
            print("\n****************END****************")
        elif op == 3:#joule to watt hour
            print('\n',num,'joule =')
            print('\n',num/3600,'watt-hour')
            print("\n****************END****************")

    def cal(num,op):
        if op == 1: #calorie to joule
            print('\n',num,'calorie =')
            print('\n',num*4.184,'joule')
            print("\n****************END****************")
            
        elif op ==2: #calorie to calorie
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op == 3:#calorie to watt hour
            print('\n',num,'calorie =')
            print('\n',num/860.4,'watt-hour')
            print("\n****************END****************")

    def watt(num,op):
        if op == 1: #watthour to joule
            print('\n',num,'watt-hour =')
            print('\n',num*3600,'joule')
            print("\n****************END****************")
            
        elif op ==2: #watt-hour to calorie
            print('\n',num,'watt-hour =')
            print('\n',num*860.4,'calorie')
            print("\n****************END****************")
            
        elif op == 3:#watt hour to watt hour
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        
    while True:
        print("\n\n\t\tEnergy Converter\n1.Joule\n2.Calorie\n3.Watt-Hour\n4.Go Back")
        fromunit=int(input("\nEnter the unit (1-3) or Enter 4 to Go back to main menu:"))
        if fromunit == 4:
            print("\nExiting Energy converter")
            break
        else:
            ch=[1,2,3]
            if fromunit not in ch:
                print("\nInvalid Choice,Please try again")
                continue
            fromval=float(input("Enter the value:"))
            tounit=int(input("Enter the unit (1-3) to be converted:"))
            if fromunit==1:
                joule(fromval,tounit)
            elif fromunit==2:
                cal(fromval,tounit)
            elif fromunit==3:
                watt(fromval,tounit)
            else:
                print('\nInvalid Choice,Please try again')

#Pressure Converter
def pressure():

    def bar(num,op):
        if op == 1: #bar to bar
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op ==2: #bar to pascal
            print('\n',num,'bar =')
            print('\n',num*100000,'pascal')
            print("\n****************END****************")
        elif op == 3:#bar to torr
            print('\n',num,'bar =')
            print('\n',num*750.1,'torr')
            print("\n****************END****************")

    def pascal(num,op):
        if op == 1: #pascal to bar
            print('\n',num,'pascal =')
            print('\n',num/100000,'bar')
            print("\n****************END****************")
            
        elif op ==2: #pascal to pascal
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
        elif op == 3:#pascal to torr
            print('\n',num,'pascal =')
            print('\n',num/133.3,'torr')
            print("\n****************END****************")

    def torr(num,op):
        if op == 1: #torr to bar
            print('\n',num,'torr =')
            print('\n',num/750.1,'bar')
            print("\n****************END****************")
            
        elif op ==2: #torr to pascal
            print('\n',num,'torr =')
            print('\n',num*133.3,'pascal')
            print("\n****************END****************")
            
        elif op == 3:#torr to torr
            print("\nSame Unit, Enter another unit and try again")
            print("\n****************END****************")
    
    while True:
        print("\n\n\t\tPressure Converter\n1.Bar\n2.Pascal\n3.Torr\n4.Go Back")
        fromunit=int(input("\nEnter the unit (1-3) or Enter 4 to Go back to main menu:"))
        if fromunit == 4:
            print("\nExiting Pressure Converter")
            break
        else:
            ch=[1,2,3]
            if fromunit not in ch:
                print("\nInvalid Choice,Please try again")
                continue
            fromval=float(input("Enter the value:"))
            tounit=int(input("Enter the unit (1-3) to be converted:"))
            if fromunit==1:
                bar(fromval,tounit)
            elif fromunit==2:
                pascal(fromval,tounit)
            elif fromunit==3:
                torr(fromval,tounit)
            else:
                print('\nInvalid Choice,Please try again')
                
        
    
                
#Main Menu 
while True:

    print('\n\t\t Unit Converter')
    print('\n\t\t Main Menu')
    print('\n1.Length\n2.Mass\n3.Time\n4.Temperature\n5.Energy\n6.Pressure\n7.Exit')
    
    try:
        ch=int(input('\nEnter the choice:'))
        if ch == 7:
            print("Exiting Unit Converter, Thank you for using")
            break
        elif ch == 1:
            length()
        elif ch == 2:
            mass()
        elif ch == 3:
            time()
        elif ch == 4:
            temp()
        elif ch == 5:
            energy()
        elif ch == 6:
            pressure()
        else:
            print('\nInvalid Choice,Please try again')
    except ValueError:
        print("Enter a valid input,Please enter a valid number")
