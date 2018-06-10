print ("----------------------------------")
print ("Welcome to the Pig Latin Generator")
print ("----------------------------------")

pyg = 'ay'

original = "Bevon"
#just suppose the word I input is Bevon

print (original, "is the word you entered")


if len(original) > 0 and original.isalpha():
  #Bevon meets requirements. More characters than 0 and only in letters  
  word = original.lower()
  #Bevon becomes bevon. everything becomes lowercase
  
  first = word[0]
  #first is b since b is the 0 index value in bevon
  
  new_word = word + first + pyg
  #new word is evon since it lost the b + b + ay making it evonbay
  new_word = new_word[1:len(new_word)]

  """yup, this shit works. I dunno I just feel happy I'm learning to
   code and yes I'm spamming the comments but whatever, not like
    its for anyone else to read"""

  second= new_word[0]
  second= second.lower()
  new_word= second+new_word

print(new_word + " is the pig latin for "+ original)
  
else:
     print (original, " was invalid or you didn't input a name. Please try again")

 #well I feel like an idiot because apparently else is invalid and I don't know what's wrong