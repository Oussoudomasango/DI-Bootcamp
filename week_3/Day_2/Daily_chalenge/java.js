console.log("Daily challlenge");
console.log(" ");
// 1
var mots=document.body.children[1].children[15];
console.log(mots);
mots.addEventListener("click",function(event){
event.preventDefault()
});

var nom1;
var adj1;
var nom2;
var verbe1;
var lieu1;
mots.setAttribute("onclick","vale()")
function vale()
{
    nom1=document.getElementById("noun").value;
    console.log("noun="+nom1);
    adj1=document.getElementById("adjective").value;
    console.log("noun="+adj1);
    nom2=document.getElementById("person").value;
    console.log("noun="+nom2);
    verbe1=document.getElementById("verb").value;
    console.log("noun="+verbe1);
    lieu1=document.getElementById("place").value;
    console.log("noun="+lieu1);


    if(nom1!=='' &&adj1!=='' &&nom2!=='' && verbe1!=='' &&lieu1!=='')
    {
        console.log("Avec une case invalide l'histoire ne sera pa bien vu");
        alert("Avec case nom correcte l'histoire ne sera pas cohérent");
        parg=document.createElement("p");
        newbutton=document.createElement("button");
        newbutton.setAttribute("onclick","nouveau()");
        newTexts= document.createTextNode("clicker ici pour changer l'histoire");
        newbutton.appendChild(newTexts);
        document.body.children[2].appendChild(newbutton);
    
        newText=document.createTextNode("\" "+nom1+" est dans un nouveau défi. Mais il/elle ne sait pas que son amis "+nom2+"  à prévus de l'aider en "+
        verbe1 + "dans un endroit comme "+ lieu1+". Ils sont "+adj1 );
        parg.appendChild(newText);
        console.log(parg);
        document.getElementById("story").appendChild(newText);

}
else
{
    console.log("Il y a des cases incorrecte");
    alert("Il y a des case incorrect veuillez corriger pour afficher l'histoire");

}
}

function nouveau(){
    alert("nous somme ici");
}