"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open('foo.txt', 'r')
print(f.read())
f.close()
print(f.closed)

# or

with open('foo.txt') as f:
    read_data = f.read()
    print(read_data)

# We can check that the file has been automatically closed.
print(f.closed)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
g = open('bar.txt', 'w+')

for i in range(3):
    if i == 2:
        g.write('This is line {}'.format(i + 1))
    else:
        g.write('This is line {}\n'.format(i + 1))

with open('bar.txt') as g:
    read_data = g.read()
    print(read_data)
