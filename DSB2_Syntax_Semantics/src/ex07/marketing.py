import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
'elon@paypal.com', 'jessica@gmail.com']

participants = ['walter@heisenberg.com', 'vasily@mail.ru',
'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']

recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

def clients_set():
    return set(clients)

def participants_set():
    return set(participants)

def recipients_set():
    return set(recipients)

def call_center():
    return clients_set() - recipients_set()

def potential_clients():
    return participants_set() - clients_set()

def loyalty_program():
    return clients_set() - participants_set()

if len(sys.argv) != 2:
    sys.exit()

task = sys.argv[1]

if task == 'call_center':
    result = call_center()
elif task == 'potential_clients':
    result = potential_clients()
elif task == 'loyalty_program':
    result = loyalty_program()
else:
    raise Exception("Invalid task name")

for email in result:
    print(email)
