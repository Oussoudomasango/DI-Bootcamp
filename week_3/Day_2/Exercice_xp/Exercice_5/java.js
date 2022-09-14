

document.getElementsByTagName("p")[0].addEventListener('click',function(){
    normal()
});

function normal() 
{
    document.getElementsByTagName("p")[0].style.padding="10%";
    document.getElementsByTagName('p')[0].style.fontSize="2.5em";
    document.getElementsByTagName('p')[0].style.backgroundColor="green";
    document.getElementsByTagName("p")[0].style.border="1px solid orange"
    document.body.style.backgroundColor='red';
}

document.getElementsByTagName('p')[0].setAttribute("ondblclick","forme1()");
document.getElementsByTagName('p')[0].setAttribute("mouseout","forme2()");
document.getElementsByTagName('p')[0].setAttribute("mouseover","forme3()");

function forme1()
{
    document.getElementsByTagName("p")[0].style.padding="4%";
    document.getElementsByTagName('p')[0].style.fontSize="1.5em";
    document.getElementsByTagName('p')[0].style.backgroundColor="black";
    document.getElementsByTagName("p")[0].style.color="orange";
    document.getElementsByTagName("p")[0].style.border="1px solid red";
    document.body.style.backgroundColor='gray';
}

function forme2()
{
    document.getElementsByTagName("p")[0].style.padding="0";
    document.getElementsByTagName('p')[0].style.fontSize="80%";
    document.getElementsByTagName('p')[0].style.backgroundColor="black";
    document.getElementsByTagName("p")[0].style.color="white";
    document.getElementsByTagName("p")[0].style.border="4px solid red";
    document.body.style.backgroundColor='yellow';
}
function forme3()
{
    document.getElementsByTagName("p")[0].style.padding="4%";
    document.getElementsByTagName('p')[0].style.fontSize="20px";
    document.getElementsByTagName('p')[0].style.backgroundColor="white";
    document.getElementsByTagName("p")[0].style.color="blue";
    document.getElementsByTagName("p")[0].style.margin="8%";
    document.body.style.backgroundColor='black';
}