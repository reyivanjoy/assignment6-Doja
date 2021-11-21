# Program 1 - Number Sorter
a = float(input("Input 1st Number: "))
b = float(input("Input 2nd Number: "))
c = float(input("Input 3rd Number: "))
d = float(input("Input 4th Number: "))
if a < b:
    if b < c:
        if c < d:
            print(d,c,b,a)
        else:
            if a < b:
                if b < d:
                    if d < c:
                        print(c,d,b,a) 
if a < c:
    if c < b:
        if b < d:
            print(d,b,c,a)
        else:
            if a < d:
                if d < c:
                    if c < b:
                        print(b,c,d,a)
if a < d:
    if d < b:
        if b < c:
            print(c,b,d,a)           
if b < a:
    if a < c:
        if c < d:
            print(d,c,a,b)
        else:
            if b < a:
                if a < d:
                    if d < c:
                        print(c,d,a,b)
if b < c:
    if c < a:
        if a < d:
            print(d,a,c,b)
        else:
            if b < c:
                if c < d:
                    if d < a:
                        print(a,d,b,c)
if b < d:
    if d < a:
        if a < c:
            print(c,a,d,b)
        else:
            if b < d:
                if d < c:
                    if c < a:
                        print(a,c,d,b)
if c < a:
    if a < b:
        if b < d:
            print(d,b,a,c)
        else:
            if c < a:
                if a < d:
                    if d < b:
                        print(b,d,a,c)
if c < b:
    if b < a:
        if a < d:
            print(d,a,b,c)
        else:
            if c < b:
                if b < d:
                    if d < a:
                        print(a,d,b,c)
if c < d:
    if d < a:
        if a < b:
            print(b,a,d,c)
        else:
            if c < d:
                if d < b:
                    if b < a:
                        print(a,b,d,c)
if d < a:
    if a < b:
        if b < c:
            print(c,b,a,d)
        else:
            if d < a:
                if a < c:
                    if c < b:
                        print(b,c,a,d)
if d < b:
    if b < a:
        if a < c:
            print(c,a,b,d)
        else:
            if d < b:
                if b < c:
                    if c < a:
                        print(a,c,b,d)
if d < c:
    if c < a:
        if a < b:
            print(b,a,c,d)
        else:
            if d < c:
                if c < b:
                    if b < a:
                        print(a,b,c,d)
if a == b:
    if a <= c:
        if c <= d:
            print(d,c,b,a)
        else:
            if d <= c:
                print(c,d,b,a)
    else:     
        if a == b:
            if c <= a:
                if a <= d:
                    print(d,b,a,c)
                else:
                    if d <= c:
                        print(b,a,c,d)         
if a == c:
    if a <= b:
        if b < d:
            print(d,b,c,a)
        else:
            if d < b:
                print(b,d,c,a)
    else:
        if a == c:
            if b <= a:
                if a <= d:
                    print(d,c,a,b)
                else:
                    if d <= b:
                        print(c,a,b,d)
if a == d:
    if a < b:
        if b < c:
            print(c,b,d,a,)
        else:
            if c < b:
                print(b,d,a,c)
    else:
        if b <= a:
            if a <= c:
                print(c,d,a,b)
            else:
                if c <= b:
                    print(d,a,b,c)
if b == c:
    if b <= a:
        if a < d:
            print(d,a,c,b)
        else:
            if d < a:
                print(a,d,c,b)
    else:
        if a <= b:
            if b <= d:
                print(d,c,b,a)
            else:
                if d <= a:
                    print(c,b,a,d)
if b == d:
    if b <= c:
        if c < a:
            print(a,c,d,b)
        else:
            if a < c:
                print (c,a,d,b)
    else:
        if c <= b:
            if b < a:
                print(a,d,b,c)
            else:
                if a < c:
                    print(d,b,c,a)
if c == d:
    if c < b:
        if b < a:
            print(a,b,d,c)
        else:
            if a < b:
                print(b,a,d,c)
    else:
        if b <= c:
            if c <= a:
                print(a,d,c,b)
            else:
                if a < b:
                    print(d,c,b,a)