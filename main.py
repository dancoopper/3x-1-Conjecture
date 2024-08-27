import matplotlib.pyplot as plt
import numpy as np

number = int(input("number: "))
number2 = int(input("second number: "))
    
    
def plot(number):
    new_number:int = number


    arr = []
    counter = 0
    #########################
    #       Stats           #

    highistNum = 0
    LoopCounter = 0

    #########################
    while True:
        LoopCounter = LoopCounter +1
        if new_number > highistNum:
            highistNum = new_number
        
        arr.append(int(new_number))
        print(new_number)
        if new_number <= 1:
            print("*************")
            counter = counter+1
        
        if counter >= 5:
            #plt.plot(ypoint, linestyle = 'dotted')
            #plt.show()
            print(f'''
                #########################
                #       Stats           #

                HighistNum: {highistNum}
                LoopCounter: {LoopCounter}

                #########################
                ''')
            break

        if new_number %2 == 0:
            new_number: int = new_number/2
        else:
            new_number = (new_number*3)+1

    ypoint = np.array(arr)     
    return ypoint
    

def countNums(array):
    arr = [0,0,0,0,0,0,0,0,0,0]
    for x in array:
        lenth = len(str(x))
        if lenth>1:
            for i in range(lenth):
                var = str(x)[i]
                arr[int(var)-1] += 1
    return arr
                
    
var1 = plot(number)
plt.plot(var1, mouseover = True)
var2 = plot(number2)
#plt.plot(var2, linestyle = 'dotted')
labels = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
#plt.pie(countNums(var2), labels= labels)
plt.show()

