places = ["seoul", "tokyo", "sydney", "paris", "london"]

print("Original list:")
print(places)

print("Alphabetical order:")
print(sorted(places))

print("Original list:")
print(places)

print("Reverse alphabetical order:")
print(sorted(places, reverse=True))

print("Original list:")
print(places)

print("Reversed:")
places.reverse()
print(places)

places.reverse()
print("Reversed again:")
print(places)

places.sort()
print("Alphabetical:")
print(places)

places.sort(reverse=True)
print("Reverse alphabetical:")
print(places)