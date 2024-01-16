def main():
    print(f"Change Owed: {get_owed_change(50)}")

def get_owed_change(money):
    while money > 0:
        print(f"Amount Due: {money}")
        coin = int(input("Insert Coin: "))
        if coin ==25 or coin == 10 or coin == 5:
            money = money - coin
    return abs(money)

main()