import random

file = open("ods4.txt","r")

data = file.read()

data_into_list = data.split()

file.close()

word = random.choice(data_into_list)

letter = list(word)

print(letter)

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
    depart = list(masque_depart(letter))
    i = 0
    non_letter = 1
    while i < len(letter):
        if n in letter:
            depart = [element.replace('_', n) for element in depart]
            print(f" lettre ", n, " trouvez")
            non_letter += 0
            n = input("entrez une lettre : ")
            print(depart)
        elif n not in letter and non_letter < 3:
            print(f"",non_letter," /3 lettre incorrecte")
            non_letter += 1
            n = input("entrez une lettre :")
            print(depart)
        else:
            print("perdu")
            break
    i += 1
    return depart



partie(letter,word)





