# determines if two words are anagrams of each other
import sys

print("Enter the first word:")
word1 = sys.stdin.readline()
print("Enter the second word:")
word2 = sys.stdin.readline()
#sort each word by letters and then compare strings.
word1 = ''.join(sorted(word1))
word2 = ''.join(sorted(word2))
if word1 == word2:
    print("They are anagrams of each other.")
else:
    print("They are not anagrams.")