# check logic to display customer order


numCP = 0
numPP = 0
numHP = 0
numMP = 0




order = [numCP,numPP,numHP,numMP]
newOrder = []

for i in range(len(order)):
    num = int(input('Enter num of pizzas: '))
    order[i] = num  
    
for i in range(len(order)):
    if order[i] != 0:
        newOrder.append(order[i])

for i in range(len(newOrder)):
    print(newOrder[i])
    
    
    # if number > 0 add to frame