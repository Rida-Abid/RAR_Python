import sys
from Logic import logic

def  DisplayValues (heading, Words):
        print(heading)
        print("-----------------------------")
        for word in Words:
            print(word)

def main():
    args = sys.argv[1:]
        

    if (len(args) < 1):
        print ("error:Enter atleast 2 words")
        print ("usage:Please enter words")
        return 

    Words = []
    Words = args
    objL = logic()
    
      
         
    DisplayValues("Original List",Words)
    DisplayValues("ReversedList",objL.ReversedList(Words))
    DisplayValues("Sorted List",objL.SortedList(Words))
    DisplayValues("Randomised List",objL.Randomise(Words))


    
        
         
if __name__ == '__main__':
    main()
