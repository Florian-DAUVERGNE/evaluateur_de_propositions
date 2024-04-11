from sympy.logic.boolalg import to_cnf
from sympy.logic.inference import satisfiable

def is_satisfiable(proposition):
    # Convertir la formule propositionnelle en forme normale conjonctive (CNF)
    cnf_form = to_cnf(proposition)
    
    # Résoudre la satisfiabilité de la CNF
    satisfiability = satisfiable(cnf_form)
    
    return satisfiability is not False

# Affichage du tableau des connecteurs logiques avec les symboles de la librairie sympy
print("Tableau des connecteurs logiques :")
print("+--------------------------------+")
print("| ¬  | ~   Non                   |")
print("| ∧  | &   Et (conjonction)      |")
print("| ∨  | |   Ou (disjonction)      |")
print("| →  | >>  Implication           |")
print("| ↔  | &   Équivalence           |")
print("+--------------------------------+")

while True:
    # Demander à l'utilisateur de saisir la formule propositionnelle
    proposition = input("\nEntrez la formule propositionnelle ou tapez 'q' pour quitter : ")

    if proposition.lower() == 'q':
        print("Programme terminé.")
        break

    # Vérifier la satisfiabilité de la formule propositionnelle
    if is_satisfiable(proposition.lower()):
        print("La formule est satisfiable.")
    else:
        print("La formule n'est pas satisfiable.")
    
    # Demander à l'utilisateur s'il souhaite entrer une nouvelle formule
    response = input("Voulez-vous entrer une nouvelle formule ? (Oui/Non) : ")
    if response.lower() != 'oui' and response.lower() != 'o':
        print("Programme terminé.")
        break
