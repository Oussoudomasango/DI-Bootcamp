/* Exercice 3 */
console.log("Exercice 3");
console.log(" ");
document.body.firstElementChild.setAttribute("id","socialNetworkNavigation");
//document.getElementById("navBar").setAttribute("id","autre")

const mo = document.body.firstElementChild.nextElementSibling;

const list = document.getElementsByTagName("li");
const premier=document.createElement("li");
const element = document.createTextNode("Logout");

premier.appendChild(element);
document.getElementById("socialNetworkNavigation").firstElementChild.appendChild(premier);

// document.getElementsByTagName("ul")[0].textContent=list[0].textContent;
// for (let i=0; i<list.length;i++){ 
let i=4;
while(i!=0){
    let x=document.getElementsByTagName("ul")[0];
    x=list[i].style.display='none';
    i--;
}

// }
// document.getElementsByTagName("ul")[0].textContent=list[1].textContent;
