"""
Given an unsigned integer, write a function that returns the number of '1' bits
that the integer contains (the
[Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight))

Examples:

- `hamming_weight(n = 00000000000000000000001000000011) -> 3`
- `hamming_weight(n = 00000000000000000000000000001000) -> 1`
- `hamming_weight(n = 11111111111111111111111111111011) -> 31`

Notes:

- "Unsigned Integers (often called "uints") are just like integers (whole
numbers) but have the property that they don't have a + or - sign associated
with them. Thus they are always non-negative (zero or positive). We use uint's
when we know the value we are counting will always be non-negative."
"""

def hamming_weight(n):
    """
    bitwise logical operators: "&" and "|"
    
    the left and right shift operations
    
    << or >>>
    
    The >> operator allows us to move the bitwise digits over one spot to the right
    
    if "&" on the rightmost digit returns a 1, increment a counter
    
    >> by 1 bitwise digit
    
    when do we stop right shifting?
    we can stop right shifting when n == 0
    
    return the number of 1s in the bistwise representation of the number
    """
    """
    counter = 0
    while n != 0:
        if n & 1 == 1: 
            counter += 1
        # do the right shift
        n = n >> 1
    return counter
    """
    
    bin_representation = bin(n)
    counter = 0
    for i in range(bin_representation):
        if bin_representation[i] == "1":
            counter+= 1
    return counter

print(hamming_weight(20))