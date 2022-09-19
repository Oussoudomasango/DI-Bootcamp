/*Exercice 1*/
console.log("Exercice 1");
console.log(" ");

// 1

function hello(){
    alert("Hello World");
}
setTimeout(hello,2000);

// 2
console.log(" ");

var tabl;
function addp()
{
    new_p=document.createElement("p");
    newText=document.createTextNode("Hello World");
    new_p.appendChild(newText);
    document.getElementById("container").appendChild(new_p);
    tabl=document.getElementsByTagName("p");
    console.log(tabl);
    if(tabl.length===5)
    clears();
}

setTimeout(addp,2000);

//3
console.log(" ");

var itter=setInterval(addp,2000);
document.getElementById("clear").setAttribute("onclick","clears()")
function clears()
{
    clearInterval(itter);
}
