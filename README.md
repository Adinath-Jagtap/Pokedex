## 📊 MEDIUM QUESTIONS - Core Patterns (10 mins)

### **Pattern 1: Fibonacci Variations** ⭐
**What it is**: Generate Fibonacci, then transform/filter it

**Core Fibonacci Generator**:
```python
a, b = 0, 1
for _ in range(n):
    # Do something with 'a'
    a, b = b, a + b  # KEY: Swap and add
```

**Common Transformations**:
1. **Cubes**: `print(a**3)`
2. **Prime Filter**: Check `is_prime(a)` before printing
3. **Range [i:j]**: Store in list, slice later
4. **Digit Operations**: `sum(int(d)**3 for d in str(a))`

**Example - Cubes of Fibonacci**:
```python
def cubes_of_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a**3, end=" ")
        a, b = b, a + b
```

---

### **Pattern 2: Digit Manipulation** 🔢
**What it is**: Break numbers into digits, transform, recombine

**Key Technique**:
```python
# Split into digits
digits = [int(d) for d in str(num)]

# Common operations
sum_of_cubes = sum(d**3 for d in digits)
digit_product = 1
for d in digits: digit_product *= d

# Check if palindrome
is_palindrome = str(num) == str(num)[::-1]

# Check increasing digits
is_increasing = all(digits[i] <= digits[i+1] for i in range(len(digits)-1))
```

---

### **Pattern 3: Prime Checking** ✓
**Standard Prime Check**:
```python
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

**Combined with Fibonacci**:
```python
def prime_fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        if is_prime(a):
            print(a, end=" ")
            count += 1
        a, b = b, a + b
```

---

### **Pattern 4: Armstrong/Special Numbers** 💎
**Logic**: Sum of digits^power = original number

```python
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d**power for d in digits) == num

# Find in range
for num in range(start, end+1):
    if is_armstrong(num):
        print(num)
```

---

### **Pattern 5: Cumulative Operations** 📈
**Track running totals/products**

```python
# Cumulative sum of Fibonacci
a, b = 0, 1
cumsum = 0
for _ in range(n):
    cumsum += a
    print(cumsum, end=" ")
    a, b = b, a + b

# Until condition
while cumsum < limit:
    cumsum += a
    a, b = b, a + b
```

---

## 🎯 MEDIUM QUICK TIPS
1. **Always initialize Fibonacci**: `a, b = 0, 1`
2. **Digit extraction**: `[int(d) for d in str(num)]`
3. **Prime check**: Loop up to `sqrt(n)`
4. **Combine conditions**: `if is_prime(fib) and fib % 2 == 0:`

---

## 🔥 HARD QUESTIONS - Matrix Patterns (10 mins)

### **Pattern 1: Snake Fill (Zig-Zag)** 🐍
**Logic**: Fill rows left→right, then right→left alternately

```python
def snake_matrix(n):
    num = 1
    for i in range(n):
        row = list(range(num, num + n))
        if i % 2 == 1:  # Odd rows reversed
            row = row[::-1]
        print(*row)
        num += n
```

**Visual**:
```
1  2  3  4
8  7  6  5  ← reversed
9 10 11 12
```

---

### **Pattern 2: Spiral Fill** 🌀
**Logic**: Fill in layers - right, down, left, up

```python
def spiral_matrix(n):
    mat = [[0] * n for _ in range(n)]
    num = 1
    left, right = 0, n - 1
    top, bottom = 0, n - 1
    
    while left <= right and top <= bottom:
        # Right
        for i in range(left, right + 1):
            mat[top][i] = num
            num += 1
        top += 1
        
        # Down
        for i in range(top, bottom + 1):
            mat[i][right] = num
            num += 1
        right -= 1
        
        # Left
        for i in range(right, left - 1, -1):
            mat[bottom][i] = num
            num += 1
        bottom -= 1
        
        # Up
        for i in range(bottom, top - 1, -1):
            mat[i][left] = num
            num += 1
        left += 1
    
    for row in mat:
        print(*row)
```

**Visual**:
```
1  2  3  4
12 13 14 5
11 16 15 6
10  9  8 7
```

---
