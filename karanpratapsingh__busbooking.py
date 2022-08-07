from tkinter import*

import sqlite3


root=Tk()
root.geometry('1200x650')

img=PhotoImage(file="bus1.gif")
img_label=Label(image=img)
img_label.pack()               
img_label.grid(column=0)
bus_servise_name_label=Label(root,text='WELCOME IN RUDRA ONLINE BUS BOOKING SERVISE',bg="gray", font=('Verdana',16))
bus_servise_name_label.grid()

#creating the database

con=sqlite3.Connection("Bus_booking")
cur=con.cursor()
cur.execute("""CREATE TABLE if not exists Bus_provider(
                                                 F_name varchar(15) not null,
                                                 Contact int(10) not null,
                                                 Address varchar(20) not null,
                                                 Operator varchar(15) not null,
                                                 Source_station varchar(15) not null,
                                                 Destination_station varchar(15) not null,
                                                 Departure_Time time not null,
                                                 Arrival_Time time not null,
                                                 Fare int(5) not null,
                                                 Seats int(5) not null,
                                                 Travelling_Time int(5) not null,
                                                 Bus_Date date not null
                                                 
                                                  )""")

cur.execute(""" CREATE TABLE if not exists Bus(
                                                Operator varchar(15) not null,
                                                Bus_type varchar(15) not null,
                                                Source_station varchar(15) not null,
                                                Destination_station varchar(15) not null,
                                                Departure_Time time not null,
                                                Arrival_Time time not null,
                                                Fare int(5) not null,
                                                Seats int(5) not null,
                                                Travelling_Time int(5) not null,
                                                Bus_Date date not null

                                                )""")

cur.execute(" PRAGMA table_info(Bus_provider)")
                                                

con.commit()
print(cur.fetchall())
con.close()


            


def fun1():
    root1=Tk()
    root1.title('ADD BUSS')
    root1.geometry('600x600')
    bus_operator_detail_filling=Label(root1,text="       Bus Operator Detail filling:",fg='navy',font=('Verdana',25))
    bus_operator_detail_filling.grid()
    
    F_name_label=Label(root1,text="\nFull Name :",font=('Verdana',12))
    F_name_label.grid()
    F_name=Entry(root1)
    F_name.grid()
    Contact_label=Label(root1,text="\nContanct No. :",font=('Verdana',12))
    Contact_label.grid()
    Contact=Entry(root1)
    Contact.grid()
    Address_label=Label(root1,text="\nAddress : ",font=('Verdana',12))
    Address_label.grid()
    Address=Entry(root1)
    Address.grid()
    Label(root1,text="\n").grid()

    
    def fun1_1():
        more_details_root1=Label(root1,text="More Details ",fg='navy',font=('Verdana',18,'bold'))
        more_details_root1.grid()
        Label(root1,text="  ").grid()
        
        Operator_label=Label(root1,text="Operaor:",font=("Verdana",12))
        Operator_label.grid(row=20,sticky=W,padx=20)
        Operator=Entry(root1)
        Operator.grid(row=20,sticky=W,padx=100)
        choice1=['AC','Non AC','AC-Sleeper','Non-AC-Sleeper','regular','other']
        V1=StringVar(root1)
        V1.set(choice1[5])
        bus_type_label=Label(root1,text="Bus Type: ",font=("Verdana",12))
        bus_type_label.grid(row=20,sticky=E,padx=125)
        Bus_type=OptionMenu(root1,V1,*choice1)
        Bus_type.grid(row=20,sticky=E)
        Source_station_label=Label(root1,text="From: ",font=('Verdana',12))
        Source_station_label.grid(row=21,sticky=W,padx=20)
        Source_station=Entry(root1)
        Source_station.grid(row=21,sticky=W,padx=100)
        Destination_station_label=Label(root1,text="To: ",font=('Verdana',12))
        Destination_station_label.grid(row=21,sticky=E,padx=125)
        Destination_station=Entry(root1)
        Destination_station.grid(row=21,sticky=E)
        Departure_time_label=Label(root1,text="Departur Time:  ",font=('Verdana',12))
        Departure_time_label.grid(row=22,sticky=W,padx=10)
        Departure_time=Entry(root1)
        Departure_time.grid(row=22,sticky=W,padx=130)
        Arrive_time_label=Label(root1,text="Arrive Time: ",font=('Verdana',12))
        Arrive_time_label.grid(row=22,sticky=E,padx=125)
        Arrive_time=Entry(root1)
        Arrive_time.grid(row=22,sticky=E)
        Fare_label=Label(root1,text="Fare:",font=('Verdana',12))
        Fare_label.grid(row=23,sticky=W,padx=20)
        Fare=Entry(root1)
        Fare.grid(row=23,sticky=W,padx=100)
        Seats_label=Label(root1,text="Seats: ",font=('Verdana',12))
        Seats_label.grid(row=23,sticky=E,padx=125)
        Seats=Entry(root1)
        Seats.grid(row=23,sticky=E)
        Travelling_time_label=Label(root1,text="Travel_time:  ",font=('Verdana',12))
        Travelling_time_label.grid(row=24,sticky=W,padx=10)
        Travelling_time=Entry(root1)
        Travelling_time.grid(row=24,sticky=W,padx=125)
        Date_label=Label(root1,text="Date:",font=('Verdana',12))
        Date_label.grid(row=24,sticky=E,padx=125)
        Date=Entry(root1)
        Date.grid(row=24,sticky=E)
        Label(root1,text="\n").grid()
        
        
        def fun1_1_1():
            #save the data in database
            con=sqlite3.Connection("Bus_booking")
            cur=con.cursor()
            cur.execute("INSERT INTO Bus_provider Values(:F_name, :Contact, :Address, :Operator,  :Source_station, :Destination_station, :Departure_time, :Arrive_time, :Fare, :Seats, :Travelling_time, :Date)",
            {
                                        
                            'F_name': F_name.get(),
                            'Contact': Contact.get(),
                            'Address': Address.get(),
                            'Operator': Operator.get(),
                            #'Bus_type': Bus_type.get(),
                            'Source_station': Source_station.get(),
                            'Destination_station': Destination_station.get(),
                            'Departure_time': Departure_time.get(),
                            'Arrive_time': Arrive_time.get(),
                            'Fare': Fare.get(),
                            'Seats': Seats.get(),
                            'Travelling_time': Travelling_time.get(),
                            'Date': Date.get()

             })
            con.commit()
            con.close()
                  
                         
            F_name.delete(0,END)
            Contact.delete(0,END)
            Address.delete(0,END)
            Operator.delete(0,END)
            Source_station.delete(0,END)
            Destination_station.delete(0,END)
            Departure_time.delete(0,END)
            Arrive_time.delete(0,END)
            Fare.delete(0,END)
            Seats.delete(0,END)
            Travelling_time.delete(0,END)
            Date.delete(0,END)
            root1.destroy() 
    
            
            
        save_root1_button=Button(root1,text="SAVE",font=('Verdana',15),bg="yellow",activebackground="navy",activeforeground="white",command=lambda:[fun1_1_1()])
        save_root1_button.grid()
        
        
    add_bus_root1_button=Button(root1,text="ADD BUS ",font=('Verdana',15),bg="Yellow",activebackground="navy",activeforeground="white",command=lambda:[fun1_1()])
    add_bus_root1_button.grid()

    

add_bus_root_button=Button(root,text='ADD BUS',width=20,height=3,activebackground="navy",activeforeground="white",bg="yellow",command=lambda:[fun1()])
add_bus_root_button.grid(row=2,padx=20,sticky=W)
def fun2():
    root2=Tk()
    root2.geometry('500x500')
    root2.title("Listing Buses")
    Listing_buses_root2_label=Label(root2,text="Listing Buses ",font=('Verdana',18,'bold'),fg='navy')
    Listing_buses_root2_label.grid(padx=150)
    Label(root2,text=" \n\n").grid()
    
    Bus_type_label=Label(root2,text="Bus Type: ",font=('Verdana',12))
    Bus_type_label.grid(row=1,sticky=W,padx=100)
    choice2=['AC','Non AC','AC-Sleeper','Non-AC-Sleeper','Other']
    V2=StringVar(root2)
    V2.set(choice2[0])
    Bus_type=OptionMenu(root2,V2,*choice2)
    Bus_type.grid(row=1,sticky=E,padx=125)
    From_label=Label(root2,text="From: ",font=('Verdana',12))
    From_label.grid(row=2,sticky=W,padx=100)
    From=Entry(root2)
    From.grid(row=2,sticky=E,padx=125)
    To_label=Label(root2,text="To: ",font=('Verdana',12))
    To_label.grid(row=3,sticky=W,padx=100)
    To=Entry(root2)
    To.grid(row=3,sticky=E,padx=125)
    Date_label=Label(root2,text="Date: ",font=('Verdana',12))
    Date_label.grid(row=4,sticky=W,padx=100)
    Date=Entry(root2)
    Date.grid(row=4,sticky=E,padx=125)
    Label(root2,text=" ").grid()
     

    def fun2_1():
        root2.withdraw()
        root3=Tk()
        root3.geometry('1200x400')
        bus_detail_label=Label(root3,text="Bus  Details",fg='navy',font=('Verdana',24,'bold underline'))
        bus_detail_label.grid(row=1,sticky=W,padx=450)
        Label(root3,text=" ").grid()
        Operator_label=Label(root3,text="Operator",font=('Verdana',13,'bold'))
        Operator_label.grid(row=3,sticky=W,padx=10)
        Bus_type_label=Label(root3,text="Bus Type ",font=('Verdana',13,'bold'))
        Bus_type_label.grid(row=3,sticky=W,padx=150)
        Source_station_label=Label(root3,text="From" ,font=('Verdana',13,'bold'))
        Source_station_label.grid(row=3,sticky=W,padx=280)
        Destination_station_label=Label(root3,text="To ",font=('Verdana',13,'bold'))
        Destination_station_label.grid(row=3,sticky=W,padx=380)
        Date_label=Label(root3,text="Date",font=('Verdana',13,'bold'))
        Date_label.grid(row=3,sticky=W,padx=440)
        Departure_time_label=Label(root3,text="Dep Time ",font=('Verdana',13,'bold'))
        Departure_time_label.grid(row=3,sticky=W,padx=530)
        Arrive_time_label=Label(root3,text="Arr time",font=('Verdana',13,'bold'))
        Arrive_time_label.grid(row=3,sticky=W,padx=670)
        Fare_label=Label(root3,text="Fare",font=('verdana',13,'bold'))
        Fare_label.grid(row=3,sticky=W,padx=790)
        Seats_available_label=Label(root3,text="Seats Available",font=('Verdana',13,'bold'))
        Seats_available_label.grid(row=3,sticky=W,padx=870)
        Select_button_label=Label(root3,text="Select",font=('Verdnana',13,'bold'))
        Select_button_label.grid(row=3,sticky=W,padx=1100)
        Book_button=Button(root3,text='  confirm  ',bg="light blue",fg="black",font=('Verdana',12,'bold'))
        Book_button.grid(row=4,sticky=W,padx=1050)
        
        
        

        con=sqlite3.Connection("Bus_booking")
        cur=con.cursor()
        cur.execute("SELECT * FROM Bus_provider")
        #cur.execute("DELETE FROM Bus_provider")
        records=cur.fetchall()
        #print(records)

        print_records=" "
        for record in records:
            print_records += str(record[3]) + "\n"

           
        query_label=Label(root3,text=print_records)
        query_label.grid(row=4,sticky=W,padx=10)
            
        
        con.commit()
        con.close()
        
        return
        
        
       
              
        
    search_bus_root2_button=Button(root2,text="Search Bus ",font=('Verdana',13,'bold'),bg="yellow",activebackground="navy",activeforeground="white",command=lambda:[fun2_1()])
    search_bus_root2_button.grid()
    
       
          
    
    
        
search_bus_root_button=Button(root,text='SEARCH BUS',width=20,height=3,activebackground="navy",activeforeground="white",bg="Yellow",command=lambda:[fun2()])
search_bus_root_button.grid(row=2,padx=20,sticky=E)


root.mainloop()
 

