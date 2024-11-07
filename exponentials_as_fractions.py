def test(number, length):
    if number <= 10**length:
        return True

def ggt(a, b):
    if b==0:
        return a
    else:
        return ggt(b, a%b)

def expand(x, digits):
    denominator = 1
    numerator = 1
    counter = 1
    # first commit
    vwfwv=8
    
    while True: 
        denominator = denominator*counter
        denominator += x**counter
        numerator = numerator*counter
        counter +=1
        
        ggt = lambda a,b: a if b==0 else ggt(b, a%b)
        fac1 = ggt(denominator, numerator)
        fac2 = ggt(denominator*counter+x**counter, numerator*counter)
        if (denominator*counter+x**counter)/fac2 >= 10**(digits):
            break
    
    return [int(denominator/fac1), int(numerator/fac1), denominator/numerator]

if __name__ == '__main__':

    print(expand(1,2))
    print(expand(2, 5))
    print(expand(3, 10))
        
