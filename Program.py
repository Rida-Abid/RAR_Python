from ast import Not
import sys
import string
from Logic import logic



def main():
    args = sys.argv[1:]
        
    try:
        if (len(args) < 1):
            print ("error:Enter atleast 2 words")
            print ("usage:Please enter words")
             
        else:
            Words = []
            Words = args
            objL = logic()

            def  DisplayValues (heading, Words):
                print("-----------------------------")
                print(heading)
                print("-----------------------------")
                for word in Words:
                    print(word)
    
      
         
            DisplayValues("Original List",Words)
            DisplayValues("ReversedList",objL.ReversedList(Words))
            DisplayValues("Sorted List",objL.SortedList(Words))
            DisplayValues("Randomised List",objL.Randomise(Words))
    except ValueError:
         for a in args:
             for c in a:
                if (c.isalpha()) == False:
                    print("error:enter words ")
         else:
            print("")


    
        
         
if __name__ == '__main__':
    main()
