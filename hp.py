
# Online Python - IDE, Editor, Compiler, Interpreter
name = str(input("Hello!, what is your name?"))
while name == "":
    name = str(input(": "))
print("Hello!",name,("nice to meet you"))
any =str(input("How are you doing?"))
while any == "":
    any =str(input("How are you doing?"))
print("I'm also ",any)
name =(input("Where do you come from?"))
while name == "":
    name =(input("Where do you come from?"))
print("ooh,I also come from ",name)
any =str(input("Which place do you know there?",))
while any == "":
    any =str(input("Which place do you know there?",))
print("wow, I also know",any, ",infact that's where I come from?")
yes=str(input("can we be friends?"))
while yes == "":
    yes=str(input("can we be friends?"))
print("sure why not.")
name =input("so where do you study?")
while name == "":
    name =input("so where do you study?")
print("wow!",name,".That school is the best")
x =str(input("who do you know there?"))
while x == "":
    x =str(input("who do you know there?"))
print("is",x,"good?")
n =str(input("okay,we will keep in touch..."))
while n == "":
    n =str(input("okay,we will keep in touch..."))
print("TRY THIS OUT")
# ("LET'S START")

words = []
# range()
n =int(input("How many items can you write?"))
for y in range(1,n+1):
  n =str(input(f"Enter the word  . {y}"))
  print(n)
  words.append(n)

print(words)