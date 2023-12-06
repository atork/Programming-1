
        
#vars
treeheight,treewidth,emptyspace,emptyspace2,star=None
               
        #take input
        
userinput = int(input("Gimme treeheight"))
        
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
            star = (input-treeheight)*2+1
                
                
                
            #calc spacing
            emptyspace = (treewidth-star)/2
            emptyspace2= emptyspace
                
                #print empty half
            for (emptyspace; emptyspace > 0; emptyspace--):
                    print(" "end='')
                
            for (; star > 0; star--):
                    System.out.print("*");
                
            for (; emptyspace2 > 0; emptyspace2--):
                    print(" "end='');
                


        #nextrow
        print('')

        treeheight=treeheight - 1