import MySQLdb


print("*****************************************************************************************")
print("Welcome To The General Store")
print("*******************************************************************************************")
def mydata():
    
    print("\n\n\n===================================================================================")
    print("1.Add Your Product     2.See Your Product    3.Total Your Product Price    4.Exit")
    print("===================================================================================")
    ch= int (input("\n Enter Your Choice:  "))

    while(ch!=4):


        if ch==1:
            try:

                mycon=MySQLdb.connect(host="localhost",user="root",password="",database="store")
                nid=int (input("\n Enter Product id :- "))
                name=(input("\n Enter Product Name :- "))
                price=int (input("\n Enter Price of product :- "))
                query="""insert into storeinfo (id ,name,price) VALUES ('{}', '{}','{}');""".format(nid,name,price)
                cur=mycon.cursor()
                cur.execute(query)
                mycon.commit()
                cur.close()
                mydata()
                break
            except:
                print("Error Occuread when Inserting Your values into the Table")
                mydata()
                break
               
        if ch==2:
            

            try:

                mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="store")
                query="SELECT * FROM storeinfo"
                cur=mycon.cursor()
                cur.execute(query)
                tdata=cur.fetchall()
                print("\nYour Product list is : ")
                print("=================================================================================================")
                print("\n\n")
                print("Id: ","\t Price","  Name")
                for row in tdata:
                    a=row[0]  
                    print(row[0],"\t",row[2],"\t ",row[1])
                    print("_______________________________________")    
                print("=================================================================================================")
               
                mydata()
                break    
            except:

                print("Error while fetching the Data! ")
                print("Try Again!!!!!!!")
                
                mydata()
                break
                
        if ch==3:
            try:
                mycon=MySQLdb.connect(host="localhost",user="root",passwd="",database="store")
                cur=mycon.cursor() 
                query="select * from storeinfo"
                cur.execute(query)
                pr=0
                tdata=cur.fetchall()
                for row in tdata:
                    pr=pr+row[2]
                    s=pr
                print("\n\n\n\n***************************************************") 
                print("Online Store Your Bill Invoice: ") 
                print("Total Price of Your Product:-",s)
                print("***********************************************************")
                
                mydata()
                break
            except:
                print("Error Occurred When Fetching Your Data!!!!!!!!!!!!!!!!")
                
                mydata()
                break
            finally:
                with open("TotalPrice.txt",'w') as f:
                    f.write("Total Price of Your Product:-")
                    f.write(str (s))
    if ch==4:
        print("\n\n\n==========================================================================================")
        print("..............................You Are Successfully Exited.................................")
           
                
































mydata()