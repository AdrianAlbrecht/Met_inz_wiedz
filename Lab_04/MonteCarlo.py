import random as rand

def montecarlo(foo,foo2, fx, lx, eps):
    oryginal = foo2(lx)-foo2(fx)
    wyliczone = 0
    punkty = 1000
    ile = 0
    minimum, maximum = foo(fx), foo(lx)
    wylosowane=[]
    ile=0
    # print(minimum,maximum)
    while(abs(wyliczone-oryginal)>eps):
        punkty+=1000
        for i in range(1000):
            newx = rand.uniform(fx,lx)
            newy = rand.uniform(minimum, maximum)
            while((newx,newy) in wylosowane):
                newx = rand.uniform(fx,lx)
                newy = rand.uniform(minimum, maximum)
            wylosowane.append((newx,newy))
            
            wynik = foo(newx)
            if(newy<=wynik):
                ile+=1
        wyliczone = (lx-fx)*(maximum-minimum)*(ile/punkty)
        print("Wyliczenie niedokładne z dokładnocią: {3}! Dla ilosci {0} punktów:{1}. Rzeczywiste: {2}".format(punkty,wyliczone,oryginal,eps))
    return wyliczone

def f2(x):
    return x**2/2

def f(x):
    return x

#aproksymacją dolną
def prostokaty(foo,foo2, fx, lx, eps):
    oryginal = foo2(lx)-foo2(fx)
    wyliczone = 0
    dzielnik = 1
    odleglosc = 1
    while(abs(wyliczone-oryginal)>eps):
        wyliczone = 0
        dzielnik*=2
        odleglosc = float(lx-fx)/float(dzielnik)
        for i in range(dzielnik):
            wyliczone+= foo(fx+odleglosc*i)*odleglosc
        print("Wyliczenie niedokładne z dokładnocią: {3}! Dla ilosci {0} prostokatow:{1}. Rzeczywiste: {2}".format(dzielnik,wyliczone,oryginal,eps))
    return wyliczone

#aproksymacją górną
def prostokaty2(foo,foo2, fx, lx, eps):
    oryginal = foo2(lx)-foo2(fx)
    wyliczone = 0
    dzielnik = 1
    odleglosc = 1
    while(abs(wyliczone-oryginal)>eps):
        wyliczone = 0
        dzielnik*=2
        odleglosc = float(lx-fx)/float(dzielnik)
        for i in range(1,dzielnik+1):
            wyliczone+= foo(fx+odleglosc*i)*odleglosc
        print("Wyliczenie niedokładne z dokładnocią: {3}! Dla ilosci {0} prostokatow:{1}. Rzeczywiste: {2}".format(dzielnik,wyliczone,oryginal,eps))
    return wyliczone

#aproksymacją srednia
def prostokaty3(foo,foo2, fx, lx, eps):
    oryginal = foo2(lx)-foo2(fx)
    wyliczone = 0
    dolna = 0
    gorna = 0
    dzielnik = 1
    odleglosc = 1
    while(abs(wyliczone-oryginal)>eps):
        wyliczone = 0
        dzielnik*=2
        odleglosc = float(lx-fx)/float(dzielnik)
        for i in range(1,dzielnik+1):
            dolna = foo(fx+odleglosc*(i-1))*odleglosc
            gorna = foo(fx+odleglosc*i)*odleglosc
            wyliczone+= (dolna+gorna)/2
        print("Wyliczenie niedokładne z dokładnocią: {3}! Dla ilosci {0} prostokatow:{1}. Rzeczywiste: {2}".format(dzielnik,wyliczone,oryginal,eps))
    return wyliczone
        
        
        
print(montecarlo(f,f2, 0, 1, 0.05))  ###zakomentowane bo długo trwa (może co nie tak działa???)
print(prostokaty(f,f2, 0, 1, 0.01))
print(prostokaty2(f,f2, 0, 1, 0.01))
print(prostokaty3(f,f2, 0, 1, 0.01))
