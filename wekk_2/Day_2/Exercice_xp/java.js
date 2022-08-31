/* exercice 1*/
let x = 5;
let y = 2;
if (x>y){
    console.log(x);
}
else{
    console.log(y);
}

/* exercice 2*/

let newdog= "Chihuahua";
let nombre= newdog.length;
console.log(nombre);
console.log(newdog.toUpperCase(newdog));
console.log(newdog.toLowerCase(newdog));

if(newdog=="Chihuahua"){
console.log("J’adore les chihuahuas, c’est ma race de chien préférée");
}
else{
    console.log(" Je m’en fiche, je préfère les chats");
}

/* exercice 3*/
let num= prompt("mettez un nombre de votre choix");
console.log(num);
if(num % 2==0){
    console.log(num + " est pair");
}
else{
    console.log(num + " est impaire");
}

/*exercice 4*/

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let numéro = users.length;
let fruit = 'Papayas';

switch (numéro) {
  case 1:
    console.log(users[0]);
    break;
  case 2 :
    console.log(users[0] + " et " + users[1] + " sont en ligne");
    break;
  case 3 :
    console.log(users[0] + " et " + users[1] + " et " + users[2] + " sont en ligne");
    break;
  case 4 :
    console.log(users[0] + " et " + users[1] + " et " + users[2]+ " et " + users[3] + " sont en ligne");
    break;
    default :
    console.log("On" + " ne "+ "sait pas.");
}
