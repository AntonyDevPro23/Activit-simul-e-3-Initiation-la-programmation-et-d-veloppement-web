def calculatrice():
    print("Bienvenue dans la calculatrice Python !\n")
    
    while True:
        try:
            num1 = float(input("Entrez le premier nombre : "))
            operateur = input("Entrez un opérateur (+, -, *, /) : ")
            num2 = float(input("Entrez le deuxième nombre : "))

            if operateur == '+':
                resultat = num1 + num2
            elif operateur == '-':
                resultat = num1 - num2
            elif operateur == '*':
                resultat = num1 * num2
            elif operateur == '/':
                if num2 == 0:
                    print("Erreur : Division par zéro !")
                    continue
                resultat = num1 / num2
            else:
                print("Opérateur invalide. Veuillez utiliser +, -, * ou /.")
                continue

            print(f"Résultat : {resultat}\n")
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.\n")

        choix = input("Voulez-vous effectuer un autre calcul ? (oui/non) : ").lower()
        if choix != "oui":
            print("Merci d'avoir utilisé la calculatrice !")
            break

calculatrice()

