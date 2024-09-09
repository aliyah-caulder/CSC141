#practice file for chapter 3
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.insert(0, "ducati")
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n{too_expensive.title()} is too expensive for me.")