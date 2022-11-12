class Pagination:
    def __init__(self,items,pageSize=10):
        self.items=items
        self.pageSize=pageSize
        self.book=[]
        self.index = 0
    '''
        j'ai definie une methode getBook pour diviser mon livre en page
        la taille d'une page est pageSize qui est egale a 10 par defaut
        les pages seront ainsi append dans une liste Book 
    '''
    def getBook(self):
        for i in range(0,len(self.items),self.pageSize):
            self.book.append(self.items[i:i+self.pageSize])
    def getVisibleItems(self):
             print(self.book[self.index])
             
    #Page suivante
    def nextPage(self):
        self.index+=1
        return self
    
    #Page precedent
    def prevPage(self):
        self.index-=1
    
    #Derniere page
    def lastPage(self):
        self.index=-1
    
    #pages Total
    def totalPages(self):
        print(f"le total des pages: ",len(self.book))
    
    #page Courant
    def currentPage(self):
        print(f"je suis a la page: ",self.index)
    
    #aller a une page donner
    def goToPage(self,page):
        if page > len(self.book):
            self.index=len(self.book)
        if page <= 0:
            self.index = 0
        self.index = page
    
    
    
if __name__=='__main__':
    alphabetList = list("abcdefghijklmnopqrstuvwqyz")
    p = Pagination(alphabetList,4)
    p.getBook()
    #print(p.book)
    p.getVisibleItems()
    p.nextPage()
    p.getVisibleItems()
    p.prevPage()
    p.getVisibleItems()
    p.lastPage()
    p.getVisibleItems()
    p.totalPages()
    p.currentPage()
    p.goToPage(5)
    p.getVisibleItems()
    
    
    
   