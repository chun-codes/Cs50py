def main():
    word=input("Put a word to see if it's a palindrome: ").lower()
    if palindrome(word):
        print("Valid")
    else:
        print("Invalid")
def palindrome(w):
    left=0
    right=len(w)-1
    while left<right:
        if not w[left]==w[right]:
            return False
        elif w[left]==w[right]:
            left+=1
            right-=1
    return True
if __name__=="__main__":
    main()