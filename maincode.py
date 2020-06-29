
import sendemail
import relay
import gps
import alcohol
A = 3.4 #currently pre defined , we'll put the gps function for repository
B = 5.7 #currently pre defined , we'll put the gps function for repository
i = 0
while True :
    val = alcohol.alcoholval()
    i = 0
        
        

    if val == 1 :
        i= i +1
        if i <= 0 :
            
            sendemail.sendemail(A,B)
        relay.fuel_stop()
    else:
        
        relay.fuel_flow()
        
    


         
