def expand(x, digits):
    denominator = 1
    numerator = 1
    counter = 1
    
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
    
    return [int(denominator/fac1), int(numerator/fac1)]
