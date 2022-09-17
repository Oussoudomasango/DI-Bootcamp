/* Exercice 1*/
console.log("Exercice 1");
console.log(" ");


// question 1

console.log(document.querySelectorAll('[selected]'));
var choisi=document.querySelectorAll('[selected]')[0].value
console.log(choisi)
alert(choisi)

// question 2
console.log(" ");
newoption=document.createElement("option");
newoption.setAttribute("value","classic");
newText= document.createTextNode("classic");
newoption.appendChild(newText);
console.log(newoption);
document.getElementById("genres").appendChild(newoption);

// question 4
console.log(" ");
document.getElementById("genres").children[2].selected=true;
console.log(document.getElementById("genres").children[2]);