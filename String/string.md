# String

### Créez une fonction qui prend une chaîne de caractères en paramètre et retourne sa longueur après avoir supprimé tous les espaces.

*Case d'usage possible: Validation de la longueur d'un tweet ou d'un message SMS*\n**Entrée :** `"Bonjour le monde !"`\n**Sortie attendue :** `16 caractères`


---

### Développez une fonction qui accepte un prénom en paramètre et renvoie une salutation personnalisée en mettant la première lettre en majuscule.

*Cas d'usage: Système de messagerie automatique ou e-mailing*\n**Entrée :** `"jean-pierre"`\n**Sortie attendue :** `"Bonjour Jean-Pierre"`


---

### Écrivez une fonction qui détermine si une chaîne de caractères se termine par un point d'exclamation.

*Cas d'usage: Analyse de ton dans un service client*\n**Entrée :** `"Je suis très satisfait !"`\n**Sortie attendue :** `True`


---

### Écrivez une fonction qui compte le nombre d'occurrences d'une lettre dans une chaîne

*Case d'usage: Dans un système de traduction automatique, il est parfois nécessaire d'inverser l'ordre des mots pour s'adapter à la structure grammaticale de la langue cible. Par exemple, dans la traduction du français vers le japonais, où l'ordre des mots est fondamentalement différent. La fonction pourrait être utilisée comme étape préliminaire dans ce processus de traduction.*

```python
french_phrase = "Je mange une pomme"
reversed = reverse_words(french_phrase)
# Résultat: "pomme une mange Je"
# Facilite la conversion vers: "私はりんごを食べる" (Watashi wa ringo wo taberu)
```


---

### Écrivez une fonction qui compte le nombre d'occurrences d'une lettre dans une chaîne

*Cas d'usage: Dans un outil d'analyse de texte pour professeurs de langue, cette fonction permet d'évaluer la fréquence d'utilisation de certaines lettres dans les productions écrites des élèves. Cela peut aider à identifier des difficultés spécifiques ou des patterns d'écriture.*


---

### Écrivez une fonction qui convertit une chaîne en "camelCase"

*Cas d'usage: Dans un système de migration de base de données, où les conventions de nommage diffèrent entre l'ancien et le nouveau système. Par exemple, lors de la conversion de noms de colonnes SQL (avec underscores) vers des propriétés JavaScript.*

```python
sql_column_name = "user_first_name"
javascript_property = to_camel_case(sql_column_name)
# Transformation pour l'intégration dans le code : "userFirstName"
```


---

### Écrivez une fonction qui compte le nombre de voyelles dans une chaîne

*Cas d'usage: Dans une application d'aide à l'apprentissage de la poésie, cette fonction peut servir à analyser la sonorité des vers et identifier les assonances. Cela aide les élèves à comprendre la structure phonétique des poèmes.*


---

### Écrivez une fonction qui alterne majuscules et minuscules dans une chaîne

*Cas d'usage: Dans un outil de génération de mots de passe mémorisables, cette fonction peut être utilisée pour créer des variantes visuellement distinctes d'un mot tout en conservant sa lisibilité.*


---

### Écrivez une fonction qui supprime les caractères en double consécutifs

*Cas d'usage: Dans un système de nettoyage de données pour un service client, cette fonction peut être utilisée pour corriger les erreurs de frappe courantes dans les messages des utilisateurs, notamment les répétitions de caractères dues à des touches maintenues trop longtemps.*

```python
message_utilisateur = "Bonjouuuur !!! J'ai besoiiiin d'aide...."
message_nettoye = remove_duplicates(message_utilisateur)
# Normalisation du texte : "Bonjour ! J'ai besoin d'aide."
print(f"Message normalisé : {message_nettoye}")
```


---

### Écrivez une fonction qui extrait les initiales d'un nom complet

*Cas d'usage: Dans un système de gestion des ressources humaines d'une grande entreprise, cette fonction est utilisée pour générer automatiquement des identifiants uniques pour les employés. Par exemple, lorsqu'un nouveau collaborateur rejoint l'entreprise*


---

### Écrivez une fonction qui masque les caractères d'une chaîne sauf les N derniers

*Cas d'usage: Dans une application bancaire sécurisée, cette fonction est essentielle pour l'affichage des données sensibles dans les relevés de compte et les rapports de transaction*

```python
# Cas d'usage : Masquage partiel d'un numéro de carte bancaire
card_number = "1234567890123456"
print(mask_string(card_number, 4)) # "3456"
```


---

### Écrivez une fonction qui vérifie si une chaîne est un palindrome

*Cas d'usage: Dans une application de vérification de marques déposées, cette fonction aide à identifier les noms de marque qui sont des palindromes, une caractéristique souvent recherchée pour leur mémorabilité*

```python
# Cas d'usage : Vérification d'un slogan publicitaire
slogan = "Eh ! ça va la vache ?"
print(is_palindrome(slogan)) # True
```


---

### Écrivez une fonction qui trouve la plus longue séquence de caractères identiques

*Cas d'usage: Dans un système de contrôle qualité pour l'impression de codes-barres, cette fonction détecte les erreurs potentielles d'impression dues à des répétitions excessives*

```python
# Cas d'usage : Analyse de répétitions dans un texte
input = "aaabbbbbcccc"
print(longest_sequence(input)) # "bbbbb"
```


---

### Écrivez une fonction qui formate un texte en ajoutant des points de suspension

*Cas d'usage: Dans un système de gestion de contenu pour réseaux sociaux, cette fonction optimise les descriptions de produits pour différentes plateformes*

```python
# Cas d'usage : Formatage de descriptions pour une liste d'articles
description = "Ceci est une très longue description d'un produit"
print(truncate(description, 20)) # "Ceci est une très..."
```


---

### Écrivez une fonction qui capitalise la première lettre de chaque mot

*Cas d'usage: Dans un système de gestion documentaire, cette fonction standardise automatiquement les titres de documents pour maintenir une cohérence dans l'archivage*

```python
# Cas d'usage : Formatage de titres d'articles
title = "bienvenue sur notre site web"
print(capitalize_words(title)) # "Bienvenue Sur Notre Site Web"
```