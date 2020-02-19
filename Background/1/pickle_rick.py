import pickle
import base64 as b64
menu = ""
userDict = {"userName": 'guest',"info":"guest","admin": 0,"points":0}
print( """
        Options:
	info: Get user info
	flag: Get flag and win this.
	register: Set your details
	save: Save your details for later use
	load: Load your save data
	points: Check points
	\n""")
while (menu != "exit"):
        menu = input("Enter option: \n")
        if (menu == "info"):
                print(userDict["userName"],userDict["info"])
        elif ( menu == "flag"):
                if not userDict["admin"]:
                        print("Go away, you have no privileges\n")
                else:
                        print("CRsCTF{P1CLKL3_R1CK_45ABD}\n")
        elif (menu == "register"):
                userDict["userName"] = input("Enter User name\n")
                userDict["info"] = input("Enter info: \n")
        elif (menu == "save"):
                print(b64.b64encode(pickle.dumps(userDict)).decode())
        elif (menu == "load"):
                d = pickle.loads(b64.b64decode(input("Enter data signature: \n").encode('utf-8')))
                if (type(d) == type({})):
                        userDict = d
                        print("Data signature accepted\n")
                else:
                        print("Invalid data\n")


