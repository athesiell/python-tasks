def replacer(s: str) -> str:
    conversion = s.maketrans({'"':"'","'":'"'})
    return s.translate(conversion)

print(replacer("'test' it or test \"this\""))