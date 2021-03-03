class Avaliable_seats():
    def __init__(self):
        self.x = int(input('Enter the number of rows:\n'))
        self.y = int(input('Enter the number of seats in each rows:\n'))
        self.ar_seats =[]
    
    def seats(self):
        alpha = 'A'
        for i in range(0,self.x+1):
            seat_list = []
            if i == 0:
                for i in range(0,self.y+1):
                    if i == 0:
                        seat_list.append(' ')
                    else:
                        seat_list.append(str(i))
            else:   
                for i in range(0,self.y+1):
                    if i == 0:
                        seat_list.append(alpha)
                        alpha = chr(ord(alpha)+1)
                    else:
                        seat_list.append("\033[1;32m"+"S"+'\033[m')
            self.ar_seats.append(seat_list)
        return self.ar_seats   


class Booking(Avaliable_seats):
    def __init__(self):
        self.booking_info = [["Seat No",'Name','Gender','Age','Ticket price','Phone No.',"F&B"]]
        super().__init__()
        self.seats_list = []
        self.net_income = []
        self.fnb = []
        self.arranged_seats = self.seats()
        self.capacity = self.x*self.y
        
    def info_taking(self):
        while True:
            while True:
                self.seat_num = input('Enter the seat no. you want to reserve: (for eg A1, B3, D15 or E9)\n')
                try:
                    self.arranged_seats[ord(self.seat_num[0])-(ord("A")-1)][int(self.seat_num[1:])] == "\033[1;32mS\033[m"
                    break
                except:
                    print("\n** Please insert vaild seat!! **\n")
            if self.seat_num in self.seats_list:
                print("Please select another seat as this seat is already booked/reserved by another person")
            
            else:
                def price_fixer():
                    a = ord(self.seat_num[0])- (ord("A")-1)
                    ticket_Price = None
                    if self.x*self.y<=60:
                        ticket_Price = 10
                    else:
                        if self.x%2 ==1:
                            if  a <= self.x//2:
                                ticket_Price = 10
                            else:
                                ticket_Price = 8
                        else:
                            if a <= self.x/2:
                                ticket_Price = 10
                            else:
                                ticket_Price = 8
                    return ticket_Price
                user_details = []
                print("Ticket price for your seat is $", price_fixer())
                Name = input("Enter your name:\n")
                Gender = input("Enter your Gender: (Male/Female/Other)\n")
                Age = input("Enter your Age:\n")
                Ticket_price = price_fixer()
                Phone_No = input("Enter you Phone No:\n")
                while True:
                    ans = input("Would you like to add Popcorn and Coke Combo for extra $5? y/n \n")
                    if ans == "y" or ans =='Y':
                        Popcorn = 5
                        break
                    elif ans == 'n' or ans =="N":
                        Popcorn = 0
                        break
                    else:
                        print("Please select valid option")
                        
                user_details.append(self.seat_num)
                user_details.append(Name)
                user_details.append(Gender)
                user_details.append(Age)
                user_details.append('$ '+str(Ticket_price))
                user_details.append(Phone_No)
                user_details.append(str(Popcorn))
                self.net_income.append(Ticket_price)
                self.booking_info.append(user_details)
                self.seats_list.append(self.seat_num)
                self.fnb.append(Popcorn)
                self.arranged_seats[ord(self.seat_num[0])-(ord("A")-1)][int(self.seat_num[1:])] = "\033[1;31m"+"B"+'\033[m'
                
                print("\nYour ticket has been Booked successfully!!\n\nYour Details:\n")
                print("Seat No: ",self.seat_num)
                print("Name:",Name)
                print("Gender:",Gender)
                print("Age:",Age)
                print("Phone_No.:",Phone_No)
                print("F&B:", ans)
                return self.booking_info
                break
    
    def stats(self):
        self.occupancy = (len(self.seats_list)/self.capacity)*100
        return self.occupancy
    
    def total_income(self):
        income = None
        if self.x*self.y <= 60 :
            income = self.x*self.y*10
        else:
            top_line = self.x//2
            back_line = self.x - (self.x//2)
            front = top_line*self.y*10
            back = back_line*self.y*8
            income = front+back
        return income
