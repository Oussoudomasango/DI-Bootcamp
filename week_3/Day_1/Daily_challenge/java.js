/*Daily challenge*/
console.log("Daily challenge");
console.log(" ");

var systeme =["Mercure","Venus","Terre","Mars","Jupiter","Saturne","Uranus","Neptune","Pluton"];
let couleur =["indigo","orange","black","red","blue","chocolate","green","yellow","gray"];
let moon=[2,3,1];

for(let i=0;i<systeme.length;i++)
{
    const x = document.createElement("div");
    const m = document.createElement("p2");
    const p = document.createElement("p");
    const y = document.createTextNode(systeme[i]);
    x.appendChild(p);
    x.appendChild(m);
    p.appendChild(y);
    p.style.color='white';
    document.body.firstElementChild.appendChild(x);
    document.getElementsByTagName("div")[i].classList.add("planet");
    document.getElementsByTagName("p2")[i].classList.add("moon");

    document.getElementsByTagName("div")[i].style.backgroundColor=couleur[i];

};
