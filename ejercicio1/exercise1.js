function isPalindrome(word) {
    const newWord = word.replace(/[\W_]/g, '').toLowerCase();
    const reverseNewWord = newWord.split('').reverse().join('').replace(/[\W_]/g, '');
    return newWord === reverseNewWord;
}

console.log(isPalindrome("radar"));
console.log(isPalindrome("anita lava la tina"));
console.log(isPalindrome("Yo dono rosas, oro no doy"));
console.log(isPalindrome("a man, a plan, a canal, Panama!"));
console.log(isPalindrome("Machine learning"));