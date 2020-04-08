import difflib
# Example 1
# enter 2 texts
text1 = '''  1. Beautiful is better than ugly.
       2. Explicit is better than implicit.
       3. Simple is better than complex.
       4. Complex is better than complicated.
     '''.splitlines(keepends=True)

text2 = '''  1. Beautiful is better than ugly.
       3.   Simple is better than complex.
       4. Complicated is better than complex.
       5. Flat is better than nested.
     '''.splitlines(keepends=True)

# show the differences between 2 texts
d = difflib.Differ()
print("".join(list(d.compare(text1, text2))))

# show the ratio of similarity
s = difflib.SequenceMatcher(None, text1, text2)
s.ratio()

# Above all is the basic applications
# the difflib can also compare the differences between 2 txt files and show the results in the html document
# Example 2
filename1 = '/Users/nina/Desktop/CPS3320desktop/cc1.txt'
filename2 = '/Users/nina/Desktop/CPS3320desktop/cc2.txt'
#open and read the txt files
with open(filename1) as f1, open(filename2) as f2:
    content1 = f1.read().splitlines(keepends=True)
    content2 = f2.read().splitlines(keepends=True)

d = difflib.HtmlDiff()
htmlContent = d.make_file(content1, content2)
#save in the html, and in the html file 
#the red one means the the distinct one in the first file
#the green one means the the distinct one in the second file
#the data with no color means the same one in both 2 files
with open('/Users/nina/Desktop/CPS3320desktop/doc.html', 'w') as f:
    f.write(htmlContent)

#show the ratio
s = difflib.SequenceMatcher(None, content1, content2)
s.ratio()





