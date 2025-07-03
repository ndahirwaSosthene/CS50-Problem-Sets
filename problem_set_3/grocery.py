menu = [] #This is the list that will contain the Items that the user will input
seen = set() #this is the set that will track if the item has been printed to prevent 
while True:
    #This loop is a forever loop that will end only once there is a break in its inside condition which in this case is a try & except block.
    try:
        item = input().upper()
        menu.append(item)

    #This will catch catch an exception thrown when function(input) hits an end-of-file condition (EOF) without reading any data.    
    except EOFError:
        print()
        #the for loop will loop through a sorted menu list
        for item in sorted(menu):
            #to help check if an item with multiple occurences is not printed multiple times
            if item not in seen: 
                #print item with occurences before it.
                print(f"{menu.count(item)} {item}") 
                seen.add(item)
        break 