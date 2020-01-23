print('Welcome to Smart Stay'.center(200))
input('Choose an Option:\n1.Log in\n2.Create an account\n3.Use as Guest')
option=int(input('>>'))
if option==1:
    usr_name=input("User Name:")
    try:
        if input('Password')==(open(usr_name,'r').readline()):
            pass
        else:
            print('Incorrect Password')
    except:
        print('User Name don\'t exit.' )
if option==2:
    user_name= input('User Name:')
    file = open(user_name, 'w+')
    password = input('Password:')

    name=input('First Name:')
    name1=input('Middle Name:')
    name2=input('Last Name:')

    address=input('Address:')

    phone_number=input('Phone Number')

    id=input('Identification Number')

    email=input('Email address:')
    if file.readline(1)!=email:
        file.writelines(password+'\n')
        file.writelines(email+'\n')
        file.writelines(name + ' ' + name1 + ' ' + name2+'\n')
        file.writelines(address+'\n')
        file.writelines(phone_number+"\n")
        file.writelines(id+'\n')

if option==3:
    input('First Name')
    input('Middle Name')
    input('Last Name')
    input('Country')
    input('Contact Information')





