def check_str(s: str):
    s = s.lower()
    return s == s[::-1]

string = "racecar"
checkstr = check_str(string)
if checkstr:
    print("Palindrome")
else:
    print("Not palindrome")