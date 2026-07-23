from random import randint
import sys

def main():
    level=get_level()
    score=0
    for _ in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        for _ in range(3):
                try:
                    
                    answer=int(input(f"{x}+{y}= "))
                    if answer==x+y:
                        score+=1
                        break
                    elif answer!=x+y:
                        print("EEE")
                        score+=0
                        continue 

                except (ValueError,EOFError):
                    continue
        else:
            print(f"{x}+{y}={x+y}")              
    print(f"Score:{score}")                
                

def get_level():
    while True:
        try:
            lvl=int(input("Level: "))
            if lvl in [1,2,3]:
                return lvl
            else:
                continue
        except ValueError:
                continue
                


def generate_integer(level):
    if level==1:
        return (randint(0,9))
    elif level==2:
        return (randint(10,99))
    elif level==3:
        return (randint(100,999))
    else:
        sys.exit()       


if __name__ == "__main__":
    main()