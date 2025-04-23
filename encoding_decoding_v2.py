#In this encoding/decoding.v2 now we can take multiple inputs and not by one as its a loop we added exit option to allow user exit if the they wants to!
import string
import random

while True:
    word=input("Enter the word:") #treordwert
    prefix=''.join(random.choices(string.ascii_letters,k=3))
    suffix=''.join(random.choices(string.ascii_lowercase,k=3))
    output=prefix+word[1:]+word[0]+suffix
    print(output)
    choice=input("Would you like to decode the word or exit? yes/no/exit:")
    if choice=="yes":
        if output.startswith(prefix) and output.endswith(suffix):
            core=output[3:-3]
            decoded=core[-1]+core[:-1]
            print(decoded)
    elif choice=="no":
        print("The word is not decoded:",output)
        break
    elif choice=="exit":
        print("Exit is successful!")
        break
    else:
        print("Enter proper input")
    
