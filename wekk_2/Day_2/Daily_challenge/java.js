/* exercice */
let sentence="The movie is not that bad, I like it";
let wordNot=sentence.indexOf("not");
let wordBad=sentence.indexOf("bad");
if(wordNot>wordBad){
    console.log("The movie is good, I like it");
}
else{
    console.log(sentence);
}