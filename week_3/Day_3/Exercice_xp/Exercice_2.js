/*Exercice 2*/
console.log("Exercice 2");
console.log(" ");

var i=0;
var j;
function myMove()
{
    console.log("you are here");
    j=setInterval(anime,1);
}
var t=document.body.children[1].scrollWidth-document.body.children[1].children[0].scrollWidth;
function anime()
{
    if(i<t)
    {
        i=i+1;
        document.getElementById("animate").style.left=i+"px";
    }
    else{
        clears(j);
    }
}
ss=document.body.children[1].scrollWidth;
console.log(ss);
function clears(j)
{
    clearInterval(j);
}