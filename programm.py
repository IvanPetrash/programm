a= int(input('chose the mode: 1 or 2'))
if a==1:
    text=str(input("Enter text: "))
    print(text)
    n = sorted(text.split())
    print(n)
if a==2:
    word = str(input("Enter text: "))
    d={}
    for char in set(word):
        d[char]=word.count(char)
    print(d)
    
