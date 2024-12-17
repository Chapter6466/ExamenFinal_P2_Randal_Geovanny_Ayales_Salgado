# ExamenFinal_P2_Randal_Geovanny_Ayales_Salgado
 
# Python Programming 2 - Final Exam

This repository contains the implementation and testing of various Python programming concepts as part of the Programming 2 final exam at Universidad Politécnica.

## Project Structure

The project consists of three main Python files:
- `parte1.py`: Contains theoretical questions and answers about Python concepts
- `parte2.py`: Implements three core functions for list and dictionary manipulation
- `parte3.py`: Contains unit tests for the implemented functions

## Core Functions

### 1. `aplanar(lista)`
Removes empty sublists from a given list.

```python
# Example usage:
aplanar([[1, 2, 3], [], [3], [5, 6]]) # Returns: [[1, 2, 3], [3], [5, 6]]
```

### 2. `permutaciones(lista)`
Generates all possible permutations of a given list using recursion.

```python
# Example usage:
permutaciones([1, 2, 3]) # Returns all possible arrangements of [1, 2, 3]
```

### 3. `diccionario_anidado(lista, diccionario)`
Creates a nested dictionary using values from a list as keys and dictionary key-value pairs as values.

```python
# Example usage:
diccionario_anidado([8, 3, 2], {'python': 4, 'is': 5, 'best': 9})
# Returns: {8: {'python': 4}, 3: {'is': 5}, 2: {'best': 9}}
```

## Testing

The project includes comprehensive unit tests in `parte3.py`. The tests cover:
- Empty list handling
- Various input combinations
- Edge cases
- Expected error conditions

To run the tests:
```bash
python parte3.py
```

## Theoretical Concepts

The project also includes explanations of key Python concepts:
1. Differences between lists and dictionaries
2. Object-oriented programming concepts (inheritance)
3. Practical applications of inheritance in code improvement

## Author

Randal Geovanny Ayales Salgado

## Date

December 16, 2024

## Course

Programming 2 - Universidad Politécnica