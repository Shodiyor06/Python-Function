def qushish(a, b):
    resalt=a+b
    return resalt
def ayirish(a, b):
    resalt=a-b
    return resalt
def bulish(a, b):
    resalt=a/b
    return resalt
def kupaytirish(a, b):
    resalt=a*b
    return resalt

def main():
    a=float(input("son1: "))
    b=float(input("son2: "))
    op=input("amal(+,-,*,/): ")

    if op == "+":
        resalt=a+b
        print(resalt)
    elif op == "-":
        resalt=a-b
        print(resalt)
    elif op == "*":
        resalt=a*b
        print(resalt)
    elif op == "/":
        resalt=a/b
        print(resalt)
main()
