/* exercice 1*/
let nourritur="riz";
let midi="dejeuner";
let phrase="Je mange le  " + nourritur + "  à  chaque " + midi;
console.log(phrase); 

/* Exercice 2*/

// partie 1
let myWatchedSeries= ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength= myWatchedSeries.length;
let myWatchedSeriesSentence=myWatchedSeries.toString();
console.log( "j'ai regarder 3 series " + myWatchedSeriesSentence);

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
//3) null 

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
// Prediction: boolean
// Actual: number

typeof("hello")
// Prediction: string
// Actual: string

typeof(true)
// Prediction: boolean
// Actual:boolean

typeof(1 != 2)
// Prediction: boolean
// Actual:boolean

"hamburger" + "s"
// Prediction: hamburgers parcqu'il y a eu concatenation
// Actual:hamburgers

"hamburgers" - "s"
// Prediction: indefini
// Actual: Nan

"1" + "3"
// Prediction: 13 car il y a concatenation pour afficher
// Actual:13

"1" - "3"
// Prediction: indefini
// Actual: NaN

"johnny" + 5
// Prediction: indefini
// Actual:johnny5

"johnny" - 5
// Prediction: NaN car on ne peut soustraire un number et un string
// Actual: NaN

99 * "hello"
// Prediction: NaN car on ne peut faire ces genre d'opération
// Actual: NaN

1 != 1
// Prediction: false parce que 1 est égale à 1
// Actual:false

1 == "1"
// Prediction:true 
// Actual:true

1 === "1"
// Prediction:false parce qu'il compare aussi les types
// Actual:false


/* exercice 6*/

5 + "34"
// Prediction: il va faire une concatenation 
// Actual:534

5 - "4"
// Prediction: indefini
// Actual:number

10 % 5
// Prediction:0 parce que le reste de la division donne 0
// Actual:0

5 % 10
// Prediction: 5 parce que le reste de la division donne 5 et le résultat 0
// Actual:5

"Java" + "Script"
// Prediction:'JavaScript' parce que c'est une concatenation de "Java" et "Script"
// Actual: 

" " + " "
// Prediction:"  " c'est une concatenation de 02 espaces vides, c'est comme un stringt
// Actual:

" " + 0
// Prediction:" 0" c'est une concatenation qui se fait
// Actual:" 0"

true + true
// Prediction:2 parce que true correspon aussi à 1, donc 1+1 donne 2
// Actual: 2

true + false
// Prediction: 1 car false correspond à 0 et le true à 1, donc 1+0 donne 1
// Actual:1

false + true
// Prediction: 1 car false correspond à 0 et le true à 1, donc 0+1 donne 1
// Actual:1

false - true
// Prediction: -1 car false correspond à 0 et le true à 1, donc 0-1 donne -1
// Actual:-1
console.log(true + false);
!true
// Prediction:false parce que pas vrai ou non vrai donne l'opposé
// Actual:false

3 - 4
// Prediction: -1 parce que 3-4 donne -1
// Actual: -1

"Bob" - "bill"
// Prediction: NaN
// Actual: NaN