investment_in_btc = 1

def bitcoinToEuros(bitcoin_amount, valor_bitcoin_euros):
    return bitcoin_amount * valor_bitcoin_euros



if __name__ == "__main__":
    if bitcoinToEuros(investment_in_btc, 25000) < 30000:
        print("Eres pobre")
    else:
        print("Vas bien")