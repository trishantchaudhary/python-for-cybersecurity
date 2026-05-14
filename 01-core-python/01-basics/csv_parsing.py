import csv


data = [


    ['name','email','phone'],
    ['trishant','trishant@gmail.com','445345'],
    ['x','t@gmail.com','435435']

     
]


#with open("o.csv", "w", newline='' ) as file:
#   writer = csv.writer(file)
#    writer.writerows(data)




with open("o.csv", "w", newline='') as x:
    csv.writer(x).writerows(data)

# both ways are good


print("[+] data written to o.csv")





# reading from csv file

with open("o.csv","r") as f:
    for row in csv.reader(f):
        print(row)

# or simplified way is

# x = csv.reader(f)
# for row in x:
# print(row)





###################### csv to dictionary #############

with open("x.csv", "w", newline="") as file:
    fields = ["name","email","phone"]
    writer = csv.DictWriter(file, fieldnames=fields)



    writer.writeheader()


    writer.writerows([
        {"name": "Ghost", "email": "ghost@cyber.com", "phone": "1234"},
        {"name": "Trishant", "email": "trish@hackmail.com", "phone": "5678"}
    ])




with open("x.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)


