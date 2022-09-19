/*Exercice 1*/
console.log("Exercice 1");
console.log(" ");

newinput=document.createElement('input');
newinput.setAttribute("placeholder","input only letters please");
newinput.setAttribute("type","text");
newinput.setAttribute("name","text");
newinput.setAttribute("onkeydown","check()");
newinput.addEventListener("click",function(event){
    event.preventDefault()
});
document.body.appendChild(newinput);

function check()
{
    tab=["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
    console.log (tab);
    var choisi= document.body.children[1];
    var verif=false;
    console.log(choisi);
    console.log(choisi.value);
    var i=choisi.value.substring(choisi.value.length-1,choisi.value.length);
    console.log(i)
    for (const elements of tab)
    {
        if (elements === i || elements.toUpperCase() === i )
        {
            verif=true;
            console.log(verif)
        }
    }
    if(verif===false)
    choisi.value=choisi.value.substring(0,choisi.value.length-1);
}