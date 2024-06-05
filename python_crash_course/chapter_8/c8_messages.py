messages = [
    'Hi who are you?',
    'Hi my name is something',
    'Where do you live and why',
    'I live wherever i want',
    ]

def show_messages(messages: list[str]) -> None: 
    if messages:
        for message in messages:
            print(message)
    else:
        print("---List empty---")

def send_messages(incoming_messages: list[str], sent_messages: list[str]) -> None:
    while incoming_messages:
        message = incoming_messages.pop(0)
        print(message)
        sent_messages.append(message)

    
sent_messages = []
send_messages(messages[:], sent_messages)
print('--Original--')
show_messages(messages)
print('--Archived--')
show_messages(sent_messages)