/* Exercice 2 */
console.log("Exercice 2");
console.log(" ");

console.log(document.getElementById("colorSelect").nextElementSibling);
var choisi_1=document.getElementById("colorSelect").nextElementSibling;
choisi_1.setAttribute("onclick","removecolor()");
function removecolor()
{
    choisi2=document.getElementById("colorSelect").value ;
    console.log(choisi2);
    var partie=document.getElementsByTagName("option");
    for(const elements of partie)
    {
        if(elements.textContent===choisi2)
        elements.outerHTML="";
    }
}