def machine():
    available = [25, 10, 5]
    coins = 50
    while True:
        print(f"Amount Due: {coins}")
        insert = int(input("Insert Coins: "))
        if insert not in available:
            continue
        coins = coins - insert
        if coins <= 0:
            coins = abs(coins)
            print(f"Change Owed: {coins}")
            break

machine()