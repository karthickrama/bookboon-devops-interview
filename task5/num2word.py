#-----------------------------------------------------
# This code print evey 10 th number in words format
# Used num2words library for number to word conversion
#-----------------------------------------------------

from num2words import num2words

class NumToWords:
    
    def __init__(self, startFrom, endTo):
        
        self.startFrom = startFrom
        self.endTo = endTo


    def numToWords(self,):
        
        i = self.startFrom

        while i <= self.endTo:
            
            if i%10 == 0 and i !=0 :

                print(num2words(i))

            else:

                print(i)   

            i += 1
        return None


def main():
    
    num2Wrd = NumToWords(0,100)
    num2Wrd.numToWords()


if __name__ == '__main__':
    main()