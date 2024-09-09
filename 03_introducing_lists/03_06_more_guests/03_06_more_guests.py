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