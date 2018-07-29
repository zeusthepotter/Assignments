import pickle,os 


class Ticket:
    name=''
    age=int()
    seat=int()
    sex=''
      
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
            # for i in data:
            #     print(i.name)
            pickle_out=open('database','wb+')
            pickle.dump(data,pickle_out)
            pickle_out.close()
            return True
    return False


def searchTicket():
    pickle_in=open('database','rb+')
    try:
        data=pickle.load(pickle_in)
    except:
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
    pickle_in=open('database','ab+')
    pickle_in.seek(0)
    try:
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
    print('No ticket found with the entered details')
    return False



        

while True:
    # os.system('cls')
    print('Welcome to Railway Ticket Reservation System!\n\n1. Book railway ticket\n2. Search ticket\n3. Delete Ticket\n4. Exit')
    i=int(input())
    if i==1:
        if not bookTicket():
            print('Sorry! No seats are available.')
        
    elif i==2:
        searchTicket()
    elif i==3:
        deleteTicket()
    elif i==4:
        break
    


# example_dict = {1:"6",2:"2",3:"f"}
 
# pickle_out = open("dict.pickle","wb")
# pickle.dump(example_dict, pickle_out)
# pickle_out.close()
# pickle_in = open("dict.pickle","rb")
# example_dict = pickle.load(pickle_in)
# print(example_dict)
# print(example_dict[3])