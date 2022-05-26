# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True





def find_anagram(word, anagram):
    # Get lengths of both strings
    s1 = len(word)
    s2 = len(anagram)
  
    # If length of both strings is not 
    # same, then they cannot be anagram
    if s1 != s2:
        return 0
  
    # Sort both strings
    word = sorted(word)
    anagram = sorted(anagram)
  
    # Compare sorted strings
    for i in range(0, s1):
        if word[i] != anagram[i]:
            return 0
  
    return 1
  
# Driver code
word = "silent"
anagram = "listen"
  
# Function Call
if areAnagram(word, anagram):
    print(
    "True")
else:
    print(
    "False")
