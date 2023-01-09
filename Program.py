from ntpath import join
import sys
import string
from Logic import logic



def main():
    args = sys.argv[1:]
        
    if (len(args) < 2):
        print ("error:Enter atleast 2 words")
        print ("usage:Please enter words")
        return

    if (a for a in args if isinstance(a, str) and a.isalpha() == False):
        print("error:enter words only")
       
             
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
    

    
        
         
if __name__ == '__main__':
    main()
