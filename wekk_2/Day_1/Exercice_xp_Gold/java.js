/*exercice 1*/
console.log("exrcice 1");
let sentence = ["my","favorite","color","is","blue"];
console.log(sentence.join(" "));

/*exercice 2*/
console.log(" ");
console.log("exrcice 2");
console.log(" ");

let str1 = "mix";
let str2 = "pod";
console.log(str1 +" avant le changement");
console.log(str2 +" avant le changement");
// changement des premières lettre
console.log(" ");
let motDécouper1 = str1.substring(0,2);
let motDécouper2 = str2.substring(0,2);
console.log(motDécouper1);
console.log(motDécouper2);
// Echangeons leur place
let motChanger1 = motDécouper1 + str2[2];
let motChanger2 = motDécouper2 + str1[2];
// chaine concatené
let motFinale = motChanger1+ " "+ motChanger2;
console.log(motFinale);


/* exercice 3*/
console.log("exercice 3")
console.log(" ");

let num1 = parseInt(prompt("veuillez entre un nombre"));
let num2 = parseInt(prompt("veuillez entre un nombre"));
alert(num1 + num2);
