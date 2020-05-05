# REN-L-Inalco
Reconnaissance d'Entités Nommées et Apprentissage 

Note explicative du REN&L

Dans cette deuxième partie, j’ai mis en place un prototype renommé REN&L(Reconnaissance d’entités nommées et apprentissage) fonctionnant avec la bibliothèque Keras et tensorflow dans le but d’apprendre à partir des données annotées(lien ) dans la première partie (lien) grâce à un prototype appelée NER.
En entrée de l’algorithme, nous exploitons les descripteurs suivants : les mots et l’étiquetage morpho-syntaxique (POS) .

Les CRF sont particulièrement efficaces pour l’étiquetage de séquences.
Dans cette nouvelle expérimentation, nous comparons l’efficacité de deux types de représentations vectorielles des mots avec le BiLSTM-CRF. 

Nous allons  procéder de la manière suivante :

    • Prétraitement des données de texte pour le traitement automatique du langage naturel.
    • Construire et former un modèle CRF et  bidirectionnel LSTM(Bi-Lstm) en utilisant Keras et Tensorflow
    • Évaluez notre modèle sur l'ensemble de test
    • Exécutez le modèle sur vos propres phrases!            

Expérimentation :

- Lecture des données annotées dans le système, avec une sélection de 500.000 lignes au lieu de 9.681.277.
Nombre de phrase 22.705, 
Nombre de mots : 1903.

- Visualisation de ces données sous forme graphique par nombre de jeton et échantillons

- Prétraitement des données

- Présentation des modèles

- Formation des modèles


- Validation

- Évaluez quelques échantillons dans l’ensemble de test

- Tester le modèle en entrant une phrase au hasard comme suit ‘’ ’’ et le système te retourne ‘’’

 
