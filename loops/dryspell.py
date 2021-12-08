#Show the maximum dry spell (dry spell is a day without rain) - maximum zero rain until next rain

rain = int(input("Rain: "))

count = 0
maximum = 0

while rain != -1:
    if( rain == 0 ):
        count +=1
        if ( maximum < count):
            maximum = count
    else:
        count = 0
    rain = int(input("Rain: "))

print("Max dry days = {}".format(maximum))

