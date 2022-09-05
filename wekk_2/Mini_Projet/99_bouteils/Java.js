/* Daily challenge*/
console.log("Daily challenge");
console.log("");
/*99 bottles of beer on the wall
99 bottles of beer
Take 1 down, pass it around
98 bottles of beer on the wall */

var i=0;
var j=0;
var nombre=0;
function playTheSong () { 
do{ 
    nombre = parseInt(prompt("Veuillez entrer le nombre de fois que je dois chanter :"));
}while(isNaN(nombre) || nombre<0);
j = nombre;
var n=0;
var t=0;
for(i=0;i<nombre;i++)
{
    t++;
    if(i==0)
        { 
        console.log(j+ " bottles of beer on the wall");
        console.log(j+ " bottles of beer");
        }
    else if (i>0)
        {
        console.log(j-t+1 + " bottles of beer on the wall");
        console.log(j-t+1 + " bottles of beer");
        }
    console.log("Take "+ t + "down,pass it around");
    console.log(j-t + " bottles of beer on the wall ");
    console.log(" ");

    //t++; 
    if(j==0){
        break;
    }
}
}