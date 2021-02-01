email=input("Enter your mail:")

data = email.split("@")

if len(data) != 2:
    print('Mail address is invalid.')
else:
    result="User Name is  {} and the Domain is {}".format(data[0],data[1])
    print(result)
