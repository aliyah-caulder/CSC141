# Aliyah Caulder
# 9/13/24
# challenge for lab 6

print()
print("-----------------------")
print("Calculate average score")
print("-----------------------")

num = int(input("\nHow many scores would you like to average? >"))

scores = []

for i in range(0, num):
    score = int(input("\nEnter a score: "))
    scores.append(score)

average = sum(scores) / len(scores)

print(f"\nYour average score is {average} points.")
print()