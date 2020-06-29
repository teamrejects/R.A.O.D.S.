
import smtplib
def sendemail(A,B):
    i = 1
    j = 1
    email = []
    x = []
    y = []
    total = [] 
    n = len(email)
    with open("email&co-ordinate.txt", mode='r') as contacts_file:
            for a_contact in contacts_file:
                e=a_contact.split()[0]
                a=float(a_contact.split()[1])
                b=float(a_contact.split()[2])
                x.append((A-a)**2)
                y.append((B-b)**2)
                email.append(e)
    n = len(email)
    for j in range(n):
        total.append(x[j] + y[j])
    for i in range(n):
        for j in range(n-i-1):
            if total[j]>total[j+1]:
                total[j],total[j+1]=total[j+1],total[j]
                email[j],email[j+1]=email[j+1],email[j]              
    rec = email[0]
    
    gmailaddress = "therejects2020@gmail.com"
    gmailpassword = "therejectskar1324"
    mailto = "therejects2020@gmail.com"
    msg = "ALCOHOL VAPOURS above legal drinking limit \n have been detected in this vehicle \n Vehicle Number XX123XX \n Driver Name  John \n Vehicle Coordinates  X1,Y1 "
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, mailto , msg)
    print(" \n Sent!")
    mailServer.quit()

print(sendemail(7,8))