customer_basket_cost = 101
customer_basket_weight = 1

def calcs():
    if customer_basket_cost >= 100:
        print("El coste total es de ", customer_basket_cost)
    else:
        price = customer_basket_cost * (customer_basket_weight * 1.2)
        print("El precio total es de ", price)

if __name__ == "__main__":
    calcs()