const countMinJumps = require('./exercise3.js');

describe('Pruebas para countMinJumps con incremento de i en cada iteración', () => {
	test('t=5, i comienza en 1 y se incrementa', () => {
	  let results = [];
	  let i = 1;
	  for (let j = 0; j < 5; j++) { 
		results.push(countMinJumps(i));
		i++;
	  }
	  expect(results).toEqual([1, 3, 2, 3, 4]);
	});
  
	test('t=10, i comienza en 1 y se incrementa', () => {
	  let results = [];
	  let i = 1;
	  for (let j = 0; j < 10; j++) {
		results.push(countMinJumps(i));
		i++; 
	  }
	  expect(results).toEqual([1, 3, 2, 3, 4, 3, 4, 4, 5, 4]);
	});
  
	test('t=11, i comienza en 1 y se incrementa', () => {
	  let results = [];
	  let i = 1;
	  for (let j = 0; j < 11; j++) {
		results.push(countMinJumps(i));
		i++;
	  }
	  expect(results).toEqual([1, 3, 2, 3, 4, 3, 4, 4, 5, 4, 5]); 
	});
  });