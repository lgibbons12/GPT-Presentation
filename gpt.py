import re

import random
import requests

#you just have to shift ctrl v to enter it in
text =  input("Please Enter ChatGPT Text Here: ")

num_of_inputs = input("How Many Words To Change? (Type All For All Words to Change) ")


indices = re.split(" ", text)
if num_of_inputs == "All":
    num_of_inputs = len(indices)
else:
    int(num_of_inputs)
if num_of_inputs > len(indices):
    num_of_inputs = len(indices)

for i in range(num_of_inputs):
    r = random.randint(0, len(indices))
    if 0 <= r < len(indices):
        pass
    else:
        r = len(indices) - 1
        print(indices[r])
    
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(indices[r])
    response = requests.get(api_url, headers={'X-Api-Key': 'Ra4kIEhA16TBeT1DhQz8pQ==kcNK1VKJk5y6QxPO'})
    if response.status_code == requests.codes.ok:
        
        search = re.findall('\["(.*?)"', response.text)
        
        if len(search) > 0:
            indices[r] = search[0]
            print("wiaufhwophfiupowehfoupwehfwuh")
        else:
            pass
        percent = round(i/num_of_inputs, 2) * 100
        print(f"{percent}% Complete")



    else:
        print("Error:", response.status_code, response.text)
   
indices = " ".join(indices)

print(indices)




