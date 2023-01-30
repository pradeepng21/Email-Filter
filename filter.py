import re
import csv

f = open("C:\\Users\\Pradeep_NG\\Desktop\\test_file.txt")

d = []
mail = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
phone = "^[0-9]{1,10}$"
for i in f:
    t = i.split(",")
    
    if re.match(mail,t[0]) and re.match(phone,t[1]):
        d.append(t)


with open(r"C:\\Users\\Pradeep_NG\\Desktop\\test.csv", 'w') as fp:
    write = csv.writer(fp) 
    write.writerows(d)
    print("done")       
        