"""Statically typed python using mypy"""

from typing import Iterator

def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

for n in fib("testing"): # Error; "testing" is not an int
    print(n) 

x: int = 1 
x = "lol" # Error; x was delcared and initialized as an int

y = 1
y = "lol" # Error; y was initialized with an int