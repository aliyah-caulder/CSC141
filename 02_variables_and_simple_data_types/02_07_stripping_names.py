# for this code, I decided to add all the stripped names into one f string so I could use the \t and \n functions.
name = "      Aliyah      "
print(name)
message = f"\t{name.lstrip()}\n\t{name.rstrip()}\n\t{name.strip()}"
print(message)