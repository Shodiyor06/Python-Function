def is_palindrome(text: str) -> bool:
    text = text.lower().strip()
    return text == text[::-1]

soz = input("Soz kiriting: ")
if is_palindrome(soz):
    print(" Bu soz palindrom.")
else:
    print(" Bu soz palindrom emas.")
