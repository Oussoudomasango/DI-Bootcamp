# Daily Challenge
print(" Daily Challenge \n");

matrix = [
    ["7","i","3"],
    ["T","s","i"],
    ["h","%","x"],
    ["i"," ", "#"],
    ["s","M"," "],
    ["$","a"," "],
    ["#","t","%"],
    ["^","r","!"]
]

def read(liste,index,*args):
    return liste[index];

message=[]
i=0;
while i<(len(matrix[0])):
    for j in matrix:
        char = read (j,i);
        if char.isalpha():
            message.append(char)
        else:
            message.append(" ")
    
    i+=1;
print("".join(message));