





user_input= input("Provide each unique word here: ")
user_input2= input("The number of times each respective word appears: ")
words=user_input.split()
frecuency=user_input2.split()

word_count={}
word_count[words[0]]=frecuency[0]
word_count[words[1]]=frecuency[1]
word_count[words[2]]=frecuency[2]
word_count[words[3]]=frecuency[3]
check_word=input("Wich word would you like to check? ")
word_exists=check_word in word_count
print("The word '{}' is in the dictionary: {} ".format(check_word,word_exists))

