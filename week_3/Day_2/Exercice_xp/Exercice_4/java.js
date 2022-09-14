var mot =document.body.children[1].children[3];
console.log(mot);
var x=document.getElementById("radius");
x.setAttribute("oninput","valeur()");
function valeur()
{
    xx=document.getElementById ("radius").value;
    console.log(xx);
    x.textContent=xx;
    console.log(xx)
    return xx;
}

console.log(x.value);

var mot1=document.body.children[1].children[4];
function calc()
{
    var vale =eval(x.value*x.value*x.value);
    vale=(vale*4*3.14)/3;
    mot.value= vale;
}

var mot1=document.body.children[1].children[4];
document.getElementById("submit").addEventListener("click",function(event){
    event.preventDefault()
});
mot1.setAttribute("onclick","calc()");
