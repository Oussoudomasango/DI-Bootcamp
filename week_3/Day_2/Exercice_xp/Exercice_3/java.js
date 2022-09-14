/* Exercice 3 */
console.log("Exercice 3");
console.log(" ");

var allBoldItems=[];

function getBold_items()
{
    var select=document.getElementsByTagName("strong");
    console.log(select);
    i=-1;
    for (const element of select)
    {
        i=i+1;
        allBoldItems[i]=element;
    }
    console.log(allBoldItems);
}

getBold_items()

function highlight()
{
    for(const elements of allBoldItems)
    elements.style.color="blue";
}



function return_normal()
{
    for (const elements of allBoldItems)
    elements.style.color="black";
}

var mathe=document.body.children[0];
mathe.setAttribute("onmouseover", "highlight()");
mathe.setAttribute("onmouseout", "return_normal()");
console.log(mathe);


