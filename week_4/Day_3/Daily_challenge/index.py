# Challenge 1
mot=input("Enter a word");
dic={};
for i,v in enumerate(mot):
    if v not in dic:
        dic[v]=[];
    
    dic[v].append(i);
print(dic)


#Chalenge 2

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1000",
  "Fertilizer": "$20",
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

while True:
    mot=input("Type 'quit' to exit or Enter to purchase ");
    if mot.casefold()=="quit":
        break
    else:
        wallet=input ("Enter the amount you have in your wallet");
        list_Product=[];
        for key,value in items_purchase.items():
            price=value[1:]
            if float (price)<= float (wallet):
                list_Product.append(key);
            else:
                pass;
        print(sorted(list_Product));