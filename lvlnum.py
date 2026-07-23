from random import randint
import sys

def positive(n):
    while True:
            try:
                if n>0:
                    return n
            except ValueError:
                continue
            
def main():
    level=positive(int(input("Level: ")))
    number=randint(1,level)
    while True:
        try:
            guess=int(input("Guess: "))
            if guess>number:
                print("Too big")
            elif guess<number:
                print("Too small")
            else:
                print("Correct!")
                exit()
        except (ValueError,EOFError):
            continue
            
            
main()