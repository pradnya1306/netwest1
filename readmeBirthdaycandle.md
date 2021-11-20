# ** Birthdaycandle**
# Problem:-
## suppose you are incharge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles,she will only be able to blow out the tallest ones.your task is to find out how many candles she can successfully blow out.for example, if your niece is turing 4 years old, and the cake will have 4 candles of height 4,4,1,3, she will be able to blow out candleds successfully 2 since the tallest candles are of height 4 and there are 2 such candles.

# Function:-
## Here i made birthdayCakeCandles function. this function return us the tallest candles count.

``` 
def birthdayCakeCandles(candles):
    max=0
    for i in range(len(candles)):
        if candles[i]>max:
            max=candles[i]
    count=(candles.count(max))
    return count


size=int(input("enter the size of your list : "))
candles=[]
for i in range(size):
    candle_hieght=int(input("enter your candle hight : "))
    candles.append(candle_hieght)

birthdayCakeCandles(candles)
```
## in this function firstly i asked  input from user for size of list. Then i have run the loop till that size of list and took height of candles from user and then i made list of candles after that i called the function.

```
def birthdayCakeCandles(candles):
    max=0
    for i in range(len(candles)):
        if candles[i]>max:
            max=candles[i]
    count=(candles.count(max))
    return count
```

## There after i took list as parameter and then  i have run the loop on the same list inorder to find maximum height of candles. and then used the count function to find the how many candles has the tallest height.
