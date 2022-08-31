/* exercice 1*/
let nourritur="riz";
let midi="dejeuner";
let phrase="Je mange le " + nourritur + "à" + midi;
console.log("Je mange le " + nourritur +" à chaque "  +midi); 

/* Exercice 2*/

// partie 1
let myWatchedSeries= ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength= myWatchedSeries.length
let myWatchedSeriesSentence= "j'ai regarder " + myWatchedSeries[0]
console.log(myWatchedSeriesSentence)

//partie 2

myWatchedSeries.splice(2,1,"friends" );
myWatchedSeries.push("Suite");
myWatchedSeries.splice(0,1,"prison break","black mirror")
myWatchedSeries.splice(1,1);
console.log(myWatchedSeries[1].substring(2,3))
console.log(myWatchedSeries) 

/* exercice 3*/


let temp = 27;
let fah= 0;
fah= (temp/5 )*9 +32;
console.log(fah);

/* exercice 4*/
let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: 55 parce que 34 + 21 font 55
// Actual: 55

a = 2;

console.log(a+b) //second expression
// Prediction: 23. a prend la valeur 2 et on fait a plus b ce qui revient  à 2+21
// Actual: 23

// 1) 55
//2) 23
//3) c n' a pas été defini. en langage c les variables sont souvent initialiser mais en JS je ne sais pas

// 4) le 3+4 donne 7. mais le fait qu'on mette le 5 entre guillemet le transforme en chaine de charactère donc je ne peut pas prévoir le résultats.
// en language c on ne peut pas additionner des entiers avec des chaines de caractères.
// Actual: 75

console.log(3 + 4 + '5');


/*exercice 5*/

typeof(15)
// Prediction: entier
// Actual:number

typeof(5.5)
// Prediction: number
// Actual: number

typeof(NaN)
// Prediction: chaine de caratères
// Actual: number

typeof("hello")
// Prediction: chaine de caractère
// Actual: string

typeof(true)
// Prediction: booléen
// Actual:boolean

typeof(1 != 2)
// Prediction: booléen
// Actual:boolean

"hamburger" + "s"
// Prediction: string
// Actual:string

"hamburgers" - "s"
// Prediction: je ne sais pas. on connais le + mais le - non
// Actual: number

"1" + "3"
// Prediction: string
// Actual:string

"1" - "3"
// Prediction: number
// Actual: number

"johnny" + 5
// Prediction: string
// Actual:string

"johnny" - 5
// Prediction: number
// Actual: number

99 * "hello"
// Prediction: number
// Actual: number

1 != 1
// Prediction: boléen
// Actual:boolean

1 == "1"
// Prediction: boléen
// Actual:boolean

1 === "1"
// Prediction:boléen
// Actual:boolean


/* exercice 6*/

5 + "34"
// Prediction: string
// Actual:string

5 - "4"
// Prediction: umber
// Actual:number

10 % 5
// Prediction:number
// Actual:number

5 % 10
// Prediction: number
// Actual:number

"Java" + "Script"
// Prediction: string
// Actual: string

" " + " "
// Prediction:string
// Actual:string

" " + 0
// Prediction:string
// Actual:string

true + true
// Prediction:number
// Actual: number

true + false
// Prediction: number
// Actual:number

false + true
// Prediction: number
// Actual:number

false - true
// Prediction: number
// Actual:number
console.log(typeof("Bob" - "bill"));
!true
// Prediction:boolean
// Actual:

3 - 4
// Prediction: number
// Actual: number

"Bob" - "bill"
// Prediction: number
// Actual: number