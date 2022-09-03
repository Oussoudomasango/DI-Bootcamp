/* Exercice 1*/
console.log ("Exercice 1");
console.log(" ");

let langue = prompt("Quelle est votre langue ?");
let minuscule = langue.toLowerCase(langue);

if(langue=="Français")
console.log("Bonjour!");
else if (langue=="English")
console.log("Hello!");
else if (langue=="Hebrew")
console.log("Shalom");
else
console.log(" 01110011 01101111 01110010 01110010 01111001");


console.log(" ");
/* Exercice 2*/
console.log ("Exercice 2");
console.log(" ");

let note = parseInt(prompt("Quel est votre note ?"));
if(note>90)
console.log("A");
else if (note<=90 && note>80)
console.log(" B ");
else if(note<=80 && note>=70)
console.log(" C ");
else
console.log("D");

console.log(" ");
/* Exercice 3*/
console.log ("Exercice 3");
console.log(" ");

let verbe = prompt("Veuillez Entrer un verbe :");

if(verbe.length>=3)
{
    if(true == verbe.endsWith("ing",verbe.length))
    {
        verbe=verbe+"ly";
        console.log(verbe);
    }
    else{
        verbe=verbe+"ing";
        console.log(verbe);
    }
}
else if (verbe.length<3)
console.log(verbe);