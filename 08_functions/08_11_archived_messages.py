# Uses the function to move items from one list to another while printing them but makes a copy of the original list so it is unchanged

def send_messages(messages, sent_messages):
    """Moves messages to sent messages while printing them each time"""
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)



messages = ['Hi', 'How are you?', 'I love Python']
sent_messages = []

print("Messages to be sent:")
print(messages)

send_messages(messages[:], sent_messages)

print("Sent messages:")
print(sent_messages)

print("Original list:")
print(messages)