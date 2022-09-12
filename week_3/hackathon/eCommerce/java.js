/* parties Java et DOM */

// ici nous avons une fonction qui vérifie que le client a bien donner un nombre
// après avoir vérifier le nombre il donne le prix du produit
function valeur(prix)
{
    let val = prompt("Veuillez entrer le nombre de produit désire");
    console.log(isNaN(val));
    console.log(typeof(val));
    if(isNaN(val))
    { 
        console.log("on est dans le if")
        console.log(" ");
        console.log(typeof(val));
        console.log(val); val=parseFloat(prompt("La Valeur entrer est incorrecte. Veuillez mettre une nouvelle valeur"));
        // boucle qui oblige le client à mettre un nombre
        while(isNaN(val))
        {
            val=parseFloat(prompt("Veuillez entrer un nombre: "));
            if(val == null)
                break
        }
        let totale = val * prix; 
        alert(" le prix totale est : " + totale + "  Fcfa");
        return totale;
       
    }
    else 
    {
        console.log("on est dans le else if")
        console.log(" ");
        console.log(val);
        let totale = val * prix;
            alert(" le prix totale est : " + totale + "  Fcfa");
            return totale;
    }
}
//var x= valeur(prix);