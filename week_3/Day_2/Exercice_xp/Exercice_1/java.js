/* Exercice 1 */
console.log("Exercice 1");
console.log(" ");

let mot=document.body.firstElementChild.firstElementChild;
console.log(mot.textContent);

console.log(" ");
document.body.firstElementChild.lastElementChild.outerHTML=" ";
console.log(document.body.firstElementChild.lastElementChild);

console.log(" ");
console.log(document.body.firstElementChild.firstElementChild.nextElementSibling);
document.body.firstElementChild.firstElementChild.nextElementSibling.setAttribute("onclick","couleur()");

function couleur ()
{
    document.body.firstElementChild.firstElementChild.nextElementSibling.style.backgroundColor="red"
}

console.log(" ");
console.log(document.body.firstElementChild.firstElementChild.nextElementSibling);
document.body.firstElementChild.firstElementChild.nextElementSibling.setAttribute("onclick","clicker()");
function clicker()
{
    document.body.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.style.display="none";
}

console.log(" ");
newbutton=document.createElement("button");
console.log(newbutton);
newbutton.textContent='clicker ici pour mettre le text en gras';
newbutton.setAttribute("onclick","gras()");
function gras()
{
    document.body.style.fontWeight="bold";
}
document.body.appendChild(newbutton);

console.log(" ");

console.log(document.body.firstElementChild.firstElementChild);
document.body.firstElementChild.firstElementChild.setAttribute("onmouseover","dessus()");
function dessus()
{
    var selected = Math.floor(Math.random() * 100);
    console.log(selected);
    document.body.firstElementChild.firstElementChild.style.fontSize=selected+"px";
}
document.body.appendChild(newbutton);



console.log(" ");
console.log(document.body.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling);
var phrase=document.body.firstElementChild.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling;
phrase.setAttribute("onmouseover", "move()");
phrase.setAttribute("class","fade");
bien=document.getElementsByClassName("fade");
function move()
{
    phrase.setAttribute('class',"fade");
    bien=document.getElementsByClassName("fade");

    phrase.style.opacity='1';
    phrase.style.transition='opacity 0.3s ease-in-out';

}
phrase.classList.toggle("bon");