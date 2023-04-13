from django.shortcuts import render,redirect
from .models import Menu
from django.contrib.auth.models import User,auth
import psycopg2
# Create your views here.

global flag
global usern
usern=''
flag=0

def index(request):
    global flag
    global usern
    menu = Menu.objects.all()
    return render(request,"index.html",{'menu':menu,'flag':flag,'usern':usern})


def men(request):
    global flag
    global usern
    menu = Menu.objects.all()
    for menus in menu:
        menus.offer_price=round(menus.price*(1-(menus.Offer_per/100)),2)
    return render(request,"menu.html",{'menu':menu,'flag':flag,'usern':usern})


def login(request):
    username = request.POST.get('username')
    pass1 = request.POST.get('pass')


    global conn
    global cursor
    global flag

    global usern

    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="localhost",
                                      port="5432",
                                      database="restaurant")
        cursor = connection.cursor()
        postgreSQL_select_Query = """select * from public."user" """

        cursor.execute(postgreSQL_select_Query)
        records = cursor.fetchall()

        for row in records:
            print(row[1])
            if(str(row[1])==username):
                if(row[2]==pass1):
                    print("granted")
                    usern=row[0]
                    flag=1
        

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    if (flag == 1):
        return render(request,"index.html",{'flag':flag,'usern':usern})
    else:
        return render(request,"login.html")





def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        birthday = request.POST['birthday']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']


        global conn
        global cursor
        global flag

        try:

            conn = psycopg2.connect(user="postgres",
                                    password="1234",
                                    host="localhost",
                                    port="5432",
                                    database="restaurant")
            cursor = conn.cursor()

            postgres_insert_query = """INSERT INTO public."user" (name,username,password,email,gender,birthday,phone) VALUES (%s,%s,%s,%s,%s,%s,%s);"""
            record_to_insert = (name,phone,password,email,gender,birthday,phone)
            cursor.execute(postgres_insert_query, record_to_insert)

            conn.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into mobile table")

        except (Exception, psycopg2.Error) as error:
            if (conn):
                print("Failed to insert record into mobile table", error)


        finally:
            if (conn):
                cursor.close()
                conn.close()
                #print("PostgreSQL connection is closed")

        #print("User Created")
        return redirect('index.html',{'flag':flag,'usern':usern})
    else:
        return render(request,"register.html",{'flag':flag,'usern':usern})
    
    
    
    
def logout(request):
    global flag
    flag=0
    return render(request, "index.html", {'flag': flag,'usern':usern})


def about(request):
    global usern
    global flag
    return render(request,"about.html",{'flag':flag,'usern':usern})


def contact(request):
    global usern
    global flag
    return render(request,"contact.html",{'flag':flag,'usern':usern})


def quanty(request):
    qty = request.GET.get('qty')
    print(qty)
    return qty

def add(request):
    if request.method=="GET":
        iname=request.GET.get('iname')
    qty=quanty(request)
      #  qty=request.GET.get('qty')
    print(iname)
    print(qty)
    return redirect("/menu.html")


def cart(request):
    return render(request,"cart.html")