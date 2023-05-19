import os


def addstudent():
    cont="y"
    file=open("student.txt","a")
    while(cont=="y"):
        print("*************************add student*************************")
        id=input("enter student id : ")
        name=input("enter student name : ")
        age=input("enter student age : ")
        file.write(f"{id}\t{name}\t{age}\n")
        print("*************************************************************")
        cont=input("do you want to add another student (y/n) : ")
        if cont!='y':
            file.close()        


            

def readstudent():
    print("**************************Students**************************")
    file=open("student.txt","r")
    for line in file:
        mt=line.split("\t")
        print(f"id : {mt[0]}\tname : {mt[1]}\tage : {mt[2]}")
    file.close()
    print("*************************************************************")

def searchstudent():
    print("**************************Search**************************")
    id=input("enter student id that you want to search for : ")
    file=open("student.txt","r")
    flag=False
    for line in file:
        st=line.split("\t")
        if st[0]==id:
            flag=True
            print("|record found|\n")
            print(f"id : {st[0]} \t name : {st[1]} \t age : {st[2]}")
            print("*************************************************************") 
    if not flag:
        print("|record not found|")
        print("*************************************************************") 

    file.close()    


def updatestudent():
    print("**************************update**************************")
    id=input("enter the id of the record you want to update : ")
    file=open("student.txt","r")
    temp=open("temp.txt","w")
    flag=False
    for line in file:
        st=line.split("\t")
        if st[0]==id:
            flag=True
            id1=input("enter new id : ")
            name=input("enter new name : ")
            age=input("enter new age : ")
            line = id1+"\t"+name+"\t"+age+"\n"
        temp.write(line)
    file.close()
    temp.close()
    os.remove("student.txt")
    os.rename("temp.txt","student.txt")
    if flag:
        print("|record updated|")
    else:
        print("|record not exist|")
    print("*************************************************************") 


def deletestudent():
    print("**************************delete**************************")
    id=input("enter the id of the record that you want to delete : ")
    file=open("student.txt","r")
    temp=open("temp.txt","w")
    flag=False
    for line in file:
        st=line.split("\t")
        if st[0]==id:
            flag=True
        else:
            temp.write(line)
    file.close()
    temp.close()
    os.remove("student.txt")
    os.rename("temp.txt","student.txt")
    if not flag:
        print("|record not exist|")
    else:
        print("|record deleted|")
    print("*************************************************************") 




def addteacher():
    cont="y"
    file=open("teacher.txt","a")
    while(cont=="y"):
        print("*************************add teacher*************************")
        id=input("enter teacher id : ")
        name=input("enter teacher name : ")
        age=input("enter teacher age : ")
        salary=input("enter teacher salary : ")
        enrollment_year=input("enter teacher enrollment year : ")
        file.write(f"{id}\t{name}\t{age}\t{salary}\t{enrollment_year}\n")
        print("*************************************************************")
        cont=input("do you want to add another teacher (y/n) : ")
        if cont!='y':
            file.close()        


            

def readteacher():
    print("**************************teachers**************************")
    file=open("teacher.txt","r")
    for line in file:
        mt=line.split("\t")
        print(f"id : {mt[0]}\tname : {mt[1]}\tage : {mt[2]}\tsalary : {mt[3]}\tenrollment year : {mt[4]}")
    file.close()
    print("*************************************************************")

def searchteacher():
    print("**************************Search**************************")
    id=input("enter teacher id that you want to search for : ")
    file=open("teacher.txt","r")
    flag=False
    for line in file:
        st=line.split("\t")
        if st[0]==id:
            flag=True
            print("|record found|\n")
            print(f"id : {st[0]} \t name : {st[1]} \t age : {st[2]} \t salary : {st[3]} \t enrollment year : {st[4]}")
            print("*************************************************************") 
    if not flag:
        print("|record not found|")
        print("*************************************************************") 

    file.close()    


def updateteacher():
    print("**************************update**************************")
    id=input("enter the id of the record you want to update : ")
    file=open("teacher.txt","r")
    temp=open("tempp.txt","w")
    flag=False
    for line in file:
        st=line.split("\t")
        if st[0]==id:
            flag=True
            id1=input("enter new id : ")
            name=input("enter new name : ")
            age=input("enter new age : ")
            salary=input("enter new salary : ")
            enrollment_year=input("enter new enrollment year : ")

            line = id1+"\t"+name+"\t"+age+"\t"+salary+"\t"+enrollment_year+"\n"
        temp.write(line)
    file.close()
    temp.close()
    os.remove("teacher.txt")
    os.rename("tempp.txt","teacher.txt")
    if flag:
        print("|record updated|")
    else:
        print("|record not exist|")
    print("*************************************************************") 


def deleteteacher():
    print("**************************delete**************************")
    id=input("enter the id of the record that you want to delete : ")
    file=open("teacher.txt","r")
    temp=open("tempp.txt","w")
    flag=False
    for line in file:
        st=line.split("\t")
        if st[0]==id:
            flag=True
        else:
            temp.write(line)
    file.close()
    temp.close()
    os.remove("teacher.txt")
    os.rename("tempp.txt","teacher.txt")
    if not flag:
        print("|record not exist|")
    else:
        print("|record deleted|")
    print("*************************************************************") 



def addsubject():
    cont="y"
    file=open("subject.txt","a")
    while(cont=="y"):
        print("*************************add subject*************************")
        name=input("enter subject name : ")
        id=input("enter teacher id that teachs this subject : ")
        an=input("if there is another teacher teachs this subject press (y) if not press (n) : ")
        if an=='y':
            id1=input("enter teacher id that teachs this subject : ")
            an=input("if there is another teacher teachs this subject press (y) if not press (n) : ")
            
            if an=='y':
                id2=input("enter teacher id that teachs this subject : ")
                an=input("if there is another teacher teachs this subject press (y) if not press (n) : ")
                if an=='y':
                    id3=input("enter teacher id that teachs this subject : ")
            
                else:
                    id3=" "

            else:
                id2=" "        
                id3=" "
        else:
            id1=" "
            id2=" "
            id3=" "
        
        file.write(f"{name}\t{id}\t{id1}\t{id2}\t{id3}\n")
        print("*************************************************************")
        cont=input("do you want to add another subject (y/n) : ")
        if cont!='y':
            file.close()        


            

def readsubject():
    print("**************************Subjects**************************")
    file=open("subject.txt","r")
    for line in file:
        mt=line.split("\t")
        print(f"name of subject : {mt[0]}\nteachers id that teach this subject : {mt[1]}\t\t{mt[2]}\t\t{mt[3]}\t\t{mt[4]}")
        print("-------------------------------------------------------------")
    file.close()
    print("*************************************************************")

def searchsubject():
    print("**************************Search**************************")
    name=input("enter subject name that you want to search for : ")
    file=open("subject.txt","r")
    flag=False
    for line in file:
        st=line.split("\t")
        if st[0]==name:
            flag=True
            print("|record found|\n")
            print(f"name of subject : {st[0]} \t teachers id that teach this subject : {st[1]}\t{st[2]}\t{st[3]}\t{st[4]}")
            print("*************************************************************") 
    if not flag:
        print("|record not found|")
        print("*************************************************************") 

    file.close()    


def updatesubject():
    print("**************************update**************************")
    name=input("enter the name of the record you want to update : ")
    file=open("subject.txt","r")
    temp=open("temppp.txt","w")
    flag=False
    for line in file:
        st=line.split("\t")
        if st[0]==name:
            flag=True
            name1=input("enter new subject name : ")
            id=input("enter new teacher id that teach this subject : ")
            an=input("if there is another teacher teachs this subject press (y) if not press (n) : ")
            if an=='y':
                id1=input("enter teacher id that teachs this subject : ")
                an=input("if there is another teacher teachs this subject press (y) if not press (n) : ")
                if an=='y':
                    id2=input("enter teacher id that teachs this subject : ")
                    an=input("if there is another teacher teachs this subject press (y) if not press (n) : ")
                    if an=='y':
                        id3=input("enter teacher id that teachs this subject : ")
                
                
                    else:
                        id3=" "
                else:
                    id2=" "
                    id3=" "


            else:
                id1=" "
                id2=" "
                id3=" "


            line = name1+"\t"+id+"\t"+id1+"\t"+id2+"\t"+id3+"\n"
        temp.write(line)
    file.close()
    temp.close()
    os.remove("subject.txt")
    os.rename("temppp.txt","subject.txt")
    if flag:
        print("|record updated|")
    else:
        print("|record not exist|")
    print("*************************************************************") 


def deletesubject():
    print("**************************delete**************************")
    name=input("enter the name of the record that you want to delete : ")
    file=open("subject.txt","r")
    temp=open("temppp.txt","w")
    flag=False
    for line in file:
        st=line.split("\t")
        if st[0]==name:
            flag=True
        else:
            temp.write(line)
    file.close()
    temp.close()
    os.remove("subject.txt")
    os.rename("temppp.txt","subject.txt")
    if not flag:
        print("|record not exist|")
    else:
        print("|record deleted|")
    print("*************************************************************") 






c="y"
while c=="y":
    print("----------------------------------------------SCHOOL SYSTEM----------------------------------------------")
    x=eval(input("to enter students system press (1)\nto enter teachers system press (2)\nto enter subjects system press (3)\n-> "))
    if x==1:
        print("----------------------------------------------STUDENTS SYSTEM----------------------------------------------")
        print("To add a student record press             (1)")
        print("To see all students records press         (2)")
        print("To search a student record press          (3)")
        print("To update a student record press          (4)")
        print("To delete a student record press          (5)")
        number=eval(input("-> "))
        match number:
            case 1:
                addstudent()
            case 2:
                readstudent()
            case 3:
                searchstudent()
            case 4:
                updatestudent()
            case 5:
                deletestudent()
    
    
    elif x==2:    
        print("----------------------------------------------TEACHERS SYSTEM----------------------------------------------")
        print("To add a teacher record press             (1)")
        print("To see all teachers records press         (2)")
        print("To search a teacher record press          (3)")
        print("To update a teacher record press          (4)")
        print("To delete a teacher record press          (5)")
        number=eval(input("-> "))
        match number:
            case 1:
                addteacher()
            case 2:
                readteacher()
            case 3:
                searchteacher()
            case 4:
                updateteacher()
            case 5:
                deleteteacher()


    elif x==3:    
        print("----------------------------------------------SUBJECTS SYSTEM----------------------------------------------")
        print("To add a subject record press             (1)")
        print("To see all subjects records press         (2)")
        print("To search a subject record press          (3)")
        print("To update a subject record press          (4)")
        print("To delete a subject record press          (5)")
        number=eval(input("-> "))
        match number:
            case 1:
                addsubject()
            case 2:
                readsubject()
            case 3:
                searchsubject()
            case 4:
                updatesubject()
            case 5:
                deletesubject()



    another=input("do you want to do another operation (y/n) : ")
    if another!="y":
        print(" ---------")
        print("|thank you|")
        print(" ---------")
        break
