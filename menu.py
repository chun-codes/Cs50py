foods={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total=0
while True:
    try:
        item=input("Item: ").title()
        if item == "":
            break    
        price=foods[item]    
        total=total+price
        print(f"Total: ${total:.2f}")             
    except EOFError:
        break
    except KeyError:
        continue    
 
       
             
                   
# Taqueria - what I learned

# 1. Running total pattern:
#    total = 0
#    total = total + new_value
#    print total immediately after updating

# 2. Dictionary lookup:
#    menu[item] gives the price

# 3. Loop until empty input:
#    if item == "": break

# 4. Two different errors, two different responses:
#    EOFError → break (user is done)
#    KeyError → continue (bad item, ask again)                               