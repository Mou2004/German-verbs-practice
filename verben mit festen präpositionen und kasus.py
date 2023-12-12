
import random
import time

print("Hello, I'm here for the test ;-) ")
print("You just need to type the preposition and a -->accusative and d -->dative.")

prev_f = None
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27]
while numbers:
    f = random.choice(numbers)
    if f != prev_f:
        numbers.remove(f)
        prev_f = f

        s = str(f)
        if s == "1":
            print("Achten:- ")
            a1 = input()
            x1 = a1.lower()
            y1 = "auf"
            if x1 != y1:
                print(a1 + ' is not a suitable preposition ')
                print("The correct answer is " + y1)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c1 = input()
                z1 = c1.lower()
                k1 = "a"
                if z1 != k1:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")
        elif s == "2":
            print("Sich ärgern :- ")
            a2 = input()
            x2 = a2.lower()
            y2 = "über"
            if x2 not in y2:
                print(a2 + ' is not a suitable preposition ')
                print("The correct answer is " + y2)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c2 = input()
                z2 = c2.lower()
                k2 = "a"
                if z2 != k2:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")

        elif s == "3":
            print("sich beschweren :- ")
            a3 = input()
            x3 = a3.lower()
            y3 = ["über", "uber", "bei"]
            if x3 not in y3:
                print(a3 + ' is not a suitable preposition ')
                print("The correct answer is " + ','.join(y3))
            else:
                print("Great, you're doing good!")
                print("bei is dativ and uber is akkusativ.")

        elif s == "4":
            print("denken :- ")
            a4 = input()
            x4 = a4.lower()
            y4 = "an"
            if x4 != y4:
                print(a4 + ' is not a suitable preposition ')
                print("The correct answer is " + y4)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c4 = input()
                z4 = c4.lower()
                k4 = "a"
                if z4 != k4:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")
        elif s == "5":
            print("diskutieren :- ")
            a5 = input()
            x5 = a5.lower()
            y5 = ["über", "mit"]
            if x5 not in y5:
                print(a5 + ' is not a suitable preposition ')
                print("The correct answer is " + ','.join(y5))
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c5 = input()
                z5 = c5.lower()
                k5 = "a"
                if z5 != k5:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")
        elif s == "6":
            print("sich entschuldigen :- ")
            a6 = input()
            x6 = a6.lower()
            y6 = ["fur", "für", "bei"]
            if x6 not in y6:
                print(a6 + ' is not a suitable preposition ')
                print("The correct answer is " + ','.join(y6))
            else:
                print("Great, you're doing good!")
                print("für -->a   bei--> d.")
        elif s == "7":
            print("sich erinnern :- ")
            a7 = input()
            x7 = a7.lower()
            y7 = "an"
            if x7 != y7:
                print(a7 + ' is not a suitable preposition ')
                print("The correct answer is " + y7)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c7 = input()
                z7 = c7.lower()
                k7 = "a"
                if z7 != k7:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")
        elif s == "8":
            print("sich freuen :- ")
            a8 = input()
            x8 = a8.lower()
            y8 = ["auf", " über"]
            if x8 not in y8:
                print(a8 + ' is not a suitable preposition ')
                print("The correct answer is " + ','.join(y8))
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c8 = input()
                z8 = c8.lower()
                k8 = "a"
                if z8 != k8:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")
        elif s == "9":
            print("sich konzentrieren :- ")
            a9 = input()
            x9 = a9.lower()
            y9 = "auf"
            if x9 != y9:
                print(a9 + ' is not a suitable preposition ')
                print("The correct answer is " + y9)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c9 = input()
                z9 = c9.lower()
                k9 = "a"
                if z9 != k9:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")
        elif s == "10":
            print("sich kummern :- ")
            a10 = input()
            x10 = a10.lower()
            y10 = "um"
            if x10 != y10:
                print(a10 + ' is not a suitable preposition ')
                print("The correct answer is " + y10)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c10 = input()
                z10 = c10.lower()
                k10 = "a"
                if z10 != k10:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")
        elif s == "11":
            print("nachdenken :- ")
            a11 = input()
            x11 = a11.lower()
            y11 = 'über'
            if x11 not in y11:
                print(a11 + ' is not a suitable preposition ')
                print("The correct answer is " + y11)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c11 = input()
                z11 = c11.lower()
                k11 = "a"
                if z11 != k11:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")
        elif s == "12":
            print("reden :- ")
            a12 = input()
            x12 = a12.lower()
            y12 = ["über", "mit"]
            if x12 not in y12:
                print(a12 + ' is not a suitable preposition ')
                print("The correct answer is " + ','.join(y12))
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c12 = input()
                z12 = c12.lower()
                k12 = "a"
                if z12 != k12:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")
        elif s == "13":
            print("sprechen :- ")
            a13 = input()
            x13 = a13.lower()
            y13 = ["über", "mit", "von"]
            if x13 not in y13:
                print(a13 + ' is not a suitable preposition ')
                print("The correct answer is " + '.'.join(y13))
            else:
                print("Great, you're doing good!")
                print("uber--> akk.... mit and von --> dativ.")

        elif s == "14":
            print("sich verlieben :- ")
            a14 = input()
            x14 = a14.lower()
            y14 = "in"
            if x14 != y14:
                print(a14 + ' is not a suitable preposition ')
                print("The correct answer is " + y14)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c14 = input()
                z14 = c14.lower()
                k14 = "a"
                if z14 != k14:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")
        elif s == "15":
            print("sich vorbereiten :- ")
            a15 = input()
            x15 = a15.lower()
            y15 = "auf"
            if x15 != y15:
                print(a15 + ' is not a suitable preposition ')
                print("The correct answer is " + y15)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c15 = input()
                z15 = c15.lower()
                k15 = "a"
                if z15 != k15:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")
        elif s == "16":
            print("warten :- ")
            a16 = input()
            x16 = a16.lower()
            y16 = "auf"
            if x16 != y16:
                print(a16 + ' is not a suitable preposition ')
                print("The correct answer is " + y16)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c16 = input()
                z16 = c16.lower()
                k16 = "a"
                if z16 != k16:
                    print("This is not dative.")
                    print("It is accusative.")
                else:
                    print("You are correct!")
        elif s == "17":
            print("sich bewerben :- ")
            a17 = input()
            x17 = a17.lower()
            y17 = ["um", "bei"]
            if x17 not in y17:
                print(a17 + ' is not a suitable preposition ')
                print("The correct answer is " + ','.join(y17))
            else:
                print("Great, you're doing good!")
                print("bei--> dativ and um --> akku.")
        elif s == "18":
            print("einladen :- ")
            a18 = input()
            x18 = a18.lower()
            y18 = "zu"
            if x18 != y18:
                print(a18 + ' is not a suitable preposition ')
                print("The correct answer is " + y18)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c18 = input()
                z18 = c18.lower()
                k18 = "d"
                if z18 != k18:
                    print("This is not accusative.")
                    print("It is dativ.")
                else:
                    print("You are correct!")
        elif s == "19":
            print("fragen :- ")
            a19 = input()
            x19 = a19.lower()
            y19 = "nach"
            if x19 != y19:
                print(a19 + ' is not a suitable preposition ')
                print("The correct answer is " + y19)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c19 = input()
                z19 = c19.lower()
                k19 = "d"
                if z19 != k19:
                    print("This is not accusative.")
                    print("It is dativ.")
                else:
                    print("You are correct!")
        elif s == "20":
            print("sich treffen :- ")
            a20 = input()
            x20 = a20.lower()
            y20 = "mit"
            if x20 != y20:
                print(a20 + ' is not a suitable preposition ')
                print("The correct answer is " + y20)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c20 = input()
                z20 = c20.lower()
                k20 = "d"
                if z20 != k20:
                    print("This is not accusative.")
                    print("It is dativ.")
                else:
                    print("You are correct!")
        elif s == "21":
            print("sich verabreden :- ")
            a21 = input()
            x21 = a21.lower()
            y21 = "mit"
            if x21 != y21:
                print(a21 + ' is not a suitable preposition ')
                print("The correct answer is " + y21)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c21 = input()
                z21 = c21.lower()
                k21 = "d"
                if z21 != k21:
                    print("This is not accusative.")
                    print("It is dativ.")
                else:
                    print("You are correct!")
        elif s == "22":
            print("teilnehmen :- ")
            a22 = input()
            x22 = a22.lower()
            y22 = "an"
            if x22 != y22:
                print(a22 + ' is not a suitable preposition ')
                print("The correct answer is " + y22)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c22 = input()
                z22 = c22.lower()
                k22 = "d"
                if z22 != k22:
                    print("This is not accusative.")
                    print("It is dativ.")
                else:
                    print("You are correct!")
        elif s == "23":
            print("sich treffen :- ")
            a23 = input()
            x23 = a23.lower()
            y23 = "mit"
            if x23 != y23:
                print(a23 + ' is not a suitable preposition ')
                print("The correct answer is " + y23)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c23 = input()
                z23 = c23.lower()
                k23 = "d"
                if z23 != k23:
                    print("This is not accusative.")
                    print("It is dativ.")
                else:
                    print("You are correct!")

        elif s == "25":
            print("abhangen :- ")
            a25 = input()
            x25 = a25.lower()
            y25 = "von"
            if x25 != y25:
                print(a25 + ' is not a suitable preposition ')
                print("The correct answer is " + y25)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c25 = input()
                z25 = c25.lower()
                k25 = "d"
                if z25 != k25:
                    print("This is not accusative.")
                    print("It is dativ.")
                else:
                    print("You are correct!")
        elif s == "26":
            print("helfen :- ")
            a26 = input()
            x26 = a26.lower()
            y26 = "bei"
            if x26 != y26:
                print(a26 + ' is not a suitable preposition ')
                print("The correct answer is " + y26)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c26 = input()
                z26 = c26.lower()
                k26 = "d"
                if z26 != k26:
                    print("This is not accusative.")
                    print("It is dativ.")
                else:
                    print("You are correct!")
        elif s == "27":
            print("sich verstehen :- ")
            a27 = input()
            x27 = a27.lower()
            y27 = "mit"
            if x27 != y27:
                print(a27 + ' is not a suitable preposition ')
                print("The correct answer is " + y27)
            else:
                print("Great, you're doing good!")
                print("Now tell me the case too.")
                c27 = input()
                z27 = c27.lower()
                k27 = "d"
                if z27 != k27:
                    print("This is not accusative.")
                    print("It is dativ.")
                else:
                    print("You are correct!")
time.sleep(3)
