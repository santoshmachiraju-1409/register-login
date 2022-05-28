import re
pattern="[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
pattern1="^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A_Z])(?=.*[!@#$%^&*()_+=].*$)"
def register():
    db=open("database.txt","r")
    username=input("enter username:")
    if(re.search(pattern,username)):
        print("valid email")
    else:
        print("invalid email")
        register()
    password=input("enter password:")
    password1=input("re-enter password:")
    result=re.findall(pattern1,password)
    result1=re.findall(pattern1,password1)
    if result==result1:
        print("password is valid")
    else:
        print("Invalid password")
        register()
    d=[]
    f=[]
    for i in db:
        a,b=i.split(",")
        b=b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    if password!=password1:
        print("invalid password,password dosn't match.restart:")
    elif username in d:
        print("username exists")
    else:
        db=open("database.txt","a")
        db.write(username+","+password+"\n")
        print("successfully registered")

def access():
    db=open("database.txt","r")
    username =input("enter your Username:")
    password =input("enter your password:")
    if not len(username or password)<1:
        d=[]
        f=[]
        for i in db:
            a,b=i.split(",")
            b=b.strip()
            d.append(a)
            f.append(b)
        data =dict(zip(d,f))
        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("sucessfully logged in")
                        print("hi,",username)
                    else:
                        print("password or username incorrect")
                except:
                    print("incorrect passpwrd or username")
            else:
                print("username doesn't exists")
        except:
            print("username or password doen't exisit")
    else:
        print("Please enter a value")

def home(option=None):
    option=input("login|register:")
    if option == "login":
        access()
    elif option == "register":
        register()
    else:
        print("please enter an option")
home()


