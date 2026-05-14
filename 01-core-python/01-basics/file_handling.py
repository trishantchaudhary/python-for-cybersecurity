#try:
    # risky code
#except Exception as e:
    # just print the error message



# if you want ki koi error hai ya nhi ek specific part always chale to


try:
    #print("trying...")
    x = 10/2

except Exception as e:
    print(f"error is: {e}")

finally:
    print('this will always print becuse of finallyyyyyy')



## open and reading files

## using with open  

#with open("filename.txt", "mode") as file:
    # file operations


# write file


with open("x.txt", "w") as file:
    file.write("hacking is fun!\n")



with open("x.txt", "r") as f:
    c = f.read()
    print(c)


# append file

with open("X.txt", "a") as f:
    f.write("new login attempt from x\n")


with open("x.txt", "r") as x:
    print(x.read())



