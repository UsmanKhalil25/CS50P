def main():
    tweet = input("Input: ")
    print(f"Output: {remove_vowels(tweet)}")

def remove_vowels(word):
    ans = ""
    vowels = ["A","a","E","e","I","i","O","o","U","u"]
    for char in word:
        if char not in vowels:
            ans+=char
    return ans

main()