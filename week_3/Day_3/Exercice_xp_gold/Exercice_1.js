/* Exercice 1*/
console.log("Exercice 1");
console.log(" ");

var tab=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
newdiv=document.createElement("div");
newdiv.style.height="90vh";
newdiv.style.width="100%";
newdiv.style.display="inline-block";
newdiv.setAttribute("id","content");
newdiv.style.textAlign="center";
var chang=document.body;
chang.style.height="99vh"
chang.appendChild(newdiv);
for (const elements of tab)
{
    noudiv1=document.createElement("div");
    noudiv1.setAttribute("id","boxes"+elements);
    newText=document.createTextNode(elements.toUpperCase()+elements);
    noudiv1.appendChild(newText);
    noudiv1.setAttribute('ondragstart','dragStart(event)');
    noudiv1.setAttribute('ondragend','dragDrop(event)');
    noudiv1.setAttribute('draggable','true');
    noudiv1.style.width="2.4%";
    noudiv1.style.textAlign="center";
    noudiv1.style.display="inline-block";
    noudiv1.style.border="solid 1px black";
    noudiv1.style.marginLeft="1.1%";
    chang.children[1].appendChild(noudiv1);

}

function dragStart(event)
{
    event.target.style.backgroundColor = "lightgreen";
    console.log("drag " + "X: "+ event.clientX + " Y: "+ event.clientY);

}
function dragDrop(event)
{
    event.target.style.backgroundColor = "lightpink";
    var x = event.clientX;
    x=Math.abs(x);
    var y = event.clientY;
    y=Math.abs(y);
    console.log(x);
    console.log(event.clientX)
    console.log(event);
    event.target.style.top= y + "px";
    event.target.style.left = x + "px";
    event.target.style.position="absolute";
    console.log ("dragend" + "X: " + event.clientX  + " Y: " +  event.clientY );
}