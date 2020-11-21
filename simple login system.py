def getUserdata(filename):
    usernames = [] # create a list
    passwords = []
    f = open(filename,"r")
    for line in f: # loop each line through a file
        data_1 = line.strip('\n')
        data_2 = data_1.split('\t') # split each line into two lists
        usernames.append(data_2[0]) # append the first list to usernames
        passwords.append(data_2[1]) # append the second list to passwords
    f.close
    return usernames,passwords

def exists(username,filename):
    user = getUserdata(filename)
    result = username in user[0]  # determine whether the input username if in the list
    return result

def createUser(username,password,filename):
    var_1 = exists(username,filename) # determine if username exist in the file
    if var_1 == False:
        f = open(filename,"a")
        f.write(str(username)+ '\t' + str(password) + '\n') # write the username and the password in strings with a tab and a newline
        return True
    else:
        return False

def login(username,password,filename):
    var_2 = exists(username,filename)
    if var_2 == True:
        user = getUserdata(filename)[0]
        i1 = user.index(username) # get the index of the username and the corresponding location of password in the file
        correctpassword = getUserdata(filename)[1] # get the password list
        if password == correctpassword[i1]: # with known index in the password list then determine whether the password is correct
            return True
        else:
            return False
    else:
        return False
    
def main():

    database = "database.txt"
    while True:
        ans = input("Press [q] to quit, [l] to login, [c] to create an account: ")
        if ans == "q":
            # Break if the user quits
            break
        elif ans == "l":
            # Login if the user types in "l"
            uname = input("Please enter your username: ")
            password = input("Please enter your password: ")
            if login(uname, password, database):
                print("Login sucessful!\n")
            else:
                print("Sorry, login unsucessful :(\n")
        elif ans == "c":
            # Create an account if the user types in c
            uname = input("Please create a username: ")
            password = input("Please create a password: ")
            # Check if username exists
            if createUser(uname, password, database):
                    print("Account creation sucessful for user,",uname,"\n")
            else:
                    print("Sorry,",uname,"is already taken!\n")
        else:
            print("Please enter a valid character")
main()

