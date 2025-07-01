def deposit(balance, miqdor):
    if miqdor > 0:
        balance += miqdor
        print(f" {miqdor} so'm depozit qilindi.")
    else:
        print(" Noto'g'ri miqdor.")
    return balance

def withdraw(balance, miqdor):
    if miqdor > 0 and miqdor <= balance:
        balance -= miqdor
        print(f" {miqdor} so'm yechildi.")
    elif miqdor > balance:
        print(" Hisobda yetarli mablag' yo'q.")
    else:
        print(" Noto'g'ri miqdor.")
    return balance

def check_balance(balance):
    print(f" Joriy balans: {balance} so'm")

def main():
    balance = 1000.0 
    while True:
        print("\n>>> Amalni tanlang: deposit / withdraw / check / exit")
        action = input(">>> ").lower()
    
        if action == "deposit":
            miqdor = float(input("Qancha mablag' qoshmoqchisiz? "))
            balance = deposit(balance, miqdor)
    
        elif action == "withdraw":
            miqdor = float(input("Qancha mablag' yechmoqchisiz? "))
            balance = withdraw(balance, miqdor)
    
        elif action == "check":
            check_balance(balance)
    
        elif action == "exit":
            print(" Dastur tugadi. Xayr!")
            break
    
        else:
            print(" Noto'g'ri amal kiritildi.")

main()