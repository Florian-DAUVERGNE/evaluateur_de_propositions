from terminaltables import AsciiTable
from truthParser import lexer, parser  

def help():
    #Affiche un message d'aide avec la liste des symboles valides pour les formules de logique de proposition.

    # Définition des correspondance connecteur / symbole
    correspondance = AsciiTable([
        ["Connecteur", "Symbole"],
        ["not", "¬"],  # Connecteur correspondant au symbole de négation
        ["and", "∧"],  # Connecteur correspondant au symbole de conjonction
        ["or", "∨"],   # Connecteur correspondant au symbole de disjonction
        ["then", "→"], # Connecteur correspondant au symbole d'implication
        ["iff", "↔"]   # Connecteur correspondant au symbole d'équivalence
    ]).table

    # Affichage du message d'aide
    print("\n-----Taper votre formule (exemple : (P or Q) then (not r iff (Q and P))-----\n")
    print("Tableau de correspondance :\n")
    # Affichage de la table de correspondance
    print(correspondance)

def syntax_converter(expression):
    #Convertit les mots-clés en symboles logiques.
    return expression.replace("not", "¬").replace("and", "∧").replace("or", "∨").replace("then", "→").replace("iff", "↔")

# Afficher l'aide au début
help()

while True:
    try:
        s = input('Votre formule : ')  # Saisie de la formule
    except EOFError:  # Si l'utilisateur entre EOF (End of File), la boucle se termine
        break
    if not s: continue  # Si la saisie est vide, retour à la saisie
    if s == 'help': 
        help()  # Afficher l'aide si l'utilisateur tape "help"
        continue
    sentence = syntax_converter(s)  # Convertir la syntaxe de la formule saisie
    if(parser.parse(sentence, lexer=lexer)) : 
        print ("Formule correcte : {}".format(sentence))  # Afficher la formule si elle est correcte
