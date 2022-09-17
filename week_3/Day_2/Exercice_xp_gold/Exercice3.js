/* Exercice_3 */
console.log("Exercice 3");
console.log(" ");

let articleListe=[];

console.log(" ");
newform=document.createElement("form");
newinput=document.createElement("input");
	newinput.setAttribute("placeholder","your artile")
	newinput.setAttribute("id","val");
newbutton=document.createElement("button");
newText= document.createTextNode("AddItem");
	newbutton.setAttribute("onclick","addItem()");
	newbutton.appendChild(newText);
	newbutton.addEventListener("click",function(event)
    {
	event.preventDefault()
	});
	newform.appendChild(newinput);
	newform.appendChild(newbutton);
	document.getElementById("root").appendChild(newform);

console.log(" ");
function addItem()
{
    var choisi=document.getElementById("val").value ;
    console.log(choisi);
    articleListe[articleListe.length]=choisi;

    console.log("Votre liste de courses");
    for (const element of articleListe) 
    {
        console.log(element);
        alert (element);  
    }
}

console.log(" ");
newbutton2=document.createElement("button");
newText2 = document.createTextNode("clearAll");
	newbutton2.setAttribute("onclick","clearAll()");
	newbutton2.appendChild(newText2);
	newbutton2.addEventListener("click",function(event){
	event.preventDefault()
	});
	document.getElementById("root").appendChild(newbutton2);

    console.log(" ");
    function clearAll(){
        console.log(articleListe)
        articleListe.length=0;
        console.log("votre liste de courses est vide");
        alert("votre liste de courses est vide");
    }
