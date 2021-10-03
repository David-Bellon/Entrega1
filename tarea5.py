import abc


money = 2000
hungry = True
icecream_price = 100
percentage = 19

if money > icecream_price and hungry == True:
    percentage += 20
    icecream_price += (icecream_price * 0.2)
    
if percentage >= 85:
    hungry = False

print("Tu porcentaje de comida es:", percentage)
if hungry:
    print("Tienes hambre")