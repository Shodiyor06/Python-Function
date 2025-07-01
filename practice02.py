def yosh_hisoblash(t_yil, h_yil):
    result=h_yil-t_yil
    return result

t_yil=int(input("tug'ilgan yilingiz: "))
h_yil=int(input("hozirgi yil: "))

resalt=yosh_hisoblash(t_yil,h_yil)
if resalt >=18:
    print("siz voyaga yetgansiz")
else:
    print("siz voyaga yetmagansiz")
print(resalt)