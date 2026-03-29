class DatabaseConnection:#creat class
    def __init__(self):#if necessary create init else discard
        pass
        """self.database = database
        self.mode = mode
        self.file = None """#unecessary for current problem

    def __enter__(self):#main block of code, start of code,enter the house

        print("Connecting to database...")
        return self#return self return whole object not self.something, self.something is self.something but self is whole
    def query(self,sql):#normal method
        print(f"Executing: {sql}")
    
    def __exit__(self, exc_type, exc_value, exc_tb):#end of code, exception type,value,traceback
        if exc_type:#if any exception happens
            print("Error Occured")
        print("Closing Connection...")
        return True#end of the block, true ensure something see in note## # ← suppresses the traceback! if you don't want to see long traceback message
with DatabaseConnection() as db:
    db.query("SELECT * FROM users")
with DatabaseConnection() as db:
    db.query("select * FROM orders")
    raise Exception("something went wrong!")#Exception(exc_value), exc_value = something went wrong!


class Own_Cntx_Mngr:
    def __init__(self,filename, mode='r'):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        print('Entered')
        self.cnn = open(self.filename, self.mode)
        return self# ← returns the class, so you can call .read() .write()
    def __exit__(self, exc_type, exc_value, tb):
        self.cnn.close()
        print("Done")
        return 
with Own_Cntx_Mngr('sample.txt','w'):
    print('Do something')

from contextlib import contextmanager
@contextmanager
def file(filename,method):
    file = open(filename,method)
    yield file
    file.close()
with file('150.txt','r') as f:
    print('Mdl')
    #do something with f
    
"""import time
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self,exc_type, exc_value, exc_tb):
        print(f"{(time.time()-self.start):.2f}")
        return False
with Timer():
    sum(range(10000000))   

from contextlib import contextmanager
import time
@contextmanager
def Timer():
    start = time.time()
    yield 
    print(f"{(time.time()-start):.2f}")
with Timer():
    sum(range(10_000_000))
    """

f = open('customers-100.csv','r')
c = f.read()
f = open('sample.txt','w+')
f.write('hellow')
c = f.read()
print(c)
##twt
#working version 
file = open('techwithtim.txt','w')
file.write('this line will run if upper line is correct,then current line will run.but if \
           current line has a problem it will not run and raise a error\
           but for file handling if this line do not run then it will not reach to' \
           'file.close line and it kept open, that is the main problem and to solve that\
           context manager is needed, as it helps to reach a file close method')
file.close()
"""
file = open('tech.txt','w')
file.write('something')v#mistakenly put a 'v' it will raise syntaxt error\nand will not run next line of code
file.close()
#
"""
#simple remedy try ,finally
file = open('techwithtim.txt','w')
try:
    file.write('something')
finally:#this line will run whatever happens to upper block
    file.close()
#what we have used
"""with open('techwith.txt','w') as file:
    file.write('hello')#this block is equivalent to line 23-27
class Open:
    def __init__(self,filename,method):
        self.file = open(filename,method)#self.file = open(filename, method)
        
    def __enter__(self):#main block: all the way it is used
        print("Enter")
        return self.file#this is the object and later it is used with )Open ... as (obj)
    def __exit__(self, type, value, traceback):
        if Exception():
            print(f"{type}, {value}, {traceback}")
        print("Exit")
        self.file.close()

with Open("sample.txt", "w") as f:
    print("Middle")
    f.write("hello!")
#    raise Exception()#this value passed to __exit__()
"""

#AI
import time
class Timer:
    def __enter__(self):
       
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Elapsed: {time.time() - self.start:.2f}s")
        return False  # Don't suppress exceptions

with Timer():
    # do something
    sum(range(10_000_000))
    
"""Note:[all note]
    # Test 1 — normal usage
with DatabaseConnection()[it is returned from created class, if we return self we can apply method from that class or we can return specific things from there] as db[our wish]:
    db.query("SELECT * FROM users")[a method from created class]

# Test 2 — with exception
with DatabaseConnection() as db:
    db.query("SELECT * FROM orders")
    raise Exception("Something went wrong!")
```

---

### Expected Output
```
# Test 1
Connecting to database...
Executing: SELECT * FROM users
Closing connection...

# Test 2
Connecting to database...
Executing: SELECT * FROM orders
Error occurred!
Closing connection...    """
class OwnCntxMngr:
    def __enter__(self):
        print("Entered the first block to return necessary obj/things")
        return self#return self.file = open(filename,mode)
    def __exit__(self, exc_type, exc_value, exc_tb):
        
        #handle error
        if exc_type:
            print("Something went wrong")
        print("Closing")
        #not to show long traceback message
        return True

class OpenFile:
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        self.file = None#not necessary but nice
    def __enter__(self):
        print("entered")
        self.file = open(self.filename,self.mode)# content = open(file,mode)
        return self.file#return content
    def __exit__(self, exc_type, exc, tb):
        self.file.close()#content.close()
        if exc_type:
            print("Error encountered!")
        print("Closed")

obj1 = OpenFile('150.txt','r')
with OpenFile('150.txt','r') as file:
    for line in file:
        print(line)