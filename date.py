months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date=input("Date: ")
        if "/" in date:
            month,day,year=date.split("/")
        
        elif "," in date:
            month_day, year = date.split(",")
            month, day = month_day.split(" ")  
            month = months.index(month) + 1
        
        else:
            continue
                
    except ValueError:
        continue    
        
    
    print(f"{int(month):02d}-{int(day):02d}-{year}")    
    break       