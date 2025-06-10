def fizzbuzz():
    for i in range(1,101):
        if (i%3!=0 and i%5!=0):
            print(i)
        elif (i%15==0):
            print("FizzBuzz")
        elif (i%3==0):
            print("Fizz")
        else:
            print("Buzz")

if __name__ == '__main__':
    fizzbuzz()