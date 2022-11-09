//document.getElementById("result").innerHTML=equal();
//equal Function						
						
function equal(){
			let var1 = document.getElementById("result").innerHTML; 
			let var2 = eval(var1) ;
			document.getElementById("result").innerHTML = var2; 
			}

//number Function

function number(numbers){
				document.getElementById("result").innerHTML+=numbers;
				}


//operator Function

function operator(op){
				document.getElementById("result").innerHTML+=op;
				}

//reset Function
				
function reset(){
			document.getElementById("result").innerHTML=" ";
			}

//clear Function

function clears(){
			let len = document.getElementById("result").innerHTML;
			let len2=len.length;
			len=len.substring(0,len2-1);
			document.getElementById("result").innerHTML=len;
			}

