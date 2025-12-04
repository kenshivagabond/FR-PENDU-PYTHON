import random

file = open("ods4.txt","r")

data = file.read()

data_into_list = data.split()

file.close()

word = random.choice(data_into_list)

letter = list(word)

def masque_depart(letter):
    letter_masque = []
    i = 0
    while i < len(letter):

        if letter[i] == letter[0]:
            letter_masque.append(letter[0])


        else:
            letter_masque.append("_")

        i += 1

    return ''.join(letter_masque)


def partie(letter,word):
    print(masque_depart(letter))
    n = input("entrez une lettre : ")
    depart = list(masque_depart(letter))  # 
    i , z = 0 , 0
    non_letter = 1
    already_use = []
    seen = []
    found = False
    while i < len(letter):
        if n in letter:
            found = True
            for j in range(len(letter)):
                if letter[j] == n:
                   seen.append(j)
            while(found and z < len(seen)):
                 p = seen[z]
                 depart[p] = n
                 z += 1
            print(depart)
            print(f" lettre  {n}  trouvez")
            if n in already_use:
                print("reessayez")
            else:
                already_use.append(n)
            if "_" not in depart:
                print("Gagnée")
                break
            non_letter += 0
            n = input("entrez une lettre : ")
        

        elif n not in letter and non_letter < 3:
            print(f"",{non_letter}," /3 lettre incorrecte")
            non_letter += 1
            n = input("entrez une lettre :")

        
        else:
            print(f"perdu le mot était {word}")
            break
    i += 1



partie(letter,word)





