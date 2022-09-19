/*Exercice 3*/
console.log("Exercice 3");
console.log(" ");

var sect1=document.getElementById("box");
sect1.setAttribute('draggable','true');
sect1.setAttribute('ondragstart','dragStart(event)');
var sect2=document.getElementById("target");
sect2.setAttribute('ondrop','dragDrop(event)');
sect2.setAttribute('ondragover','allowDrop(event)');
sect2.setAttribute('ondragenter','allowDrop(event)');
sect2.setAttribute('ondragleave','allowDrop(event)');
function allowDrop(event)
{
    event.preventDefault();
}

function allowEnter(event)
{
    event.target.classlist.add('over');
}

function dragStart(event)
{
    console.log("target:",event.target);
    console.log("box: ",event.target.id);
    event.dataTransfer.setData("text",event.target.id);
}

function dragDrop(event)
{
    event.preventDefault();
    // retrieve the data dragged

    let data = event.dataTransfer.getData("text");
    console.log("data: ", data); // data: square1

    let boxe= document.getElementById(data);
    event.target.appendChild(boxe);
}