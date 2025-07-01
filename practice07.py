def ask_question(question, correct_answer):
    user_answer = input(question + "\n>>> ")
    return check_answer(user_answer, correct_answer)

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()

score = 0
if ask_question("O'zbekiston poytaxti qaysi shahar?", "Toshkent"):
    print(" To'g'ri!")
    score += 1
else:
    print(" Noto'g'ri. To'g'ri javob: Toshkent")

if ask_question("Python dasturlash tilini yaratuvchisi kim?", "Guido van Rossum"):
    print(" To'g'ri!")
    score += 1
else:
    print(" Noto'g'ri. To'g'ri javob: Guido van Rossum")

print(f"\nSizning umumiy baliyingiz: {score}/2")
