#practice for chapter 2
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJava")

favorite_language = "python "
favorite_language = favorite_language.strip()

nostarch_url = "https://nostarch.com"
simple_url = nostarch_url.removeprefix("https://")
print(simple_url)