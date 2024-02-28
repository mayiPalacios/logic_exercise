function countMinJumps(x) {
    let y = 0;
    let jumps = 0;
  
    for (let k = 1; k <= x; k++) {
      y += k;
      jumps++;
      if (y == x) {
        return jumps;
      }
      if (y > x) {
        const isLastTriangularNumber = y - x === 1;
        if (isLastTriangularNumber) {
          return jumps + 1;
        }
        return jumps;
      }
    }
  
    return -1;
  }
  var t = 5;
  let i = 1;
  for (let j = 0; j < t; j++) {
    console.log(i, countMinJumps(i));
    i++;
  }