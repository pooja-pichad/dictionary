emp={1:("Amit",25000),2:("Suman",30000),3:("Ravi",36000)}

pid=int(input("Enter the product id"))

l=[ ]
d={}

if pid in emp:

  l=emp[pid]

  print("Employee id, Employee Name", "\t””Salary")

  print(pid,"\t""\t""\t""\t",l[0],"\t""\t",l[1])


else:
    print("nothing")

