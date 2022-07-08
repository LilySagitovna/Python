ferstFrendSpeed = 4
secondFrendSpeed = 5
distance = 1000
dogSpeed = 10
minDistance = 10
friend = 2
dogCounter = 0

while distance > minDistance:
    if friend == 1: # собака бежит ко второму другу
        time = distance/(ferstFrendSpeed + dogSpeed)
        friend = 2
    else:
        time = distance/(secondFrendSpeed + dogSpeed)
        friend = 1 
    distance = distance - (ferstFrendSpeed + secondFrendSpeed)* time
    dogCounter = dogCounter + 1
print(dogCounter, "раз пробежит собака от одного друга до другого")
