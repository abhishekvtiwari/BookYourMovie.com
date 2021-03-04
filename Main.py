import seat_book

Movie = seat_book.Booking()

while True:
    print("\n\nWelcome to BookYourMovie.com\nBookYourMovies brings booking tickets for movies to your fingertips\n")
    print("\nMain-Menu:")
    print("1. Show Seating Arrangement")
    print("2. Book a seat")
    print("3. Show Booking Details")
    print("4. Statistics")
    print("0. Exit")
    n = input("Please select of your desired option:(for eg. 1, 2 or 3)\n")
    if n == "1":
        print("\n")
        print("Cinema:\n")
        print("__"*5+"\033[4mScreen This Way!\033[m"+"__"*5+"\n")
        print('\n'.join('\t'.join(i) for i in Movie.arranged_seats))
        print("\nPlease Note:")
        print('i. '+"\033[1;32m"+"S"+"\033[m" +" = Unreserved Seats(Availble for Booking)")
        print('ii. '+"\033[1;31m"+"B"+"\033[m" +" = reserved Seats(Not Availble for Booking)")
        while True:
            book_seat = input("Would you like to book a seat? y/n\n")
            if  book_seat =="y" or book_seat == 'Y':
                Movie.info_taking()
                while True:
                    q = input('would you like to book another seat? y/n\n')
                    if q =="y" or q == 'Y':
                        Movie.info_taking()
                    elif q =='n' or q == 'N':
                        print('Thank you for booking ticket with us!')
                        break
                    else:
                        print("Please select a valid option")
                break
            elif book_seat =="N" or book_seat =="n":
                print("\nDiverting you to Main Menu...\nThank you!")
                break
            
            else:
                print("Please select a valid option")
    elif n=="2":
        print("\n")
        Movie.info_taking()
        while True:
            q = input('would you like to book another seat? y/n\n')
            if q =="y" or q == 'Y':
                Movie.info_taking()
            elif q =='n' or q == 'N':
                print('Diverting you to Main Menu...\nThank you for booking your ticket with BookMyMovie.com!')
                break
            else:
                print("Please select a valid option")
    elif n == "3":
        print("\n")
        if len(Movie.booking_info) == 1 :
            print("No Bookings till now!!\n")
            print('\n'.join('\t'.join(i) for i in Movie.booking_info))
        else:
            length_list = [len(element) for row in Movie.booking_info for element in row]
            column_width = max(length_list)
            for row in Movie.booking_info:
                row = " ".join(element.ljust(column_width+1)for element in row)
                print(row)
        print('\n')
    elif n =="4":
        print("\nStatistics:\n")
        print("Number of Ticket Purchased: ", len(Movie.seats_list))
        print("Percentage of Tickets Booked:","{:.2f}".format(Movie.stats()),"%")
        print("Current Income: $",sum(Movie.net_income))
        print("Total Income (Max Income from sell of Tickets): $", Movie.total_income())
        print("Food & Beverages Income: $", sum(Movie.fnb))
        
    elif n == "0":
        break
    else:
        print("\n")
        print("Please select a valid option")
        print("\n")
