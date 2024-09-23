current_users = ['Jonathan','Mary','Jesus',
                 'Murphy', 'Eric','Mark']
new_users = ['Lucca','JONATHAN', 
             'eRic', 'Faye', 'Quinn']
lowercase_currents = []
for user in current_users:
    lowercase_currents.append(user.lower())

for new_user in new_users:
    if new_user.lower() in lowercase_currents:
        print("this username has already been taken")
    else:
        print('this username is available')

