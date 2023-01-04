import sys
from Logic import logic

def main():
    args = sys.argv[1:]
        

    if (len(args) != 5):
        print ("error:Enter atleast 5 words")
        print ("usage:Please enter 5 words")

    else:
        Words = []
        Words = args

        objL = logic()
        objP = DisplayValues
         
    DisplayValues("Original List",Words)
    DisplayValues("ReversedList",objL.ReversedList(Words))
    DisplayValues("Sorted List",objL.SortedList(Words))
    DisplayValues("Randomised List",objL.Randomise(Words))


def  DisplayValues (heading, Words):
    print(heading)
    print("-----------------------------")
    for word in Words:
        print(word)
        
         
if __name__ == '__main__':
    main()
