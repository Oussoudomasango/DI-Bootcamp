/*Exercice*/
console.log("Exercice");
console.log(" ");

function calculateTip()
{
    var billAmount=document.getElementById("billamt").value;
    billAmount=parseInt(billAmount);
    console.log(billAmount)
    var serviceQuality=document.getElementById("serviceQual").value;
    serviceQuality=Number(serviceQuality);
    console.log(serviceQuality)
    var numberOfPeople=document.getElementById("peopleamt").value;
	numberOfPeople=parseInt(numberOfPeople)
	console.log(numberOfPeople);
    if(!billAmount ||serviceQuality===0)
    { 
    alert("il y une valeur incorrecte");
    }
    else
     {
    if(!numberOfPeople||numberOfPeople<1){
            numberOfPeople=1;
            console.log(numberOfPeople);		
    }
    var total=((billAmount*serviceQuality)/numberOfPeople);	
    total.toFixed(2)
    console.log(total)
    document.getElementById("totalTip").style.display="block";
    document.getElementById("tip").innerHTML=total;	
    }
   
}

document.getElementById("totalTip").style.display="none"

document.getElementById("calculate").addEventListener("click",function(event){
    event.preventDefault()
    });
    document.getElementById("calculate").setAttribute("onclick","calculateTip()")
