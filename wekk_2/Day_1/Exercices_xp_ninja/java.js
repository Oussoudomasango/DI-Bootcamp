/* exercice 1*/
    
5 >= 1
// vrai parce que 5 est plus grand que 1
//
    
0 === 1
//faux parce que 0 est différent de 1
//
    
4 <= 1
// faux simplement parce que 1 n'est pas supérieur ni égale à 4
//
    
1 != 1
// 1 égale 1 et pas le contraire donc faux
//

    
"A" > "B"
// faux parce que dans la table ASCII B est plus grand que A
//
    
"B" < "C"
// vrai parce que dans la table ASCII C est plus grand que B
//

    
"a" > "A"
// vrai parce que dans la table ASCII a est plus grand que A
//

"b" < "A"
// faux parce que dans la table ASCII b dépasse A
//

true === false
// faux parce que faux différent bien sûr de vrai mê s'ils sont booléen
//
    
true != true
// faux tout simplement. vrai égale à vrai bien sûr
//

/* exercice 2 */
console.log(" ");
console.log("Exercice 2");
console.log(" ");
/*
let nombre = prompt("veuillez entrer deux nombre séparer par une virgule");
let calcule = nombre.split("");
console.log(calcule);
let valeur = parseInt(calcule[0]) + parseInt(calcule[1]);
console.log(valeur);*/

console.log(" ");
/* Exexrcice 3 */
console.log(" Exercice 3 ");
console.log(" ");

let phrase = prompt("enter une phrase contenant le mot 'Nemo' ");
let mot = phrase.split(" ");
console.log(phrase);
console.log(mot);
console.log("Nemo est à la position : " + mot.indexOf("Nemo"));


console.log(" ");
/* Exexrcice 4 */
console.log(" Exercice 4 ");
console.log(" ");

let nombre = parseInt(prompt("Veuillez entrer un nmobre"));
let mots="boom";
let ajout;
if (nombre<2)
alert(mots)
else if (nombre>2 && nombre%2==0)
{
    ajout="b"+ 'o'.repeat(number) + "m!";
    alert(ajout);
}
else if (nombre>2 && nombre%2!=0)
{
    ajout="b"+'o'.repeat(nombre) + "m";
    alert(ajout);
}
else if (nombre%5==0)
{
    ajout="b"+'o'.repeat(nombre) + "m";
    alert(ajout.toUpperCase(ajout));
}
else if (nombre%2==0 && nombre%5==0)
{
    ajout="b"+'o'.repeat(nombre) + "m!";
    alert(ajout.toUpperCase(ajout));
}