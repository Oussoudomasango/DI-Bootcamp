/* mini projet 1 */
console.log("Exercice 1");
console.log(" ");
var nombre;


function playTheGame()
{
   
    let confirmation= confirm("Est-ce que vous voulez jouer au jeu");
    if(confirmation== true)
    {
        nombre = + prompt("Veuillez entrer un nombre compris entre 0 et 10 :");
        if( isNaN(nombre))
        {
            alert(" Désolé pas un numéro, au revoir");
            playTheGame();
        }
        else if (nombre>10 || nombre<0)
        {
            alert("Désolé, ce n’est pas un bon nombre, au revoir");
            playTheGame();
        }
        else
        {
            let computerNumber = Math.floor(Math.random()*(10-0+1)+0);
            compareNumbers(nombre,computerNumber);
        }       
        
    }
    else { 
    alert("Pas de problème, au revoir");
    playTheGame();
    }
};

        
function compareNumbers(userNumer,computrNumber){
    let i=0;
    do{
        
        if(userNumer==computrNumber)
        { 
        alert("Vous avez gagner")
        break;
        }
        else if (userNumer<computrNumber) 
        {
            alert ("votre nombre est un peu plus petit que celui de l'ordinateur");
            i++;
            if(i==3){
                alert("Looser");
                break;
            }
            userNumer = prompt("Veuillez entrer une nouvelle valeur: ");
            
        
              while(isNaN(userNumer)||(userNumer>10 || userNumer<0))
                { 
                 alert(" Invalide ");
                 userNumer = prompt("Veuillez entrer une nouvelle valeur: ");
                }
             
             
        } 
        else if (userNumer>computrNumber) 
        {
            alert ("votre nombre est un peu plus grand que celui de l'ordinateur");
            i++;
            if(i==3){
                alert("Looser");
                break;
            }
            userNumer = prompt("Veuillez entrer une nouvelle valeur: ");
            
            while(isNaN(userNumer)||(userNumer>10 || userNumer<0))
            { 
             alert(" Invalide ");
             userNumer = prompt("Veuillez entrer une nouvelle valeur: ");
            }
            
                        
        }
                           
        
    }while(i<=3);
    
};


