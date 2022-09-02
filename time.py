import time
currentTime = int(time.strftime('%H'))   

if currentTime < 12 :
     print('Good morning')
elif currentTime == 12  :
     print('Good afternoon')
elif currentTime > 6 :
     print('Good evening')
