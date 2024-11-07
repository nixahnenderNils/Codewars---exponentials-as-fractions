def expand(x, digits):
    denominator = 1
    numerator = 1
    counter = 1
    
    fac = lambda a: 1 if a <= 1 else a*fac(a-1)
    ggt = lambda a,b: a if b==0 else ggt(b, a%b)

    while True: 
        numerator=(x**counter*denominator+numerator*fac(counter))
        denominator=denominator*fac(counter)
        divider=ggt(numerator, denominator)
        numerator=numerator/divider
        denominator=denominator/divider
        if len(str(int(numerator))) >=digits:
             break
        counter+=1
        
    return [int(numerator), int(denominator), numerator/denominator]

if __name__ == '__main__':

    print(expand(1,2))
    print(expand(2, 5))
    print(expand(3, 10))
    print(expand(1.5,10))
        
