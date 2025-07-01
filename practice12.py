def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Og'irligingizni kiriting (kg): "))
height = float(input("Bo'yingizni kiriting (metr): "))

bmi = calculate_bmi(weight, height)
status = bmi_status(bmi)

print(f"\n Sizning BMI: {bmi:.2f}")
print(f" Holatingiz: {status}")
