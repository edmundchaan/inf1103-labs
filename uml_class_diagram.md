# UML Class Diagram: OOP Inventory Management System

```
+-----------------------------------------+
|                 Product                 |
+-----------------------------------------+
| - __product_id : String                 |
| - __name : String                       |
| - __price : float                       |
| - __stock : int                         |
+-----------------------------------------+
| + __init__(product_id, name, price,     |
|            stock) : void                |
| + get_product_id() : String             |
| + get_name() : String                   |
| + get_price() : float                   |
| + get_stock() : int                     |
| + update_stock(quantity : int) : void   |
| + display_information() : void          |
| + to_dict() : dict                      |
+-----------------------------------------+
                    ^
                    | 0..*  (contains)
                    |
+-----------------------------------------+
|                Inventory                |
+-----------------------------------------+
| - __products : list[Product]            |
+-----------------------------------------+
| + __init__() : void                     |
| + add_product(product : Product) : bool |
| + search_product(product_id : String)   |
|       : Product                         |
| + update_stock(product_id : String,     |
|       quantity : int) : bool            |
| + display_all() : void                  |
| + get_products() : list[Product]        |
+-----------------------------------------+
```

## Relationship

`Inventory` holds a collection of `Product` objects (one-to-many composition). The main program (`inventory_oop.py`) creates the `Inventory` and `Product` objects, shows the menu, reads user input and calls `Inventory` methods. It also handles loading and saving `inventory.json`.

## Responsibilities (Single Responsibility Principle)

| Class | Responsibility |
|---|---|
| Product | Represents one product and manages its own state |
| Inventory | Manages a collection of products (store, add, search, display) |
| Main program | Menu, user input, calling Inventory methods, file loading and saving |
