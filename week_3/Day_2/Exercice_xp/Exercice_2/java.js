// Exerxcice 2*/
console.log("Exercice 2");
console.log(" ");

console.log(document.getElementsByTagName('form')[0]);
console.log(" ");

console.log(document.getElementById("fname"));
console.log(document.getElementById("lname"));

console.log(" ");
console.log(document.querySelectorAll('[name]'));
document.getElementById("submit").addEventListener("click",function(event)
{
    event.preventDefault()
});

var changer =document.body.children[0].children[9];
changer.setAttribute("onclick","ajouter()");
console.log(changer);
function ajouter()
{
    var prenom=document.getElementById("fname").value;
    var nomFamille=document.getElementById("lname").value;
    console.log(prenom + " " + nomFamille);
    if(prenom!=="" && nomFamille!=="")
    {
        console.log("valid input");
        newli1=document.createElement("li");
        newTextNode1= document.createTextNode(prenom);
        console.log(newTextNode1);
        newli1.appendChild(newTextNode1);
        console.log(newli1);
        newli2=document.createElement("li");
        newTextNode2=document.createTextNode(nomFamille);
        console.log(newTextNode2);
        newli2.appendChild(newTextNode2);
        console.log(newli2);
        change4=changer=document.body.children[1];
        change4.appendChild(newli1);
        change4.appendChild(newli2);
        console.log(change4);

    }
    else
    {
        console.log("on of values is invalid try again");
        alert("one or both values are invalid try again");
    }
}