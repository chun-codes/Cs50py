
    
while True:
    try:
        n=input("Fraction: ")
        number=n.split("/")
        x=int(number[0])
        y=int(number[1])
        divide=x/y
        if x>y:
            continue
    except (ValueError, ZeroDivisionError):
        continue  
            
    percentage=round(divide*100)
    if percentage <= 1:
        print("E") 
    elif percentage >= 99:
        print("F")       
    else:
        print(f"{percentage}%")     