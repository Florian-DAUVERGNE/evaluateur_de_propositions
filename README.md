# README

## Projet : Évaluateur de Propositions Logiques

Ce projet est un évaluateur de propositions logiques basé sur la syntaxe et la sémantique des langages de programmation. Il permet aux utilisateurs de saisir des formules logiques en utilisant des mots-clés, puis de les convertir pour une évaluation.

## Fonctionnalités

- **Conversion de Syntaxe :** Convertit les mots-clés en symboles logiques pour une représentation interne.
- **Analyse Syntaxique :** Utilise un lexer et un parser pour analyser la formule saisie par l'utilisateur.

## Installation

1. Assurez-vous d'avoir Python 3 installé sur votre système.

2. Clonez ce dépôt

    ```
    git clone git@github.com:Florian-DAUVERGNE/evaluateur_de_propositions.git
    ```

 ou téléchargez les fichiers source.

![alt text]( https://bpb-us-e1.wpmucdn.com/sites.northwestern.edu/dist/b/3044/files/2021/05/github.png)


3. (Optionnel) Si vous préférez travailler dans un environnement virtuel, vous pouvez le créer en utilisant les étapes suivantes :
    ```
    python -m venv venv
    source venv/bin/activate  # Pour Linux/macOS
    .\venv\Scripts\activate   # Pour Windows
    ```

4. Installez les dépendances nécessaires en exécutant la commande suivante :
    ```
    pip install -r requirements.txt
    ```

## Utilisation

1. Exécutez le script principal en utilisant Python :
  ```
  python main.py #Python
  python3 main.py #Python3
  ```
2. Suivez les instructions à l'écran pour saisir votre formule logique.
3. Utilisez la commande `help` pour afficher un tableau de correspondance entre les mots-clés et les symboles logiques.

## Exemple de Formule

```
(P or Q) then (not r iff (Q and P))
```

## Structure du Projet

- `main.py` : Le point d'entrée du programme. Gère l'interaction avec l'utilisateur et l'affichage des résultats.
- `Parser.py` : Contient le lexer et le parser PLY pour analyser les formules logiques.

## Bibliothèque
ply : https://github.com/dabeaz/ply

terminaltables : https://pypi.org/project/terminaltables/