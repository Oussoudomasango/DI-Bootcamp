let gradesList=[15,17,18,20,17,18,20];
var total=0;
function findAvg(gradesList)
{
    totalnote();
    moyenne();
}

function totalnote ()
{
    for(let i=0;i<gradesList.length;i++)
    totat=total+gradesList[i];
}

function moyenne()
{
    totalnote();
    let moy= total/gradesList.length;
    if (moy>65)
        console.log("success!");
    else
        console.log("failed,you must repeat the course");
}

findAvg(gradesList);