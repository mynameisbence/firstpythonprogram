'''Egy olyan program, ami képes egy derékszögű háromszög két megadott oldala
    segítségével kiszámolni a területét, kerületét, beírható és köréírható körét
    illetve természetesen a harmadik ismeretlen oldalát. Ezt a programot a jelentkezéshez
    írtam, mivel nem volt bemutatható kreálmányom, viszont ezelőtt csináltam ilyenhez
    hasonlót ami egy informatikai feladat megoldásához kellett. Azért a python nyelvet
    választottam, mert viszonylag sokat használtam a scratch-et és a két nyelv nagyon
    hasonló, így egyszerűbb dolgom volt ebben írni.'''
from math import *
def pt():
    befogó1 = input("'A' befogó mérete (Ha nincs adat írj 0 át!): ")
    befogó2 = input("'B' befogó mérete (Ha nincs adat írj 0 át!): ")
    a = int(befogó1)
    b = int(befogó2)
    if a and b > 0:
        részmegoldás1 = ((a * a) + (b * b))
        c = sqrt(részmegoldás1)
        print("Az oldalak hossza: ","'A' oldal:",a, sep=" ")
        print("'B' oldal:",b, sep=" ")
        print("'C' oldal:",c, sep=" ")
        print("Szeretnél többet tudni a háromszögedről?")
        válasz = input("(i/n): ")
        if válasz == "i":
            kerület = a + b + c
            külsőkör = c
            s = kerület / 2
            terület = sqrt((s * (s - a) * (s - b) * (s - c)))
            belsőkör = c / 2
            print("A háromszöged kerülete:",kerület, sep=" ")
            print("Területe:",terület, sep=" ")
            print("Köré írható kör sugara:",külsőkör, sep=" ")
            print("Beírható kör sugara:",belsőkör, sep=" ")
        elif válasz == "n":
            print("Ebben az esetben további szép napot kívánok!:)")
    elif a == 0:
        átfogó = input("Mennyi a 'C' átfogó mérete?: ")
        c = int(átfogó)
        a = sqrt(((c * c) - (b * b)))
        print("Az oldalak hossza: ","'A' oldal:",a, sep=" ")
        print("'B' oldal:",b, sep=" ")
        print("'C' oldal:",c, sep=" ")
        print("Szeretnél többet tudni a háromszögedről?")
        válasz = input("(i/n): ")
        if válasz == "i":
            kerület = a + b + c
            külsőkör = c
            s = kerület / 2
            terület = sqrt((s * (s - a) * (s - b) * (s - c)))
            belsőkör = c / 2
            print("A háromszöged kerülete:",kerület, sep=" ")
            print("Területe:",terület, sep=" ")
            print("Köré írható kör sugara:",külsőkör, sep=" ")
            print("Beírható kör sugara:",belsőkör, sep=" ")
        elif válasz == "n":
            print("Ebben az esetben további szép napot kívánok!:)")
    elif b == 0:
        átfogó = input("Mennyi a 'C' átfogó mérete?: ")
        c = int(átfogó)
        b = sqrt(((c * c) - (a * a)))
        print("Az oldalak hossza: ","'A' oldal:",a, sep=" ")
        print("'B' oldal:",b, sep=" ")
        print("'C' oldal:",c, sep=" ")
        print("Szeretnél többet tudni a háromszögedről?")
        válasz = input("(i/n): ")
        if válasz == "i":
            kerület = a + b + c
            külsőkör = c
            s = kerület / 2
            terület = sqrt((s * (s - a) * (s - b) * (s - c)))
            belsőkör = c / 2
            print("A háromszöged kerülete:",kerület, sep=" ")
            print("Területe:",terület, sep=" ")
            print("Köré írható kör sugara:",külsőkör, sep=" ")
            print("Beírható kör sugara:",belsőkör, sep=" ")
        elif válasz == "n":
            print("Ebben az esetben további szép napot kívánok!:)")
            
            
        

    
        
    
        
    
    



    
    

