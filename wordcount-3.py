__author__ = ''
COMMON_WORDS = {"the", "be", "are", "is", "were", "was", "am",
                "been", "being", "to", "of", "and", "a", "in",
                "that", "have", "had", "has", "having", "for",
                "not", "on", "with", "as", "do", "does", "did",
                "doing", "done", "at", "but", "by", "from"}

"""This program counts the number of times each unique word appears in
a text file. The results are output to the command line, and the user
is given the option of printing the results to a new text file."""

user_input = input("Provide words here: ")
results_list=user_input.split()
user_input2= input("Provide more wordws here: ")
results_list2=user_input2.split()
added_results=results_list+results_list2
print(added_results)

appende_input=input("What word would you lik to append?")
added_results.append(appende_input)
print(added_results)
remove_input=input("What word would you like to remove?")
added_results.remove(remove_input)
print(added_results)
# user_input = input("Please enter the path and name of the text file you want"
#                   " to analyze. (E.g.: C:/Users/Monty/Desktop/file.txt):"
#                   "\n")

# common_word = input("Would you like to strip common words from the results? (Y/N) ")

# user_output = input("\nWould you like to output these results to a file? (Y/N) ")
