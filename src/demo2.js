/*
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
*/
const hammingWeight = n => {
    const unit = n.toString();
    const unitArr = unit.split("");
    let count = 0
    for (const unit of unitArr) {
        if (unit == 1) count++; 
        else continue;
    }
    return count;
}

console.log(hammingWeight(00000000000000000000000000001000));