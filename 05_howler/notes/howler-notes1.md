## Reading File 

`os` module has may methods to finding files, directiories and more.

```python3

#check if balargh is  a file and return as false.
os.path.isfile('balargh') 

file = '/var/lib/db.txt'
#Returns /var/lib as the directory name of the file 
os.path.dirname(file)


#Returns db.txt as the file name in the varible 
os.path.basename(file)

#A file handle must be open() to read() the file 
fh = open(file)

```
# UNSAFE CODE 
** Never  try to open a file without checking if it exist.** 
>>> fh = open(file)
>>> file = 'blargh
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  FileNotFoundError: [Errno 2] No such file or directory: 'blargh'

## Always check the file

file = 'inputs/fox.txt'
if os.path.isfile(file):
    fh = open(file)


