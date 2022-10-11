class Phone():
    def __init__(self,name):
        self.name=name
        self.call_history=[]
        self.messages=[]
        
    def add(self,string):
        self.call_history.append(string)
        
    def add2(self,string):
        self.messages.append(string)
        
    def name(self):
        return self.name
        
    def Call(self,other_phone1,other_phone):
        cname='you have call '+other_phone1
        rname='you receive a call from '+self.name
        self.call_history.append(cname)
        other_phone.add(rname)
        
    def show_call_history(self):
        for i in self.call_history:
            print(i)
            
    def send_message(self,other_phone1,other_phone,content):
        dic={'to':other_phone1,'content':content}
        self.messages.append(dic)
        dic2={'from':self.name,'content':content}
        other_phone.add2(dic2)
    
    def show_messages(self):
        for i in self.messages:
            print(i)
            
    def show_outgoing_messages(self):
        for i in self.messages:
            for j in i.keys():
                if j=='to':
                    print(i)
                    
    def show_incoming_messages(self):
        for i in self.messages:
            for j in i.keys():
                if j=='from':
                    print(i)

Naruto=Phone("Naruto")
Lee=Phone('Lee')
Naruto.Call(Lee.name,Lee)
Naruto.send_message(Lee.name,Lee,'Hi guy How are you')
Lee.send_message(Naruto.name,Naruto,'Yeah guy i\'m okay and you')
Naruto.send_message(Lee.name,Lee,'I\'m pretty fine what\'s going on ? long time ago')
Lee.send_message(Naruto.name,Naruto," ohhh that's right man i'm pretty busy those time")
Naruto.send_message(Lee.name,Lee,"Ah I see, then let's see us on friday ")
Lee.send_message(Naruto.name,Naruto,"Okay let's do it")
Naruto.send_message(Lee.name,Lee,'Nice')
Lee.Call(Naruto.name,Naruto)

print('\n')
print("Naruto call history : ")
Naruto.show_call_history()
print('\n')
print("Lee call history : ")
Lee.show_call_history()
print('\n')
print("Harold messages : ")
Naruto.show_messages()
print("outgoings : ")
Naruto.show_outgoing_messages()
print("incomings : ")
Naruto.show_incoming_messages()
print('\n')
print("Ezekiel messages : ")
Lee.show_messages()
print("outgoings : ")
Lee.show_outgoing_messages()
print("incomings : ")
Lee.show_incoming_messages()



