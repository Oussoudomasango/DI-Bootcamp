/* exercice 1*/
console.log("Exercice 1");
let people = ["Greg", "Mary", "Devon", "James"];

// supprimer Greg
console.log("supprimer Greg");
people.shift();

//remplacer james par Jason
console.log("remplacer james par Jason");
people[2]= "Jason";

// ajouter mon nom à la fin du tableau
console.log("ajouter mon nom à la fin du tableau");
people.push("Ahldaïr");

//code qui affiche l'index de "Mary"
console.log("code qui affiche l'index de Mary");
console.log(people.indexOf("Mary"));

// code qui copy les noms de "Mary" à mon nom
console.log("code qui copy les noms de Mary à mon nom");
let nomCopier = people.slice(1,3);

// un code qui affiche  l'index de "foo"
console.log("un code qui affiche  l'index de foo");
console.log(people.indexOf("foo"));

// dernier élement du tableau
console.log("dernier élement du tableau");
let taille = people.length;
console.log(taille);

console.log(people[taille-1]);

// Partie 2
console.log("Partie 2");
// on parcours le tableau
console.log("on parcours le tableau");
for(let i = 0; i<=3; ++i)
{
    console.log(people[i]);
}

// on quitte la boucle si "Jason" est affiché
console.log("on quitte la boucle si Jason est affiché");
for(let i = 0; i<=3; ++i)
{
    console.log(people[i]);
    if(people[i]=="Jason" )
    break;
}

// exercice 2

console.log("exercice 2");
// création de tableu qui affiche 5 couleur
console.log("création de tableu qui affiche 5 couleur");

let colors= ["blanc", "bleu", "rouge", "violet","jaune"];
let i = 0;
do{
    console.log(colors[i]);
    ++i;
}while(i<5);

// affiche le tableu avec des termes
console.log(" affiche le tableu avec des termes");
let n = 0;
while(n<5){

    console.log( "Mon choix n °" + n + " est :" + colors[n]);
    ++n;
}
// afficher le tableau avec suffixe
var s = 1;
let suffixe= ["er", "ième"]; 
for(let i = 0; i<=4; ++i)
{
    if (i==0)
        console.log("Mon " + s + suffixe[0] + " choix est " + colors[i] );
    else
        console.log("Mon " + s + suffixe[1] + " choix est " + colors[i] );
    ++s;
}

// exercice 3
console.log("exercice 3");

//demande une numéro au client
console.log ("demande un numéro au client");
/*
var nombre = prompt ("veuillez entrer un numéro");
console.log(typeof(nombre));

//demander à l'utilisateur de saisir un numéro bien que ça soit inférieur à 10;
while (nombre<10){
     nombre  = prompt("veuillez entrer un numéro");
}
*/

// exercice 4
console.log("exercice 4");

let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}

// nombre d'étage dans le batiments
console.log("nombre d'étage dans le batiment:");

console.log(building.numberOfFloors);

// nombre d'apartement au étage 1 et 3
console.log("nombre d'apartement au étage 1 et 3");

console.log(building.numberOfAptByFloor.firstFloor + " est le nombre d'apartement au 1 étage");
console.log(building.numberOfAptByFloor.thirdFloor + " est le nombre d'apartement au 3 étage");

//le nom du deuxième locataire et le nombre de pièces qu'il a dans son apartement
console.log ("info sur le deuxième locataire");

console.log(building.nameOfTenants[1] + " est le deuxième locataire et le nombre de pièces dans sa maison est : " + building.numberOfRoomsAndRent.dan[0] );

// la somme du loyer de Sarah et David est plus importante que celle de Dan. Si c’est le cas, augmentez le loyer de Dan à 1200.
console.log ("comparaison des loyer");
let loyer1= building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] ;
if (loyer1>building.numberOfRoomsAndRent.dan[1])
building.numberOfRoomsAndRent.dan[1] = 1200 ;

// exercice 5
console.log("exercice");

let famille = {
 parent : {
    père : "M Sanou" ,
    mère : "Mme Sanou",

 },
 enfant: {
    garçons: "Amadou",
    fille: "Fanta",
 }
};
//parcourir l'objet 
console.log("Affiche les objets de la famille");

for(let i in famille ){
    console.log(i);
}

//parcourir les valeurs des objets de la famille
console.log ("Afficher les valeurs des objets de famille");
    for(let n in famille)
    console.log(famille[n]);

// exercice 6
console.log("exercice 6");
let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
  for (let n in details) {
    console.log(n + " "+ details[n]);
    
  }

  // exercice 7
console.log ("exercice 7")

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort();
console.log(names);
let premierlettre = [];
let taill = names.length;
console.log(taill);
for(let i = 0; i< taill ; ++i)
{
    premierlettre[i]= names[i].slice(0,1);
}

console.log(premierlettre.join(""));

