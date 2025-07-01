from random import randint
def check_guess(secret, guess):
    return secret == guess
def print_result(is_correct):
    if is_correct:
        print("tog'ri topdingiz")
    else:
        print("topolmadingiz")
    
def main():
    secret = randint (1, 9)
    guess = int(input("sirli kod: "))
    is_correct = check_guess(secret,guess)
    print_result (is_correct)

main()