import sqlite3
import time
import hashlib

connection = None
cursor = None

#This is a connection between the database and the python program
def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()
    return


#This is a login option
# check if the username and password are valid to login
# return the user if login successfully
# return 0 if no such user or login failed
def login(username, password):
    global connection, cursor
    
    login_option = input('login as an user? (Yes or No) ')
    if (login_option == 'No'):
        return 0    
    username = input('User: ')
    password = getpass.getpass('Password: ')      
    if re.match("^[A-Za-z0-9_]*$", username) and re.match("^[A-Za-z0-9_]*$", password):
        cursor.execute('SELECT * FROM users WHERE uid=? AND pwd=? ;', (username, password))
        user = cursor.fetchall()
        if(user):
            print('Welcome')
            return user
    print('login falied')
    return 0


def menu_a():
    print('---------------------------------')
    print('1. Register a birth')    
    print('2. Register a marriage')  
    print('3. Renew a vehicle registration')     
    print('4. Process a bill of sale')    
    print('5. Process a payment')  
    print('6. Get a driver abstract') 
    print('7. logout') 
    print('---------------------------------')
    choose = input('Enter your choice: ')
    return choose

def menu_o():
    print('---------------------------------')
    print('1. Issue a ticket')    
    print('2. Find a car owner')  
    print('3. logout') 
    print('---------------------------------')
    choose = input('Enter your choice: ')
    return choose



#This is user use to register a birth
def register_birth(user):
    global connection, cursor
    return 

def renew_vehicle_registration(user):
    global connection, cursor
    return 
 
def process_bill_sale(user):
    global connection, cursor
    return      
 
 
def get_driver_abstract(user):
    global connection, cursor
    
    return        
 
 
def Issue_ticket(user):
    global connection, cursor
    
    return         
 
def find_car_owner(user):
    global connection, cursor
    
    return        


def main():
    global connection, cursor

    path="./prj-test.db"
    connect(path)
    
    user = login()
    while (user ==0):
        user = login()
    while (user['utype']=='a') :
        choose = menu_a()
        if (choose == 1):
            register_birth(user)
        elif (choose == 2):
            register_marriage(user)
        elif (choose == 3):
            renew_vehicle_registration(user)
        elif (choose == 4):
            process_bill_sale(user)
        elif (choose == 5):
            register_marriage(user)        
        elif (choose == 6):
            get_driver_abstract(user)    
        elif (choose == 7):
            break;    
    while (user['utype']=='o') :
        choose = menu_o()
        if (choose == 1):
            Issue_ticket(user)
        elif (choose == 2):
            find_car_owner(user)
        elif (choose == 3):
            break;           
    
    connection.commit()
    connection.close()
    return

if __name__ == "__main__":
    main()
