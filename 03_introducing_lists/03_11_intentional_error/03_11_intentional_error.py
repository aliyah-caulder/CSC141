# this code produces an index error

names = ["jillian", "rhiley", "kassia", "luke"]

message = f"Hello, {names[1].title()}, I hope you're doing well."
print(message)
message = f"Hello, {names[2].title()}, I hope you're doing well."
print(message)
message = f"Hello, {names[3].title()}, I hope you're doing well."
print(message)
message = f"Hello, {names[4].title()}, I hope you're doing well."
print(message)

# this can be fixed by changing all indeces by -1, since python starts counting at zero.