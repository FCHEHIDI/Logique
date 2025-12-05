# Object 2

### # Écrivez une fonction qui récupère toutes les valeurs d'un objet

```python
# Cas d'usage : Récupération des scores d'un joueur
scores = {
    "level1": 100,
    "level2": 85,
    "level3": 95
}
print(get_values(scores))  # [100, 85, 95]
```


---

### # Écrivez une fonction qui transforme les valeurs d'un objet

```python
# Cas d'usage : Conversion de prix en euros vers dollars
prices_in_euros = {
    "book": 20,
    "pen": 5,
    "notebook": 10
}
to_dollars = lambda euros: euros * 1.1
print(transform_values(prices_in_euros, to_dollars))
# { "book": 22.0, "pen": 5.5, "notebook": 11.0 }
```


---

### # Écrivez une fonction qui fusionne deux objets en sommant les valeurs numériques communes

```python
# Cas d'usage : Fusion des ventes mensuelles de deux magasins
store1_sales = { "january": 1000, "february": 1200, "march": 900 }
store2_sales = { "january": 800, "february": 950, "march": 1100 }
print(merge_objects(store1_sales, store2_sales))
# { "january": 1800, "february": 2150, "march": 2000 }
```


---

### # Écrivez une fonction qui filtre un objet selon une condition sur les valeurs

```python
# Cas d'usage : Filtrage des produits en rupture de stock
inventory = {
    "laptop": 0,
    "smartphone": 5,
    "tablet": 0,
    "headphones": 8
}
print(filter_object(inventory, lambda stock: stock == 0))
# { "laptop": 0, "tablet": 0 }
```


---

### # Écrivez une fonction qui convertit un objet plat en objet imbriqué en utilisant les points comme séparateurs

```python
# Cas d'usage : Configuration d'une application
flat_config = {
    'app.name': 'MyApp',
    'app.version': '1.0.0',
    'database.host': 'localhost',
    'database.port': 5432
}
print(flat_to_nested(flat_config))
# {
#     'app': { 'name': 'MyApp', 'version': '1.0.0' },
#     'database': { 'host': 'localhost', 'port': 5432 }
# }
```


---

### # Écrivez une fonction qui trouve les clés d'un objet ayant une valeur spécifique

```python
# Cas d'usage : Recherche des produits en rupture de stock
product_stock = {
    "laptop": 0,
    "mouse": 5,
    "keyboard": 0,
    "monitor": 3
}
print(find_keys_by_value(product_stock, 0))
# ["laptop", "keyboard"]
```


---

### # Écrivez une fonction qui crée un objet à partir de deux tableaux

```python
# Cas d'usage : Création d'un objet de scores à partir de noms de joueurs et leurs points
player_names = ["Alice", "Bob", "Charlie"]
scores = [100, 85, 90]
print(create_object_from_arrays(player_names, scores))
# { "Alice": 100, "Bob": 85, "Charlie": 90 }
```


---

### # Écrivez une fonction qui compte les occurrences de valeurs dans un objet

```python
# Cas d'usage : Analyse des statuts de commandes
order_statuses = {
    "order1": "pending",
    "order2": "delivered",
    "order3": "pending",
    "order4": "cancelled",
    "order5": "pending"
}
print(count_values(order_statuses))
# { "pending": 3, "delivered": 1, "cancelled": 1 }
```


---

### # Écrivez une fonction qui extrait certaines propriétés d'un objet

```python
# Cas d'usage : Extraction des informations publiques d'un profil
user_profile = {
    "name": "Jean Martin",
    "email": "jean@email.com",
    "password": "secret123",
    "age": 35,
    "address": "123 rue Principal"
}
public_info = ["name", "age"]
print(extract_properties(user_profile, public_info))
# { "name": "Jean Martin", "age": 35 }
```


---

### # Écrivez une fonction qui trie les propriétés d'un objet par valeur

```python
# Cas d'usage : Tri des scores de joueurs
player_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}
print(sort_object_by_value(player_scores))
# { "Charlie": 78, "Alice": 85, "Bob": 92, "David": 95 }
```


---

### # Écrivez une fonction qui trouve la valeur maximale dans un objet de nombres

```python
# Cas d'usage : Recherche du meilleur score dans un jeu
game_scores = {
    "level1": 850,
    "level2": 920,
    "level3": 880,
    "level4": 1020
}
print(find_max_value(game_scores))  # 1020
```


---

### # Écrivez une fonction qui créé un objet à partir d'un tableau de paires clé-valeur

```python
# Cas d'usage : Création d'un catalogue de produits
product_pairs = [
    ["pommes", 2.5],
    ["bananes", 1.8],
    ["oranges", 2.2]
]
print(create_object_from_pairs(product_pairs))
# { "pommes": 2.5, "bananes": 1.8, "oranges": 2.2 }
```


---

### # Écrivez une fonction qui recherche une valeur dans un objet imbriqué

```python
# Cas d'usage : Recherche dans une structure de données de configuration
config = {
    "app": {
        "name": "MonApp",
        "settings": {
            "theme": "dark",
            "notifications": {
                "email": True,
                "push": False
            }
        }
    }
}
print(find_value_in_object(config, "dark"))  # ["app", "settings", "theme"]
```


---

### # Écrivez une fonction qui groupe les objets par une propriété spécifique

```python
# Cas d'usage : Groupement d'étudiants par niveau
students = [
    { "name": "Alice", "level": "Débutant" },
    { "name": "Bob", "level": "Intermédiaire" },
    { "name": "Charlie", "level": "Débutant" },
    { "name": "David", "level": "Avancé" }
]
print(group_by_property(students, "level"))
# {
#   "Débutant": [
#     { "name": "Alice", "level": "Débutant" },
#     { "name": "Charlie", "level": "Débutant" }
#   ],
#   "Intermédiaire": [{ "name": "Bob", "level": "Intermédiaire" }],
#   "Avancé": [{ "name": "David", "level": "Avancé" }]
# }
```


---

### # Écrivez une fonction qui vérifie si un objet correspond à un schéma spécifique

```python
# Cas d'usage : Validation d'un formulaire utilisateur
user_schema = {
    "name": "string",
    "age": "number",
    "email": "string"
}
user_input = {
    "name": "Marie",
    "age": 25,
    "email": "marie@email.com"
}
print(validate_object(user_input, user_schema))  # True
```


---

### # Écrivez une fonction qui compare les modifications entre deux objets

```python
# Cas d'usage : Suivi des modifications d'un profil utilisateur
old_profile = {
    "name": "Jean Dupont",
    "email": "jean@email.com",
    "age": 30
}
new_profile = {
    "name": "Jean Dupont",
    "email": "jean.dupont@email.com",
    "age": 31,
    "phone": "0123456789"
}
print(compare_differences(old_profile, new_profile))
# {
#     "email": { "type": "modified", "old": "jean@email.com", "new": "jean.dupont@email.com" },
#     "age": { "type": "modified", "old": 30, "new": 31 },
#     "phone": { "type": "added", "new": "0123456789" }
# }
```


---

### # Écrivez une fonction qui convertit un objet en chaîne de paramètres d'URL

```python
# Cas d'usage : Construction d'une URL de recherche
search_params = {
    "query": "ordinateur portable",
    "maxPrice": 1000,
    "brand": "Dell",
    "inStock": True
}
print(object_to_url_params(search_params))
# query=ordinateur%20portable&maxPrice=1000&brand=Dell&inStock=true
```


---

### # Écrivez une fonction qui génère un résumé statistique d'un objet contenant des nombres

```python
# Cas d'usage : Analyse des ventes mensuelles
monthly_revenues = {
    "january": 1000,
    "february": 1200,
    "march": 900,
    "april": 1500
}
print(get_object_stats(monthly_revenues))
"""
{
 basic: {
   min: 900,
   max: 1500,
   average: 1150,
   total: 4600
 },
 advanced: {
   median: 1100,
   variance: 52500,
   standardDeviation: 229.13
 }
}
"""
```