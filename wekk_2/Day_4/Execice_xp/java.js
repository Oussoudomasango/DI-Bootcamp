// Exercice 1
console.log("exercice1");

// partie 1
console.log("partie 1")
function infoAboutMe(){
  console.log("Mon nom est Sango Donald A. O. j'ai 27 ans et j'aime lire pendant mes temps libre et en compagnie d'amis ");
  console.log ("On passe du temps sur les Play Station.");  
};
infoAboutMe();

console.log(" ");
// partie 2
console.log("partie 2");

function infoAboutPerson (personName, personAge, personFavoriteColor)
{
console.log("Votre nom est : "+ personName + " et vous avez "+ personAge + " ans " );
console.log ("Votre couleur préférer est : " + personFavoriteColor );
};
// utilisation de la fonction

console.log("Utilisation de la fonction");
console.log(" ");
infoAboutPerson("David", 45, "blue");
console.log(" ")
infoAboutPerson("Josh", 12, "yellow");

console.log(" ");
// exercice 3 
console.log("Exercice 2");

function calculateTip() 
{
let montant = prompt("veuillez entrer le montant de la facture") ;
parseFloat(montant);
console.log(montant);
let valeur = 0;
    if (montant< 50)
    {
         valeur =  montant*1.2 ;
        console.log("la somme totale dépenser est : " + valeur);
    }
    else if ((montant>50) && (montant<200 ))
    {
         valeur = montant*1.15; 
        console.log("la somme totale dépenser est : " + valeur);
    }
    else
    {
         valeur = montant*1.1 
        console.log("la somme totale dépenser est : " + valeur);
    }
};
calculateTip();

// Exercice 3 
console.log("Exercice 3");
console.log(" ");

function isDivisible(){
    var x=0;
    sum=0;
    console.log("les nombre inferieurs à 500 et divisible par 23 sont : ");
    while(x<=500){
        if (x%23==0){
            console.log(x);
            sum=sum+x;
        }
        x++;
    }
    console.log("la somme de ces nombre vaut :" + sum);
}
isDivisible();

console.log(" ");
//Exercice 4;
console.log("Exercice 4");

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = {
    "banana" : 1, 
    "apple" : 1, 
    "orange" : 1
};
var montant = 0 ;
function myBill() {

    for (x in shoppingList) 
    {
        if (stock[x] !=0 ){
            console.log("le prix de " + x + " est" + prices[x] + " fcfa");
            stock[x]= stock[x]-1;
            montant = montant + prices[x];
            
        }
        
    }
    return montant;
};
let prix = myBill();
console.log("Le prix total est : " + prix );
