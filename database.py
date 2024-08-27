import pymysql
from tkinter import messagebox


def connect_database():
    global mycursor,conn
    try:
        conn=pymysql.connect(host='localhost',user='root',password='pdk789' )
        mycursor=conn.cursor()
        #print('connect connected')
    except:
        messagebox.showerror('Error','Somthing went wrong ,Please open app before running again')
        return
    
    mycursor.execute('create database if not exists employee_data')
    mycursor.execute('use employee_data')
    mycursor.execute('create table if not exists data (Id varchar(20), Name varchar(50), phone varchar(15), role varchar(20), gender char(6), salary decimal(10,2))')

def search(option,value):
    try:
        conn=pymysql.connect(host='localhost',user='root',password='pdk789' ,database='employee_data')
        mycursor=conn.cursor()
        #print('connect connected')
    except:
        messagebox.showerror('Error','Somthing went wrong ,Please open app before running again')
    mycursor.execute(f'select * from data where {option}=%s',value)
    result=mycursor.fetchall()
    return result


def insert(id,name,phone,role,gender,salary):
    ex=mycursor.execute('SELECT * FROM data WHERE Id=%s',(id))
    if ex==0:
        mg=messagebox.askyesno('alert','Do u want to insert Data')
        if mg==True:
            mycursor.execute("insert into data values(%s,%s,%s,%s,%s,%s)",(id,name,phone,role,gender,salary))
            conn.commit()
            conn.close()
            messagebox.showinfo('Success','Data Inserted')
            
    else:
        messagebox.showerror('Error','Id already exist')

   
def fetch_employees():
    try:
        conn=pymysql.connect(host='localhost',user='root',password='pdk789' )
        mycursor=conn.cursor()
        #print('fetch connected')
    except:
        messagebox.showerror('Error','Somthing went wrong ,Please open app before running again')
        return
    mycursor.execute('use employee_data')
    mycursor.execute('select * from data')
    result=mycursor.fetchall()
    #print(result)
    
    return result



def update(new_name,new_phone,new_role,new_gender,new_salary,id):
    try:
        conn=pymysql.connect(host='localhost',user='root',password='pdk789',database='employee_data' )
        mycursor=conn.cursor()
        #print('update connected')
    except:
        messagebox.showerror('Error','Somthing went wrong ,Please open app before running again')
        return
   
    mycursor.execute('use employee_data')
    #mycursor.execute('set SQL_SAFE_updates = 0')
    try:

        mycursor.execute('update data set name=%s,phone=%s,role=%s,gender=%s,salary=%s where id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
        messagebox.showinfo('Success','Data updated')
    except:
         messagebox.showerror('Error','Somthing went wrong ,Please open app before running again')
   
    conn.commit()
    mycursor.execute('select * from data')
    p=mycursor.fetchall()
    # for i in p :
    #     print(i)
    # print(new_name,new_phone,new_gender,new_role,new_salary,id)
    conn.close()



def delete(id):
    try:
        conn=pymysql.connect(host='localhost',user='root',password='pdk789',database='employee_data' )
        mycursor=conn.cursor()
        #print('connected')
    except:
        messagebox.showerror('Error','Somthing went wrong ,Please open app before running again')
        return
   
    mycursor.execute('use employee_data')
    #mycursor.execute('set SQL_SAFE_updates = 0')
    try:

        mycursor.execute('DELETE FROM data where id=%s',(id))
        messagebox.YESNOCANCEL('Success','Data Deleted')
    except:
        #print('not Deleted')
        messagebox.showerror('Error','Somthing went wrong ,Please open app before running again')
   
    conn.commit()
    mycursor.execute('select * from data')
    mycursor.fetchall()
    
    conn.close()
    
def delete_all():
    try:
        conn=pymysql.connect(host='localhost',user='root',password='pdk789',database='employee_data' )
        mycursor=conn.cursor()
        #print('connected')
    except:
        messagebox.showerror('Error','Somthing went wrong ,Please open app before running again')
        return
   
    mycursor.execute('use employee_data')
    #mycursor.execute('set SQL_SAFE_updates = 0')
    try:
        mycursor.execute('TRUNCATE TABLE data')
        messagebox.YESNOCANCEL('Success','Deleted all Data')
    except:
        messagebox.showerror('Error','Somthing went wrong ,Please open app before running again')
        #print('not Deleted')
    conn.commit()
    mycursor.execute('select * from data')
    mycursor.fetchall()
    
    conn.close()
def search_result(field,search_entry):
    try:
        conn=pymysql.connect(host='localhost',user='root',password='pdk789' )
        mycursor=conn.cursor()
        #print('fetch connected')
    except:
        messagebox.showerror('Error','Somthing went wrong ,Please open app before running again')
        return
    mycursor.execute('use employee_data')
    mycursor.execute('select * from data where %s=%s',(field,search_entry))
    result=mycursor.fetchall()
    
    
    return result


    


#connect_database()