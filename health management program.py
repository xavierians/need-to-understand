client_list={1: "HAMAD",2: "HARRY",3: "ROHAN"}
lock_list={1: "EXCERCISE",2: "FOOD"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("CHOOSE THE PERSON")
    for key,value in client_list.items():
        print("PRESS",key,"FOR",value)
    client_name=int(input())

    print("SELECTED CLIENT:",client_list[client_name])

    print("ENTER 1 FOR LOCK")
    print("ENTER 2 FOR RETRIEVE")
    op=int(input())

    if op == 1:
        for key,value in lock_list.items():
            print("PRESS",key,"TO LOCK",value)
        lock_name=int(input())
        print("SELECTED JOB:",lock_list[lock_name])
        f=open(client_list[client_name]+"_"+lock_list[lock_name]+".txt","a")
        k='y'
        while k != "n":
            print("ENTER",lock_list[lock_name])
            my_text=input()
            f.write("["+str(getdate())+"]"+my_text)
            k=input("ADD MORE? y/n")
            continue
            f.close()
    elif op == 2:
        for key,value in lock_list.items():
            print("PRESS",key,"TO RETRIEVE", value)
        lock_name=int(input())
        print(client_list[client_name],"-",lock_list[lock_name],"REPORT")
        f=open(client_list[client_name]+"_"+lock_list[lock_name]+".txt","rt")
        contents=f.readlines()
        for line in contents:
            print(line)
        f.close()
    else:
        print("INVALID INPUT")
except Exception as e:
    print("WRONG INPUT")
