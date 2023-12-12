
        
#vars
treeheight=None
treewidth= None
emptyspace= None
emptyspace2= None
star=None
               
        #take input
        
userinput = int(input("Gimme :"))
        
#Calculate max width
treeheight = userinput
treewidth= treeheight*2+1
        
#print tree
#check not below 1 
if (treeheight>0): 
            
            
    #prints until no more height
    while (treeheight>0): 
        if (treeheight == userinput):
            star= 1
        else:
            star = (userinput-treeheight)*2+1
                
                
                
            #calc spacing
            emptyspace = ((treewidth-star)/2)
            emptyspace2= emptyspace
                
                #print empty half
            while  emptyspace > 0:
                    print(' ',end='')
                    emptyspace -= emptyspace
            while star > 0 :
                    print("*",end='')
                    star -= star
                
            while emptyspace2 > 0 :
                    print(" ",end='')
                    emptyspace2 -= emptyspace2
                


        #nextrow
        print('')

        treeheight-=treeheight