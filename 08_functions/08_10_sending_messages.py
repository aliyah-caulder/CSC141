# defines a function to move messages from one list to another while printing them.

def send_messages(messages, sent_messages):
    """Moves messages to sent messages while printing them each time"""
    print("Messages to be sent:")
    print(messages)
    print()
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)
    print()
    print("Messages sent:")
    print(sent_messages)



messages = ['Hi', 'How are you?', 'I love Python']
sent_messages = []

send_messages(messages, sent_messages)