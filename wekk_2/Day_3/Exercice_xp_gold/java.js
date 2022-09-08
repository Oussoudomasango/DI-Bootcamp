/*Exercice 1*/
console.log("Exercice 1");
console.log(" ");

let numbers = [123, 8409, 100053, 333333333, 7];
let taille=numbers.length;

// verifier si le nobre est divisible par 3 et afficher vrai ou faux en fonction du résultat

for (let i=0;i<taille;i++)
{
    if(numbers[i]%3==0)
    {
        console.log(true);
    }
    else
    console.log(false);
}

/*Exercice 2*/
console.log(" ");
console.log("Exercice 2");
console.log(" ");

// vérifier si le nom de l'utilisateur est dans la base que nous on a

let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  }
  //"Hi! I'm [name], and I'm from [country]."
  var vérifier = prompt("Veuillez entrer votre nom");
  for(let x in guestList)
  {
    if(x==vérifier)
    { 
        console.log("Hi! I'm "+ x +", and I'm from "+ guestList[x] );
        break;
    }
    else if (x!=vérifier)
    {
        console.log("Hi! I'm a guest.");
    }

}

/*Exercice 3*/
console.log(" ");
console.log("Exercice 3");
console.log(" ");

let age = [20,5,12,43,98,55];
let tail = age.length;
var sum=0;
var gran=0;
for (let i=0; i<tail;i++)
{
    sum= sum + age[i];
    if(age[i]>gran)
    gran=age[i];
}
console.log("la somme est :" + sum);
console.log("Le plus grand nombre parmis eux est : " + gran );
