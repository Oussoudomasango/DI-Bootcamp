/* Exercice 1*/
console.log("Exercice 1");
console.log(" ");

let info=document.getElementById("container").innerHTML;
document.getElementsByTagName("li")[1].innerHTML="Richard";
document.getElementsByTagName("li")[0].innerHTML="Donald";
document.getElementsByTagName("li")[2].innerHTML="Donald";
document.getElementsByTagName("li")[3].remove();

console.log(info.length);
let change2 = document.getElementsByTagName("ul");
console.log(change2[1]);

/* Exercice 2*/  


//console.log(mots.lastElementChild);
//console.log(document.getElementById("container").innerHTML);
//console.log(document.firstChild("div").innerHTML);

//const element = document.getElementById("myList")
//let html = element.lastElementChild.innerHTML;