'''
import time 
from openKiosk import CustomerTransaction2


# if timer == 600 openKiosk()

def startTime():
    my_time =   5    #600 (10 min)

    for x in range(0,my_time):
        time1 = x
        time.sleep(1)
        print(time1)

    print('Done')
    CustomerTransaction2()


#startTime()
'''