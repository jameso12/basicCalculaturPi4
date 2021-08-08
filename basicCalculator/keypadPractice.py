from gpiozero import Button
from gpiozero import InputDevice
from gpiozero import OutputDevice
# activate virtual enviroment: source {activate file}
# deactivate    
numPad = [["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]]
[]
# bellow is a boardPinNumber -> GPIO_PinNumber
MappingMToGPIO = {
1: 26,
2: 19,
3: 13,
4: 6,
5: 5,
6: 11,
7: 9,
8: 10
}     

rows, cols = dict(), dict()
# may be wrong, but easy reverse
rowsNum = (4,3,2,1)
colsNum = (8,7,6,5)
for i in range(4):

        r,c = rowsNum[i],colsNum[i]        
        rows[i] = InputDevice(MappingMToGPIO[r], pull_up= True, active_state= None)
        cols[i] = OutputDevice(MappingMToGPIO[c], active_high=False)

try:
        while True:
                for c in range(4): # cols go from low, check input, to high
                        cols[c].on()
                        for r in range(4):
                                if rows[r].value == 1: # if inpuit is low, bottun press
                                        print(numPad[c][r])
                                        while rows[r].value == 1: # verify what happens when this loop is removed
                                                pass
                        cols[c].off()

except:
        pass
"""
def  row1Pressed():
        if cols[0].value == 1:
                print("D")
        elif cols[1].value == 1:
                print("#")
        elif cols[2].value == 1:
                print("0")
        elif cols[3].value == 1:
                print("*")

def  row2Pressed():
        if cols[0].value == 1:
                print("7")
        elif cols[1].value == 1:
                print("8")
        elif cols[2].value == 1:
                print('9')
        elif cols[3].value == 1:
                print('C')
                
def  row3Pressed():
        if cols[0].value == 1:
                print('4')
        elif cols[1].value == 1:
                print('5')
        elif cols[2].value == 1:
                print('6')
        elif cols[3].value == 1:
                print('B')
                
def  row4Pressed():
        if cols[0].value == 1:
                print("1")
        elif cols[1].value == 1:
                print('2')
        elif cols[2].value == 1:
                print('3')
        elif cols[3].value == 1:
                print('A')
                
rows[0].when_activated = row1Pressed
rows[1].when_activated = row2Pressed
rows[2].when_activated = row3Pressed
rows[3].when_activated = row4Pressed

colN = 0
def scanCol(n):
        if n == 1:
                cols[0].on()
                cols[1].off()
                cols[2].off()
                cols[3].off()
        elif n == 2:
                cols[0].off()
                cols[1].on()
                cols[2].off()
                cols[3].off()
        elif n == 3:
                cols[0].off()
                cols[1].off()
                cols[2].on()
                cols[3].off()
        elif n == 4:
                cols[0].off()
                cols[1].off()
                cols[2].off()
                cols[3].on()

colN = 0
try:
        while  True:
                scanCol(colN)
                if colN == 4:
                        colN = 0
except:
        pass
"""