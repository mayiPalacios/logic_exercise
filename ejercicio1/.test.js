const isPalindrome = require('./exercise1');


test('radar es un palíndromo', () => {
    expect(isPalindrome("radar")).toBe(true);
});

test('anita lava la tina es un palíndromo', () => {
    expect(isPalindrome("anita lava la tina")).toBe(true);
});

test('Yo dono rosas, oro no doy es un palíndromo', () => {
    expect(isPalindrome("Yo dono rosas, oro no doy")).toBe(true);
});

test('a man, a plan, a canal, Panama! es un palíndromo', () => {
    expect(isPalindrome("a man, a plan, a canal, Panama!")).toBe(true);
});

test('Machine learning no es un palíndromo', () => {
    expect(isPalindrome("Machine learning")).toBe(false);
});
