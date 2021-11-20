
def birthdayCakeCandles(candles):
    max=0
    for i in range(len(candles)): #The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default)
        if candles[i]>max:
            max=candles[i]
    count=(candles.count(max))#The count() method returns the number of elements with the specified value.
    return count


size=int(input("enter the size of your list : "))
candles=[]
for i in range(size):
    candle_hieght=int(input("enter your candle hight : "))
    candles.append(candle_hieght)

birthdayCakeCandles(candles)



