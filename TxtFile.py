text=(open("File.txt")).read()
print("Original string:\n\n",text,"\n")
print("Palindrome string:\n\n",text[::-1],"\n")
print("Every 2nd digit skipped :\n\n",text[::2],"\n")



