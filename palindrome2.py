def main():
    word=input("Put a word to see if it's a palindrome: ").lower()
    if palindrome(word):
        print("Valid")
    else:
        print('Invalid')
def palindrome(w):
    for i in range(len(w)//2):
        if w[i]!=w[-(i+1)]:
            return False
    return True
if __name__=="__main__":
    main()