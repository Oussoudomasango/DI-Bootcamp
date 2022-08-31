/*exercice 1*/

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.splice(0,1);
console.log(fruits);
fruits.sort();
console.log(fruits);
fruits.push("Kiwi");
console.log(fruits);
fruits.shift();
console.log(fruits);
let val = fruits[0];
fruits[0]=fruits[1];
fruits[1]=fruits[2];
fruits[2]=val;
console.log(fruits);


/* exercice 2*/

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1]);