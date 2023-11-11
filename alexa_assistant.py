#Link replit
https://replit.com/join/oewvrnrsij-maria-fernan901

def detect_alexa(text):
  #SPLIT THE TEXT TEXT INTO WORDS
  words = text.split()

  #COUNT THE OCURRENCES OF ALEXA
  alexa_count = words.count("Alexa")

  #Check the count and provide the response
  if alexa_count == 1:
    return "Tell me , how can I help you?"
  elif alexa_count == 2:
    return "Hey, just say my name once"
  else:
    return "Hey, just say my name once"

#Input user
text= input("Input: ")

#Fuction and response
response = detect_alexa(text)

#output
print(response)
