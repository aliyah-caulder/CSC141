languages = ["english", "korean", "french", "russian", "spanish"]

print(f"\nMy first language is {languages[0].title()}.")

print(f"\nI either know or am learning {len(languages)} languages.")
print(languages)

print("\nI also want to learn Arabic")
languages.append("arabic")
print(languages)

print("\nLet's put it in a different spot in the list.")
popped = languages.pop()
languages.insert(1, popped)
print(languages)

print("\nI'm already fluent in English, so let's take that out of the list.")
del languages[0]
print(languages)

print("\nI never liked Spanish, so let's take that out too.")
languages.remove("spanish")
print(languages)

print("\nLet's order them into alphabetical order.")
print(sorted(languages))

print("\nNow reverse alphabetical order.")
print(sorted(languages, reverse=True))

print("\nNow back to normal.")
print(languages)

print("\nNow let's reverse them.")
languages.reverse()
print(languages)

print("\nNow let's reverse them again to get back to normal.")
languages.reverse()
print(languages)

print("\nNow let's permanently sort them alphabetically so I can say I used every function.")
languages.sort()
print(languages)

print("\nMight as well do reverse alphabetical too.")
languages.sort(reverse=True)
print(languages)

print("\nOK that's all, bye.")