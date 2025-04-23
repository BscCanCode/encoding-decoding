import string
import random

word=input("Enter the word:") #treordwert
prefix=''.join(random.choices(string.ascii_lowercase,k=3))
suffix=''.join(random.choices(string.ascii_lowercase,k=3))
output=prefix+word[1:]+word[0]+suffix
print(output)
choice=input("Would you like to decode the word? yes/no:")
if choice=="yes":
    if output.startswith(prefix) and output.endswith(suffix):
        core=output[3:-3]
        decoded=core[-1]+core[:-1]
        print(decoded)
elif choice=="no":
    print("The word is not decoded:",output)
else:
    print("Enter proper input")
    
