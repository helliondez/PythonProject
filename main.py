# yourCash = input("How much cash? ")
# yourSaved = input("Percent of what you want to save.")
# toSave = float(yourCash) * float(yourSaved)
# print(f"This is how much to save {toSave}")

# amount = input("Cash, money, hoes! ")
# amount = float(amount)
# print(f"you're taxes are this much ${amount * 0.15} pay up!")

# F = 91.4
# C = (F - 32) * (5/9)
# print(C)

# Ce = 40.3
# Fa = (Ce * 9/5) + 32
# print(Fa)

# temp = weather = input("give the weather: ")
# weather = weather.upper()
# temp = float(temp[:-1])
# if "C" in weather:
#     print(f"The weather in F is {(temp * 9/5) + 32}")
# elif "F" in weather:
#     print(f"The weather in C is {(temp - 32) * (5/9)}")
# else:
#     print("WRONG!")
# while True:
#     temp = weather = input("Enter the weather to convert or type end: ")
#     upWeather = weather.upper()
#     if "C" in upWeather[-1:]:
#         temp = float(temp[:-1])
#         fa = (temp * 9/5) + 32
#         print(f"Your weather in celsius converted to fahrenheit is {fa}F")
#     elif "F" in upWeather[-1:]:
#         temp = float(temp[:-1])
#         ce = (temp - 32) * (5/9)
#         print(f"Your weather in fahrenheit converted to celsius is {ce}C")
#     elif "END" in upWeather:
#         print("ending...")
#         break
#     else:
#         print("invalid")
weatList = []
while True:
    weather = input("Enter the weather to convert or type end to stop: ")
    upWeather = weather.upper()
    for i in upWeather[:-1]:
        if i < "0" or i > "9":
            print("Extra letter found must be all numbers followed by a c or a f")
            upWeather = ""
            break
    if "C" in upWeather[-1:]:
        temp = float(weather[:-1])
        fa = (temp * 9/5) + 32
        print(f"Your weather in celsius converted to fahrenheit is {fa}F")
        weatList.append(fa)
    elif "F" in upWeather[-1:]:
        temp = float(weather[:-1])
        ce = (temp - 32) * (5/9)
        print(f"Your weather in fahrenheit converted to celsius is {ce}C")
        weatList.append(ce)
    elif "LIST" == upWeather:
        for temp in weatList:
            print(temp)
    elif "END" == upWeather:
        print("ending...")
        break