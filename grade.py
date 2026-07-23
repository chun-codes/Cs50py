def main():
    while True:
        try:
            frac=input("Fraction: ")
            print(gauge(convert(frac)))
        except (ValueError,ZeroDivisionError,TypeError):
            continue
        break
def convert(fraction):
    strx,stry=fraction.split("/")
    x=int(strx)
    y=int(stry)
    perc=round((x/y)*100)
    return perc

def gauge(percentage):
    if percentage<=1:
        return 'E'
    elif percentage>=99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()