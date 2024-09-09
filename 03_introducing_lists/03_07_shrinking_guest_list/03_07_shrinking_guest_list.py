guest_list = ["Bangchan", "Hyunjin", "Felix"]

print(f"\n{guest_list[0]}, it would be an honor for you to join me to dinner tonight.")

print(f"\nHello {guest_list[1]}, would you be so kind as to join me to dinner tonight?")

print(f"\nIt would be an honor for you to join my dinner party tonight, {guest_list[2]}.")

# I chose to use the pop() function to be able to print a statement after I remove the guest

cant_make_it = guest_list.pop(0)

print(f"\n{cant_make_it} can't make it...")

guest_list.insert(0, "Han")

print(f"\n{guest_list[0]}, it would be an honor for you to join me to dinner tonight.")

print(f"\nHello {guest_list[1]}, would you be so kind as to join me to dinner tonight?")

print(f"\nIt would be an honor for you to join my dinner party tonight, {guest_list[2]}.")

print("\nI have found a bigger table for the dinner party!")

guest_list.insert(0, "Changbin")
guest_list.insert(2, "Seungmin")
guest_list.append("Lee Know")

print(f"\n{guest_list[0]}, it would be an honor for you to join me to dinner tonight.")

print(f"\nHello {guest_list[1]}, would you be so kind as to join me to dinner tonight?")

print(f"\nIt would be an honor for you to join my dinner party tonight, {guest_list[2]}.")

print(f"\n{guest_list[3]}, it would be an honor for you to join me to dinner tonight.")

print(f"\nHello {guest_list[4]}, would you be so kind as to join me to dinner tonight?")

print(f"\nIt would be an honor for you to join my dinner party tonight, {guest_list[5]}.")

print("\nTurns out the table won't arrive in time and I can only invite two people for dinner...")

uninvited = guest_list.pop()
print(f"\nSorry, {uninvited}, I dont have enough space at my table and have to uninvite you from the dinner party...")
uninvited = guest_list.pop()
print(f"\nSorry, {uninvited}, I dont have enough space at my table and have to uninvite you from the dinner party...")
uninvited = guest_list.pop()
print(f"\nSorry, {uninvited}, I dont have enough space at my table and have to uninvite you from the dinner party...")
uninvited = guest_list.pop()
print(f"\nSorry, {uninvited}, I dont have enough space at my table and have to uninvite you from the dinner party...")

print(f"\nDon't worry, {guest_list[0]}, you're still invited to my dinner party!")
print(f"\nDon't worry, {guest_list[1]}, you're still invited to my dinner party!")

del guest_list[1]
del guest_list[0]

print(guest_list)