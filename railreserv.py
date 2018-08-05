import pickle,os 

class Ticket:
         
    def __init__(self,name=None,age=None,sex=None,seat=None):
        self.name=name
        self.age=age
        self.sex=sex
        self.seat=seat


def bookTicket():
    pickle_in=open('database','ab+')
    pickle_in.seek(0)
    try:
        data=pickle.load(pickle_in)
    except:
        data=[Ticket() for _ in range(10)]
    pickle_in.close()
    for n,d in enumerate(data):
        if d.name==None:
            name=input('Enter your name:\n')
            age=input('Enter your age:\n')
            sex=input('Enter your sex:\n')
            t=Ticket(name,age,sex,n+1)
            print(t.name)
            data[n]=t
            pickle_out=open('database','wb+')
            pickle.dump(data,pickle_out)
            pickle_out.close()
            return True
    return False


def searchTicket():
    try:
        pickle_in=open('database','rb+')
        data=pickle.load(pickle_in)
    except:
        print('No tickets have been booked yet!')
        return False
    pickle_in.close()
    name=input('Enter your name (Should be exactly the same as in the booked ticket):\n')
    age=input('Enter your age:\n ')
    for d in data:
        if d.name==name and d.age==age:
            print('Ticket Found!\n\nName = ',name,'\nAge = ',age,'\nSex = ',d.sex,'\nSeat Number =',d.seat)
            return True    
    print('No ticket found with the entered details')
    return False


def deleteTicket():
    try:
        pickle_in=open('database','ab+')
        pickle_in.seek(0)
        data=pickle.load(pickle_in)
    except:
        print('No tickets have been booked yet!')
        pickle_in.close()
        return False
    pickle_in.close()
    print('\nEnter the details of the ticket to be deleted:\n\n')
    name=input('Enter your name (Should be exactly the same as in the booked ticket):\n')
    age=input('Enter your age:\n ')
    for n,d in enumerate(data):
        if d.name==name and d.age==age:
            print('Ticket Found!\n\nName = ',name,'\nAge = ',age,'\nSex = ',d.sex,'\nSeat Number =',d.seat)
            confirm=input('\nEnter y to confirm deletion of the ticket:\n')
            if confirm.lower()=='y':
                data[n]=Ticket()
            pickle_out=open('database','wb+')
            pickle.dump(data,pickle_out)
            pickle_out.close()
            print('Ticket deleted successfully!')  
            return True  
    print('No ticket found with the entered details!')
    return False

        
def viewTickets():
    try:
        pickle_in=open('database','rb+')
        data=pickle.load(pickle_in)
    except:
        print('No tickets have been booked yet!')
        return False
    pickle_in.close()
    found=False
    for d in data:
        if d.name:
            found=True
            print('\nName = ',d.name,'\nAge = ',d.age,'\nSex = ',d.sex,'\nSeat Number =',d.seat)
    if found==False:
        print('\nNo tickets have been booked yet!\n')
    return True



while True:
    print("Enter any key to go to the main menu.")
    input()
    os.system('cls')
    print('\n\nWelcome to Railway Ticket Reservation System!\n\n1. Book railway ticket\n2. Search ticket\n3. Delete Ticket\n4. View All Tickets\n5. Exit\n')
    i=input()
    if i==1:
        if not bookTicket():
            print('Sorry! No seats are available.')
        
    elif i=='2':
        searchTicket()
    elif i=='3':
        deleteTicket()
    elif i=='4':
        viewTickets()
    else:
        break
    

