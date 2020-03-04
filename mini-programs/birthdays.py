birthdays = {'Alice' : 'Apr 1', 'Bob' : 'Dec 12', 'Carol' : 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')

        bday = input()

        # Check input format
        bdayarray = bday.split(" ")
        # bdayarray first argument: month so we need 3 character string
        # first check string
        try:
            bdaymonth = str(bdayarray[0])
        except:
            print("Enter a month! (3 char lenght)")
            continue

        # second check lenght
        if len(bdaymonth) != 3:
            print("Enter a month correctly! (3 char lenght)")
            continue

        # thirth check day integer
        try:
            bdayinteger = int(bdayarray[1])
        except:
            print("Enter a day correctly!")
            continue

        birthdays[name] = bday

        print(name + "'s birthday added to database. (" + bday + ")")
