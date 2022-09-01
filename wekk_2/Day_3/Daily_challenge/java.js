// exercice

// première manière avec une boucle
console.log("les étoiles affichés avec une boucle");
console. log(" ");

let n = 1 ;
var étoile = ["*"];
    let i = 0;
    do { 
        if (i==0){ 
    console.log(étoile[0]);
        }
        else{
            console.log(étoile.join(" "));
        }

    étoile.push("*");
    i++;
    }while(i<=5);
    
// afficher les étoiles avec des boucles imbriquer
console.log("Afficher les étoiles avec des boucles imbriqués");
console.log(" ");


étoile2 = ["*","*"];
var t = 0;
for(let i = 0; i<2; ++i)
{

    if (i==0) 
    console.log(étoile[0]);
    else{
        console.log(étoile.join(" "));
    }
for (let j = 0; j<2; ++j)
    {
        console.log(étoile2.join(" "));
        étoile2.push("*");
    }    
}











