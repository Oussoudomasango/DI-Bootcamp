/* info sur java */

document.write("affiche des infos sur la page web"); // document.write permet d'afficher des infos sur la page web

// var permet de déclarer une variable valable sur tout le progrmme java
var age;
var age=5;
// let est une variable locale (valable dans un block de code)
let taille=185;

document.write(taille); // affiche la variable

//on peut utiliser alert aussi pour afficher une variable
alert(age);

// typeof donne la nature de l'élement qu'il indique
document.write(typeof(age));
typeof age;
typeof (taille); // on a deux syntaxe possible

// prompt permet de demander des infos à l'utilisateur. il retourne toujours des string
let name = prompt("comment poy t'appel t'on");

// avec la fonction 
var nam = prompt("comment poy t'appel t'on");
nam = parseInt(nam);
let nature = parseInt(nam); // on peut le ramener en number
// on a aussi parseFloat()

// on aussi confirm
confirm("êtes vous sur que c'est du java");

// !== vérifie si le type est différent il retourne vrai ou si les valeurs sont différentes il retourne vrai
// !== ce opérateur prend les deux (valeur et type) en compte. donc si l'une est différent il donne vrai.
//!== pas bsoin que les deux soits différents pour rendre vrai.

// quelque type primitif
// int float str (chaine de carachtère) 

// <condition> ? <cas_vrai> : <cas_faux>
let number=15;

let res: (number>10) ? "number>10" : "number<10"
document.write(res),=;

// boucle while(){}
 let i=0;

 while(i<5){
    document.write("a");
    i++;
 }

 // boucle do{} while()
 let i=10;
 do{
    document.write("a");
    i++;
 }
 while(i<10);

 // boucle for ( let i=0; i<5 ; ++i;)

 for ( let i=0; i<5 ; i++;){
    document.write("A");
 }

// for ...in
// fon ...of

// si le if est vrai il revient au début de la boucle sans exécuter le reste
//des instructions. En remplaçant le continue par break on arrête la boucle

for ( let i=0; i<5 ; i++;){
    document.write("A");

    if(i===2)
        continue;
    document.write("b");

 }

 // notion de fonction
 // création de fonction function nomdelafonction (on peut mettre des paramètre ou pas){instruction}
 function helloworld()
 {
    document.write("Hello ");
    document.write("World !");

 }

// appele de la fonction pour l'utiliser nomdelafonction (on peut mettre des paramètre ou pas)

helloworld();

// fonction de somme


function sum (nb1, nb2)
{
    document.write(nb1 + nb2);
}
sum(4; 7);

// la fonction produit un resultat que nous recupérons

function sum1 (nb1, nb2)
{
   return nb1 + nb2 ;
} 

let result = sum1(5, 5);
document.write(result);

// possibilité de déclarer des fonctions avec des paramètres variables
function sum (...args){}

// imbirquer une fonctiondans une autre

function som()
{
let info = 18;
// on ne peut pas appeller la fonction somme depuis la boite génerale
// il faut l'appeller dans cette boite et ensutie utiliser la grande 
//fonction pour voir le resultat. mais quand on l'affiche ça s'utilise
// quand même. mais pas visible au document génerale
    function somme ()
    {
        document.write(info);
    }
    somme();
}

som();

// on a la possibilité de déclarer des variable qui reçoivent des fonctions
// commme donné

let sum = function (x, y){ return x + y ; } ;

console.log(sum(45, 17));

document.write(sum(17, 19));

// fonction fléché
// (<arguments>) => {<instructions>}


let sum = (x, y) => { return x + y ; } ;






