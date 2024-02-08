# Object Type Checking Functions

## 1. `inherits_from(obj, a_class)`

### Purpose:
Checks if `obj` is an instance of a class that directly inherits from `a_class`.

### Logic:
- Uses `issubclass(type(obj), a_class)` to see if `obj`'s class is a subclass of `a_class`.
- Uses `type(obj) != a_class` to exclude cases where `obj` is an instance of `a_class` itself (not just a subclass).

### Examples:
- `inherits_from(MySubclass(), MyClass)` returns `True`.
- `inherits_from(MyInstance, MyClass)` returns `False` (not directly inherited).

## 2. `is_kind_of_class(obj, a_class)`

### Purpose:
Checks if `obj` is an instance of either `a_class` or any class that inherits from it (including direct and indirect inheritance).

### Logic:
Uses `isinstance(obj, a_class)` to directly check if `obj` is an instance of `a_class`.

### Examples:
- `is_kind_of_class(MySubclass(), MyClass)` returns `True` (inherited).
- `is_kind_of_class(MyInstance, MyClass)` returns `True` (direct instance).
- `is_kind_of_class(object(), object)` returns `True` (all objects inherit from `object`).

## 3. `is_same_class(obj, a_class)`

### Purpose:
Checks if `obj` is an instance of exactly `a_class` and not any subclass of it.

### Logic:
Uses `obj.__class__ == a_class` to compare the type of the object (`__class__`) with the specific class object (`a_class`).

### Examples:
- `is_same_class(MyInstance, MyClass)` returns `True` (direct instance).
- `is_same_class(MySubclass(), MyClass)` returns `False` (subclass, not exactly `MyClass`).
- `is_same_class(object(), object)` returns `True` (all objects are of the same type `object`).
