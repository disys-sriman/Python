class phone_Contacts:
    def __init__(self, Firstname, Lastname, Phone_number, Email_ID, Groups, DOB):
        self.firstname = Firstname
        self.lastname = Lastname
        self.phonenumber = Phone_number
        self.emailid = Email_ID
        self.groups = Groups
        self.dob = DOB

    def open_phcontacts(self):
        print("Phone Contacts")

    def firstname_verification(self):
        if type(self.firstname) == str:
            if len(self.firstname) <= 15:
                print("Firstnameame verified")
            else:
                raise ValueError("Firstnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Firstname should contain letters only")

    def lastname_verification(self):
        if type(self.lastname) == str:
            if len(self.lastname) <= 15:
                print("Lastnameame verified")
            else:
                raise ValueError("Lastnameame should contain lesser than or equal to 15 letters")
        else:
            raise TypeError("Lastname should contain letters only")

    def phonenumber_verification(self):
        if (len(self.phonenumber) == 10):
            if type(self.phonenumber) == str:
                print("Phone number verified")
            else:
                raise TypeError("Phone number should contain only integers ")
        else:
            raise ValueError("phone number should not be grater than or lesser than 10")

    def emailid_verification(self):
        if type(self.emailid) == str:
            if len(self.emailid) <= 25:
                print("Emailid verified")
            else:
                raise ValueError("Emailid should not contain more than 25 values")
        else:
            raise TypeError("Invalid emailid")

    def groups_verification(self):
        if type(self.groups) == str:
            if len(self.groups) <= 10:
                print("Groups verified")
            else:
                raise ValueError("Groups should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("Groups should contain letters only")

    def dob_verification(self):
        if isinstance(self.dob, str):
            if len(self.dob) <= 10:
                print("DOB verified")
            else:
                raise ValueError("DOB should contain lesser than or equal to 10 letters")
        else:
            raise TypeError("DOB should contain numbers and symbols only")


Sriman = phone_Contacts("Sriman", "S", "888816987", "sriman07@gmail.com", "Family", "15/01/2001")
Sriman.open_phcontacts()
Sriman.firstname_verification()
Sriman.lastname_verification()
Sriman.phonenumber_verification()
Sriman.emailid_verification()
Sriman.groups_verification()
Sriman.dob_verification()

phone = [{"Firstname": "Abishek", "Lastname": "R", "Phno": 9854268725, "Email_id": "abi@gmail.com", "Groups": "Family",
          "DOB": "08/04/2001"},  # DICTIONARY INSIDE LIST
         {"Firstname": "Anu", "Lastname": "priyaa", "Phno": 9986338725, "Email_id": "anu@gmail.com",
          "Groups": "Friends", "DOB": "03/05/2001"},
         {"Firstname": "Anitha", "Lastname": "mani", "Phno": 98542683335, "Email_id": "anitha@gmail.com",
          "Groups": "Family", "DOB": "30/05/2003"},
         {"Firstname": "manaal", "Lastname": "safeera", "Phno": 9674268225, "Email_id": "manaal@gmail.com",
          "Groups": "Family", "DOB": "09/10/2010"},
         {"Firstname": "Jehara", "Lastname": "fathima", "Phno": 6574839373, "Email_id": "jehara@gmail.com",
          "Groups": "Family", "DOB": "04/04/2006"},
         {"Firstname": "safrin", "Lastname": "Reehana", "Phno": 9854268725, "Email_id": "safrin@gmail.com",
          "Groups": "Family", "DOB": "20/12/2000"},
         {"Firstname": "yusuf", "Lastname": "yusufkhan", "Phno": 9842448248, "Email_id": "yusuf@gmail.com",
          "Groups": "Family", "DOB": "15/09/1990"},
         {"Firstname": "sabitha", "Lastname": "banu", "Phno": 9800098789, "Email_id": "sabi@gmail.com",
          "Groups": "Family", "DOB": "30/01/2000"},
         {"Firstname": "Ahamed", "Lastname": "k", "Phno": 9597916931, "Email_id": "ahamed@gmail.com",
          "Groups": "Family", "DOB": "24/01/2001"},
         {"Firstname": "riyas", "Lastname": "Khan", "Phno": 9854223446, "Email_id": "khan@gmail.com",
          "Groups": "Family", "DOB": "07/08/1994"},
         {"Firstname": "sofia", "Lastname": "riyas", "Phno": 9854268725, "Email_id": "sofi233@gmail.com",
          "Groups": "Family", "DOB": "26/07/1996"},
         {"Firstname": "shifana", "Lastname": "k", "Phno": 9008762565, "Email_id": "shifana@gmail.com",
          "Groups": "Family", "DOB": "18/04/2014"},
         {"Firstname": "noor", "Lastname": "nisha", "Phno": 6545686576, "Email_id": "nisha11@gmail.com",
          "Groups": "Family", "DOB": "22/08/2012"},
         {"Firstname": "dilshad", "Lastname": "begum", "Phno": 7909826226, "Email_id": "dilshad@gmail.com",
          "Groups": "Family", "DOB": "20/07/1999"},
         {"Firstname": "pavithra", "Lastname": "k", "Phno": 93436377788, "Email_id": "pavi22@gmail.com",
          "Groups": "Family", "DOB": "29/09/1998"},
         {"Firstname": "mani", "Lastname": "kandan", "Phno": 8245434786, "Email_id": "manikandan@gmail.com",
          "Groups": "Friends", "DOB": "08/04/2000"},
         {"Firstname": "Ajith", "Lastname": "Kumar", "Phno": 9854500098, "Email_id": "ajith@gmail.com",
          "Groups": "Friends", "DOB": "14/11/2000"},
         {"Firstname": "bala", "Lastname": "krishnan", "Phno": 9876767676, "Email_id": "balakrish@gmail.com",
          "Groups": "Friends", "DOB": "18/01/1999"},
         {"Firstname": "thanveer", "Lastname": "n", "Phno": 9842449250, "Email_id": "thanveer@gmail.com",
          "Groups": "Friends", "DOB": "18/11/2000"},
         {"Firstname": "praveen", "Lastname": "pp", "Phno": 9854260983, "Email_id": "praveen@gmail.com",
          "Groups": "Friends", "DOB": "30/08/2001"},
         {"Firstname": "shahul", "Lastname": "hameed", "Phno": 9444562058, "Email_id": "shahul@gmail.com",
          "Groups": "Friends", "DOB": "28/11/2000"},
         {"Firstname": "prasanna", "Lastname": "paneer", "Phno": 9854268725, "Email_id": "prasanna@gmail.com",
          "Groups": "Friends", "DOB": "11/09/1999"},
         {"Firstname": "suganth", "Lastname": "r", "Phno": 9854263333, "Email_id": "suganth@gmail.com",
          "Groups": "Friends", "DOB": "08/04/1998"},
         {"Firstname": "natrajan", "Lastname": "marimuthu", "Phno": 9854233325, "Email_id": "natrajan@gmail.com",
          "Groups": "Friends", "DOB": "28/06/1987"},
         {"Firstname": "priya", "Lastname": "jeyaram", "Phno": 8549685645, "Email_id": "priya@gmail.com",
          "Groups": "Friends", "DOB": "03/09/2011"},
         {"Firstname": "swetha", "Lastname": "gandhi", "Phno": 9942810046, "Email_id": "abi@gmail.com",
          "Groups": "Friends", "DOB": "02/01/2000"},
         {"Firstname": "jesmitha", "Lastname": "ahmeed", "Phno": 9878785454, "Email_id": "jesmi@gmail.com",
          "Groups": "Friends", "DOB": "08/04/2001"},
         {"Firstname": "jeryln", "Lastname": "synthuia", "Phno": 7876545678, "Email_id": "jerlyn@gmail.com",
          "Groups": "Friends", "DOB": "17/10/2013"},
         {"Firstname": "Abivagas", "Lastname": "Rithinyaa", "Phno": 9854268725, "Email_id": "abi@gmail.com",
          "Groups": "Friends", "DOB": "27/02/2000"},
         {"Firstname": "Abimaniyu", "Lastname": "kumar", "Phno": 9876787643, "Email_id": "abimaniyu@gmail.com",
          "Groups": "Friends", "DOB": "18/09/2000"},
         {"Firstname": "vishal", "Lastname": "k", "Phno": 9854268725, "Email_id": "vishal@gmail.com",
          "Groups": "Friends", "DOB": "15/02/1997"},
         {"Firstname": "vishnu", "Lastname": "a", "Phno": 9854268725, "Email_id": "vishnh@gmail.com",
          "Groups": "Friends", "DOB": "30/04/1998"},
         {"Firstname": "dhanush", "Lastname": "kumar", "Phno": 9854268725, "Email_id": "dhanush@gmail.com",
          "Groups": "Friends", "DOB": "24/10/1999"},
         {"Firstname": "santhosh", "Lastname": "raj", "Phno": 9854268725, "Email_id": "santhosh@gmail.com",
          "Groups": "Family", "DOB": "08/09/1976"},
         {"Firstname": "nittesb", "Lastname": "mani", "Phno": 9854268725, "Email_id": "nithesh@gmail.com",
          "Groups": "Friends", "DOB": "28/04/2000"},
         {"Firstname": "sree", "Lastname": "raj", "Phno": 9854268725, "Email_id": "sree@gmail.com", "Groups": "Friends",
          "DOB": "02/09/2000"},
         {"Firstname": "sri", "Lastname": "man", "Phno": 9854268725, "Email_id": "sriman@gmail.com",
          "Groups": "Friends", "DOB": "04/02/2001"},
         {"Firstname": "sri", "Lastname": "ram", "Phno": 9854268725, "Email_id": "sriram@gmail.com",
          "Groups": "Friends", "DOB": "06/01/1998"},
         {"Firstname": "jeya", "Lastname": "dev", "Phno": 9854268725, "Email_id": "jeyadev@gmail.com",
          "Groups": "Friends", "DOB": "08/04/1998"},
         {"Firstname": "aakash", "Lastname": "kanna", "Phno": 6575454657, "Email_id": "aakash@gmail.com",
          "Groups": "Friends", "DOB": "08/04/1997"},
         {"Firstname": "tirupathi", "Lastname": "narayanan", "Phno": 9852228725, "Email_id": "tirupathi@gmail.com",
          "Groups": "Friends", "DOB": "08/04/1999"},
         {"Firstname": "angu", "Lastname": "vinayagam", "Phno": 9854268725, "Email_id": "angu@gmail.com",
          "Groups": "Family", "DOB": "12/06/2004"},
         {"Firstname": "vinayak", "Lastname": "raj", "Phno": 7867545367, "Email_id": "vinayak@gmail.com",
          "Groups": "Family", "DOB": "18/04/2007"},
         {"Firstname": "arsath", "Lastname": "ahamed", "Phno": 8773737783, "Email_id": "arsath@gmail.com",
          "Groups": "Family", "DOB": "29/04/2000"},
         {"Firstname": "aspaq", "Lastname": "ahamed", "Phno": 98523338725, "Email_id": "aspaq@gmail.com",
          "Groups": "Family", "DOB": "30/06/1996"},
         {"Firstname": "adhil", "Lastname": "k", "Phno": 9853368725, "Email_id": "aadil@gmail.com", "Groups": "Family",
          "DOB": "08/12/1997"},
         {"Firstname": "abdullah", "Lastname": "k", "Phno": 649393837, "Email_id": "abdullah@gmail.com",
          "Groups": "Family", "DOB": "9/11/1998"},
         {"Firstname": "rajini", "Lastname": "kanth", "Phno": 9854268725, "Email_id": "rajini@gmail.com",
          "Groups": "Family", "DOB": "19/04/1998"},
         {"Firstname": "silambarsan", "Lastname": "tr", "Phno": 8767546467, "Email_id": "silambarsan@gmail.com",
          "Groups": "Family", "DOB": "09/12/1999"},
         {"Firstname": "mukesh", "Lastname": "kanna", "tr": 9854268725, "Email_id": "mukesh@gmail.com",
          "Groups": "Family", "DOB": "10/04/2000"},
         {"Firstname": "dinesh", "Lastname": "anand", "Phno": 9876787444, "Email_id": "dinesh@gmail.com",
          "Groups": "Family", "DOB": "08/09/1999"},
         {"Firstname": "karthi", "Lastname": "keyan", "Phno": 9854268725, "Email_id": "karthi@gmail.com",
          "Groups": "Family", "DOB": "08/04/1988"},
         {"Firstname": "mahesh", "Lastname": "waran", "Phno": 93483958343, "Email_id": "mahesh@gmail.com",
          "Groups": "Family", "DOB": "08/04/1996"},
         {"Firstname": "pandi", "Lastname": "p", "Phno": 9943418320, "Email_id": "pandi@gmail.com", "Groups": "Family",
          "DOB": "08/04/1996"},
         {"Firstname": "nirai", "Lastname": "mathi", "Phno": 9854268725, "Email_id": "nirai@gmail.com",
          "Groups": "Family", "DOB": "08/04/1994"},
         {"Firstname": "dhivya", "Lastname": "dharshini", "Phno": 6398787645, "Email_id": "dhivya@gmail.com",
          "Groups": "Family", "DOB": "08/12/2005"},
         {"Firstname": "gayathri", "Lastname": "rishi", "Phno": 9323848498, "Email_id": "gayathri@gmail.com",
          "Groups": "Family", "DOB": "19/08/2008"},
         {"Firstname": "rishi", "Lastname": "natrajan", "Phno": 985323468725, "Email_id": "rishi@gmail.com",
          "Groups": "Family", "DOB": "27/02/2011"},
         {"Firstname": "kovil", "Lastname": "kumar", "Phno": 98542687445, "Email_id": "abi@gmail.com",
          "Groups": "Family", "DOB": "31/04/2001"},
         {"Firstname": "subra", "Lastname": "mani", "Phno": 98542687765, "Email_id": "subramani@gmail.com",
          "Groups": "Family", "DOB": "22/03/2001"},
         {"Firstname": "hrithik", "Lastname": "raja", "Phno": 98542687098, "Email_id": "hrithik@gmail.com",
          "Groups": "Family", "DOB": "08/01/2001"},
         {"Firstname": "hayagriv", "Lastname": "narayanan", "Phno": 9854268234, "Email_id": "hayagrib@gmail.com",
          "Groups": "Family", "DOB": "19/04/2001"},
         {"Firstname": "indhu", "Lastname": "Rithinyaa", "Phno": 9854260494, "Email_id": "indhu@gmail.com",
          "Groups": "Family", "DOB": "30/10/2001"},
         {"Firstname": "josyln", "Lastname": "jane", "Phno": 9854268725, "Email_id": "josylyn@gmail.com",
          "Groups": "Family", "DOB": "23/04/2001"},
         {"Firstname": "Abdul", "Lastname": "rahman", "Phno": 9853368725, "Email_id": "abdulrahuman@gmail.com",
          "Groups": "Family", "DOB": "23/12/2001"},
         {"Firstname": "dhisan", "Lastname": "s", "Phno": 9854268725, "Email_id": "dhisan@gmail.com",
          "Groups": "Family", "DOB": "08/2/1998"},
         {"Firstname": "safrin", "Lastname": "fathima", "Phno": 9854268725, "Email_id": "safrin@gmail.com",
          "Groups": "Family", "DOB": "06/04/1997"},
         {"Firstname": "afrash", "Lastname": "t", "Phno": 9854268725, "Email_id": "afrsh@gmail.com", "Groups": "Family",
          "DOB": "09/05/1998"},
         {"Firstname": "ajash", "Lastname": "k", "Phno": 878968725, "Email_id": "ajash@gmail.com", "Groups": "Family",
          "DOB": "22/07/1996"},
         {"Firstname": "abbas", "Lastname": "h", "Phno": 98884268725, "Email_id": "abbas@gmail.com", "Groups": "Family",
          "DOB": "22/06/1996"},
         {"Firstname": "kamal", "Lastname": "batsha", "Phno": 8854268725, "Email_id": "kamal@gmail.com",
          "Groups": "Family", "DOB": "28/08/1993"},
         {"Firstname": "suhail", "Lastname": "d", "Phno": 7854268725, "Email_id": "suhail@gmail.com",
          "Groups": "Family", "DOB": "09/11/1994"},
         {"Firstname": "suhaib", "Lastname": "d", "Phno": 9854268725, "Email_id": "suhain@gmail.com",
          "Groups": "Family", "DOB": "05/12/2011"},
         {"Firstname": "keerthana", "Lastname": "d", "Phno": 9854268725, "Email_id": "keerthana@gmail.com",
          "Groups": "Family", "DOB": "03/10/1999"},
         {"Firstname": "aafrin", "Lastname": "fathima", "Phno": 9854268725, "Email_id": "aafrin@gmail.com",
          "Groups": "Family", "DOB": "28/04/1999"},
         {"Firstname": "aiswarya", "Lastname": "t", "Phno": 9854268725, "Email_id": "aiswarya@gmail.com",
          "Groups": "Family", "DOB": "18/3/1987"},
         {"Firstname": "ravi", "Lastname": "shankar", "Phno": 9854268725, "Email_id": "ravi@gmail.com",
          "Groups": "Family", "DOB": "28/04/2001"},
         {"Firstname": "kumar", "Lastname": "raja", "Phno": 9854268725, "Email_id": "kumar@gmail.com",
          "Groups": "Family", "DOB": "19/12/1999"},
         {"Firstname": "rohit", "Lastname": "sharma", "Phno": 7906545376, "Email_id": "rohit@gmail.com",
          "Groups": "Family", "DOB": "02/11/1998"},
         {"Firstname": "dhawan", "Lastname": "skiher", "Phno": 9800765008, "Email_id": "dhawan@gmail.com",
          "Groups": "Family", "DOB": "06/06/2001"},
         {"Firstname": "bhuvi", "Lastname": "Rithinyaa", "Phno": 9007890078, "Email_id": "bhuvi@gmail.com",
          "Groups": "Family", "DOB": "02/12/1996"},
         {"Firstname": "gomathi", "Lastname": "sankar", "Phno": 9870098700, "Email_id": "gomathi@gmail.com",
          "Groups": "Family", "DOB": "05/11/2001"},
         {"Firstname": "dhanraj", "Lastname": "k", "Phno": 9657890008, "Email_id": "dhanraj@gmail.com",
          "Groups": "Family", "DOB": "21/05/1999"},
         {"Firstname": "aravind", "Lastname": "babu", "Phno": 987655677, "Email_id": "arvind@gmail.com",
          "Groups": "Family", "DOB": "08/03/1998"},
         {"Firstname": "nisha", "Lastname": "begum", "Phno": 6350550463, "Email_id": "nisha@gmail.com",
          "Groups": "Family", "DOB": "4/09/1995"},
         {"Firstname": "hwakani", "Lastname": "nisha", "Phno": 9854268725, "Email_id": "hwakani@gmail.com",
          "Groups": "Family", "DOB": "25/06/2000"},
         {"Firstname": "apsana", "Lastname": "nisha", "Phno": 7867898767, "Email_id": "apsana@gmail.com",
          "Groups": "Family", "DOB": "23/04/2001"},
         {"Firstname": "mohamed", "Lastname": "idrish", "Phno": 7373608055, "Email_id": "mohamed@gmail.com",
          "Groups": "Family", "DOB": "08/04/2001"},
         {"Firstname": "keerthi", "Lastname": "sursh", "Phno": 654545676, "Email_id": "keerthi@gmail.com",
          "Groups": "Family", "DOB": "08/04/2001"},
         {"Firstname": "siva", "Lastname": "sankar", "Phno": 9854268725, "Email_id": "siva@gmail.com",
          "Groups": "Family", "DOB": "08/04/2001"},
         {"Firstname": "veera", "Lastname": "muthu", "Phno": 9854268725, "Email_id": "veera@gmail.com",
          "Groups": "Family", "DOB": "08/04/2001"},
         {"Firstname": "alan", "Lastname": "andrew", "Phno": 9854268725, "Email_id": "renose@gmail.com",
          "Groups": "Family", "DOB": "08/04/2001"},
         {"Firstname": "muthu", "Lastname": "sankar", "Phno": 9854268725, "Email_id": "muthu@gmail.com",
          "Groups": "Family", "DOB": "08/04/2001"},
         {"Firstname": "balaa", "Lastname": "mani", "Phno": 9854268725, "Email_id": "balaa@gmail.com",
          "Groups": "Family", "DOB": "08/03/2001"},
         {"Firstname": "prasanna", "Lastname": "kumar", "Phno": 9854268725, "Email_id": "prasanna@gmail.com",
          "Groups": "Family", "DOB": "08/12/2001"},
         {"Firstname": "renose", "Lastname": "fathima", "Phno": 9854268725, "Email_id": "mandela@gmail.com",
          "Groups": "Family", "DOB": "03/11/2001"},
         {"Firstname": "mandela", "Lastname": "mani", "Phno": 9854268725, "Email_id": "vijay@gmail.com",
          "Groups": "Family", "DOB": "03/10/2001"},
         {"Firstname": "vijay", "Lastname": "sethupathi", "Phno": 9854268725, "Email_id": "vijay@gmail.com",
          "Groups": "Family", "DOB": "05/0/2001"},
         {"Firstname": "Abinauv", "Lastname": "mukund", "Phno": 9854268725, "Email_id": "Abinauv@gmail.com",
          "Groups": "Family", "DOB": "09/08/2001"},
         {"Firstname": "isarth", "Lastname": "m", "Phno": 9854268725, "Email_id": "isarth@gmail.com",
          "Groups": "Family", "DOB": "14/07/2001"},
         {"Firstname": "manoj", "Lastname": "kumar", "Phno": 9854268725, "Email_id": "manoj@gmail.com",
          "Groups": "Family", "DOB": "23/06/2001"},
         {"Firstname": "mohamed", "Lastname": "shameer", "Phno": 9854268725, "Email_id": "mohamed@gmail.com",
          "Groups": "Family", "DOB": "19/06/2001"},
         {"Firstname": "thufsil", "Lastname": "ahamed", "Phno": 9854268725, "Email_id": "thufsil@gmail.com",
          "Groups": "Family", "DOB": "08/02/2001"},
         {"Firstname": "hemaraj", "Lastname": "sathish", "Phno": 9854268725, "Email_id": "hemaraj@gmail.com",
          "Groups": "Family", "DOB": "08/04/2001"},
         {"Firstname": "kiruba", "Lastname": "karan", "Phno": 9854268725, "Email_id": "kiruba@gmail.com",
          "Groups": "Family", "DOB": "19/04/2001"},
         {"Firstname": "VIGNESH", "Lastname": "SHIVAN", "Phno": 9854268725, "Email_id": "VIGNESH@gmail.com",
          "Groups": "Family", "DOB": "17/04/2001"},
         {"Firstname": "shivam", "Lastname": "gupta", "Phno": 9854268725, "Email_id": "shivam@gmail.com",
          "Groups": "Family", "DOB": "15/04/2001"},
         {"Firstname": "hakeem", "Lastname": "sofi", "Phno": 9854268725, "Email_id": "hakeem@gmail.com",
          "Groups": "Family", "DOB": "12/04/2001"},
         {"Firstname": "naren", "Lastname": "kumar", "Phno": 9854268725, "Email_id": "naren@gmail.com",
          "Groups": "Family", "DOB": "13/04/1996"},
         {"Firstname": "zara", "Lastname": "khan", "Phno": 9854268725, "Email_id": "zara@gmail.com", "Groups": "Family",
          "DOB": "14/04/1987"},
         {"Firstname": "ajrith", "Lastname": "singh", "Phno": 9854268725, "Email_id": "ajrith@gmail.com",
          "Groups": "Family", "DOB": "15/04/1987"},
         {"Firstname": "kingsley", "Lastname": "k", "Phno": 9854268725, "Email_id": "kingsley@gmail.com",
          "Groups": "Family", "DOB": "26/04/1997"},
         {"Firstname": "ashiq", "Lastname": "mohamed", "Phno": 9854268725, "Email_id": "ashiq@gmail.com",
          "Groups": "Family", "DOB": "29/04/1998"},
         {"Firstname": "vidhya", "Lastname": "k", "Phno": 9854268725, "Email_id": "vidhya@gmail.com",
          "Groups": "Family", "DOB": "30/04/2000"},
         {"Firstname": "rehhana", "Lastname": "f", "Phno": 9854268725, "Email_id": "rehhana@gmail.com",
          "Groups": "Family", "DOB": "23/04/1999"},
         {"Firstname": "deepika", "Lastname": "rithi", "Phno": 9854268725, "Email_id": "deepika@gmail.com",
          "Groups": "Family", "DOB": "13/04/1987"},
         {"Firstname": "rithika", "Lastname": "shajahan", "Phno": 9854268725, "Email_id": "rithika@gmail.com",
          "Groups": "Family", "DOB": "16/04/1997"},
         {"Firstname": "shajahan", "Lastname": "p", "Phno": 9854268725, "Email_id": "shajahan@gmail.com",
          "Groups": "Family", "DOB": "18/04/1996"},
         {"Firstname": "durai", "Lastname": "kumar", "Phno": 9854268725, "Email_id": "durai@gmail.com",
          "Groups": "Family", "DOB": "19/04/1997"},
         {"Firstname": "shivani", "Lastname": "narayanan", "Phno": 6565657687, "Email_id": "shivani@gmail.com",
          "Groups": "Family", "DOB": "08/04/1998"}, ]

for i in phone:
    for j, k in i.items():
        print(f"{j}:{k}")