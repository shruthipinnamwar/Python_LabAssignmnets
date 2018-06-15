class Hotel:
    def __init__(self, hotnam): #constructor
        self.hotelname = hotnam
       
class Employee:
    def __init__(self, enam, eid,essn): #constructor
        self.employeename = enam
        self.empid = eid     
    def __getssn(self):                        #private data member
#        print("Employee SSN is:" + self.essn)
        print("Employee SSN is 78787")
        return
    def callprivate(self):
        self.__getssn()
    def getEmployeeDetails(self):
        print("Employee Name:" +  self.employeename)
        print("Employee Id is" + self.empid)
        
class Room:
    def __init__(self,rnum,rtype):
        self.roomnum = rnum
        self.roomtyp = rtype
    def GetRoomDetails(self):
        print("Room number:" +  self.roomnum)
        print("ERoom Type" + self.roomtyp)
class Occupants:
    def __init__(self,onam,ophon,oid):
        self.occname = onam
        self.occphone = ophon
        self.occid = oid
    
class Owner(Hotel):    # Inheritance
    def __init(self,hotnam,onam,oid):
        super().hotelname = hotnam
        self.ownname = onam
        self.ownid = oid
       
        
print("Welcome to Hotel ABC Online Reservation ")

    
name = input("enter your name:")
ide = input("Enter your id:")
ssn = input("Enter your ssn:")
emp1 = Employee(name,ide,ssn)


roomtype = input("What kind of room do you wantLuxurt/Normal:")
room1 = Room("6587875",roomtype)

print("Your Reservation Details are:")


emp1.getEmployeeDetails()
room1.GetRoomDetails()
#Emp1.callprivate()
      
      
    
    
#    if (choice == 1):
#        hotelname = input("enter the hotel name")
#        a = Hotel(hotelname)
#    if (choice == 2):
#        employeename = input("enter the employee name")
#        employeeage = input("enter the employee age")
#        employeessn = input("enter the employee Id number")
#        b = HotelEmployee(employeename,employeeage,employeessn)
#
#    if (choice == 3):
#        roomnumber = input("enter the room number")
#        roomtype = input("enter the room type")
#        c = Room(roomnumber,roomtype)
#
#    if (choice == 4):
#        customername= input("enter the name of customer")
#        customerphone = input("enter the phone number of customer")
#        roomnum = input("enter the room number customer has taken")
#        d = Occupant(customername,customerphone,roomnum)
#
#    if (choice==6):
#        break
#
#    if(choice==5):
#        d.display()
        
        
        
        
#Creating Employees
#Emp1 = Employee("Shruthi", "DES", 400)
#print("Employees Details:")
#Emp1.getEmployeeDetails()
#Emp1.callprivate()
#Room1 = Room("5656","Luxury")
#print("Room Details:")
#Room1.GetRoomDetails()

        
