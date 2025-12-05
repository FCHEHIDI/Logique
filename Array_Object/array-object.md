# Array-Object

### Écrivez une fonction qui filtre un tableau d'objets selon une propriété et sa valeur

```python
# Cas d'usage : Filtrage des utilisateurs actifs dans une application
users = [
    {"id": 1, "name": "Alice", "age": 25, "active": True},
    {"id": 2, "name": "Bob", "age": 30, "active": False},
    {"id": 3, "name": "Charlie", "age": 35, "active": True}
]
print(filter_by_property(users, 'active', True))
# [{"id": 1, "name": "Alice", "age": 25, "active": True}, {"id": 3, "name": "Charlie", "age": 35, "active": True}]
```


---

### Écrivez une fonction qui groupe les éléments d'un tableau selon une propriété

```python
# Cas d'usage : Regroupement de produits par catégorie dans un e-commerce
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699},
    {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 29}
]
print(group_by(products, 'category'))
# {"Electronics": [...], "Clothing": [...]}
```


---

### Écrivez une fonction qui trouve l'intersection entre deux tableaux d'objets selon une propriété donnée

```python
# Cas d'usage : Trouver les livres disponibles dans deux bibliothèques
library1 = [
    {"id": 1, "title": "1984", "author": "Orwell", "available": True},
    {"id": 2, "title": "Dune", "author": "Herbert", "available": False}
]
library2 = [
    {"id": 3, "title": "1984", "author": "Orwell", "available": True},
    {"id": 4, "title": "Foundation", "author": "Asimov", "available": True}
]
print(find_intersection(library1, library2, 'title'))
# [{"id": 1, "title": "1984", "author": "Orwell", "available": True}]
```


---

### Écrivez une fonction qui transforme un tableau d'objets en utilisant une fonction de mapping personnalisée

```python
# Cas d'usage : Création d'un rapport de salaires avec noms complets
employees = [
    {"id": 1, "firstName": "John", "lastName": "Doe", "salary": 50000},
    {"id": 2, "firstName": "Jane", "lastName": "Smith", "salary": 60000}
]
transformer = lambda emp: {
    "id": emp["id"],
    "fullName": f"{emp['firstName']} {emp['lastName']}",
    "annualSalary": emp["salary"] * 12
}
print(transform_array(employees, transformer))
# [{"id": 1, "fullName": "John Doe", "annualSalary": 600000}, ...]
```


---

### Écrivez une fonction qui agrège les données d'un tableau d'objets

```python
# Cas d'usage : Calcul des totaux par catégorie de dépenses
transactions = [
    {"id": 1, "type": "debit", "amount": 100, "category": "Food"},
    {"id": 2, "type": "debit", "amount": 50, "category": "Food"},
    {"id": 3, "type": "credit", "amount": 75, "category": "Income"}
]
print(aggregate_data(transactions, 'category', 'amount'))
# {"Food": 150, "Income": 75}
```