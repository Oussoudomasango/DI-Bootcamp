//Exercice 1
var num = 8;
var num = 10;
console.log(num);
// résultat : 10

//Exercice 2
function numbers() {
  for (let i = 0; i < 5; i += 1) {
    console.log(i);
  }
    console.log(i);
}
numbers();

//Exercice 3
//4
function calculTTC(depense,TVA) {
    return depense + (depense*TVA);
}

function affMonRest() {
    //1
    let money = 1500;
    //2
    const TVA = 0.18;
    //3
    let depense = 500;
    //5
    let rest = money - calculTTC(depense,TVA);
    //6
    console.log(rest);
}

affMonRest();

