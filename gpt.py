#imports
import re
import random
import requests

#get ChatGPT input
text =  input("Please Enter ChatGPT Text Here: ")

num_of_inputs = input("How Many Words To Change? (Type All For All Words to Change) ")

#splits the text into a array of words
indices = re.split(" ", text)

#logic to make sure num_of_inputs is an integer
if num_of_inputs == "All":
    num_of_inputs = len(indices)
else:
    int(num_of_inputs)
if num_of_inputs > len(indices):
    num_of_inputs = len(indices)

#main loop to edit text
for i in range(num_of_inputs):
    #pick a random word from the array
    r = random.randint(0, len(indices))
    if 0 <= r < len(indices):
        pass
    else:
        r = len(indices) - 1
        print(indices[r])
    
    #sends request to api to find a synonym for the selected word
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(indices[r])
    response = requests.get(api_url, headers={'X-Api-Key': 'Ra4kIEhA16TBeT1DhQz8pQ==kcNK1VKJk5y6QxPO'})
    if response.status_code == requests.codes.ok:
        
        #use re to grab out the synonym
        search = re.findall('\["(.*?)"', response.text)
        
        #passes if there were no synonyms for the word
        if len(search) > 0:
            indices[r] = search[0]
        else:
            pass
        #simple logic to give updates on percent completed
        percent = round(i/num_of_inputs, 2) * 100
        print(f"{percent}% Complete")



    else:
        print("Error:", response.status_code, response.text)
  
#puts the array back into text
indices = " ".join(indices)

#shows newly formed text!
print(indices)




