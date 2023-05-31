p = ["kat", "Fred", "Sam", "Bob", "Lucy"]
pt = ["Lex", "Hal", "Ann", "Greg", "Laura"]
g = [95, 85, 93, 90, 88]
while True:
    op = input("What would you like to do? 1 to list all options. 2 to change a grade or partner. 3 to end")
    if op == "1":
        for i in range(len(p)):
            print(p[i],"and", pt[i], "'s grade is:", g[i])
    if op == "2":
        o = input("Would you like to change a grade or partner? 1 for grade. 2 for partner")
        if o == "1":
            print(g)
            gr = input("Which grade would you like to change?")
            if gr == "95":
                gra = input("The grade you have selected is 95, what would you like to change it to?")
                g.remove(95)
                g.insert(0, gra)
            if gr == "85":
                gra = input("The grade you have selected is 85, what would you like to change it to?")
                g.remove(85)
                g.insert(1, gra)
            if gr == "93":
                gra = input("The grade you have selected is 93, what would you like to change it to?")
                g.remove(93)
                g.insert(2, gra)
            if gr == "90":
                gra = input("The grade you have selected is 90, what would you like to change it to?")
                g.remove(90)
                g.insert(3, gra)
            if gr == "88":
                gra = input("The grade you have selected is 88, what would you like to change it to?")
                g.remove(88)
                g.insert(4, gra)
        if o == "2":
            print(p, pt)
            pte = input("Which partner would you like to change?")
            if pte in p:
                print("You are changing", pte)
                np = input("What would you like to change the person to?")
                y = p.index(pte)
                del(p[y])
                p.insert(y, pte)
    if op == "3":
        break