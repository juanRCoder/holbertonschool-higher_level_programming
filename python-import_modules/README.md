# Pyhton - Import & Modules
- In this project we will review topics such as import&modules:
```py
   # file.py
   def greet(str):
    return f"Hola {str}"

   # file2.py
   module = __import__("file").greet
   print(module("Juan"))
   # Hola Juan


   # file3.py
   from file import greet
   print(greet("Juan2"))
   # Hola Juan2
```
