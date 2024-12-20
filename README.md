# Enums & Exceptions

## Enums (Enumerations)

### Basic Enum Usage
- Enums are classes that inherit from `enum.Enum`
- Each enum member is an instance of the enum class
- Enum members have attributes:
  - `name`: The name of the enum member
  - `value`: The value assigned to the enum member

### Key Features
1. **Identity Tests**
   - Enum members are singleton objects
   - Same-valued enum members are identical (`is` comparison works)
   - Can use `==` for comparison

2. **Iteration**
   - Can iterate through enum members
   - Only unique values are included in iteration

3. **Access Methods**
   - By name: `Color['RED']`
   - By value: `Color(1)`
   - Direct attribute: `Color.RED`

4. **Auto Values**
   - Can use `enum.auto()` to automatically assign values
   - Values increment starting from 1 by default

### Advanced Features
1. **Aliases**
   - Multiple names can map to the same value
   - Useful for handling different strings with same meaning
   - Example:
     ```python
     class Status(enum.Enum):
         ready = 'ready'
         running = 'running'
         busy = 'running'      # Alias
         processing = 'running' # Alias
     ```

2. **Custom Methods**
   - Can add methods to enum classes
   - Can override built-in methods like `__repr__`
   - Can implement comparison methods

## Exceptions

### Exception Hierarchy
- BaseException
  - Exception
    - LookupError
      - IndexError
      - KeyError
    - ValueError
    - TypeError
    - ...

### Exception Handling

1. **Basic Structure**
```python
try:
    # code that might raise an exception
except Exception as e:
    # handle the exception
```

2. **Multiple Exception Handlers**
- Can catch different types of exceptions
- More specific exceptions should come before general ones

3. **Exception Propagation**
- Exceptions propagate up the call stack if not handled
- Can re-raise exceptions using `raise`

### Custom Exceptions

1. **Creating Custom Exceptions**
- Should inherit from `Exception` or its subclasses
- Can add custom attributes and methods
- Example:
  ```python
  class CustomError(Exception):
      def __init__(self, message):
          self.message = message
          super().__init__(self.message)
  ```

2. **Best Practices**
- Use descriptive names ending with 'Error' or 'Exception'
- Include meaningful error messages
- Consider creating exception hierarchies for complex applications

### Exception Design Patterns

1. **EAFP (Easier to Ask for Forgiveness than Permission)**

```python
try:
# Attempt operation
except ExceptionType:
# Handle failure
```

2. **LBYL (Look Before You Leap)**

```python
if condition:
# Attempt operation
else:
# Handle failure
```

## Practical Example (Library System)

The library system implementation demonstrates:

1. **Enums**
- `BookGenre`: Categorizes books using auto-values
- `MembershipLevel`: Defines membership levels with specific values

2. **Custom Exceptions**
- `BookNotAvailableError`
- `InvalidMembershipError`
- `LateReturnError`

3. **Exception Handling**
- Proper error messages
- Specific exception types for different error cases
- Clean exception hierarchy