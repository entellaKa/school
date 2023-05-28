from tkinter import *
from tkinter import ttk, messagebox, font
from PIL import ImageTk,Image
import pymysql
import requests
from io import BytesIO
from datetime import datetime

id=""
con = pymysql.connect(host='localhost', user='root', password='0000',db='동물원', charset='utf8') # 한글처리 (charset = 'utf8')
url = 'https://raw.githubusercontent.com/entellaKa/school/hojae/secondGrade/databaseProject/{}.png?raw=true'

#로그인/로그아웃
def Logout():
    global id
    if id == "":
        Login()
    else:
        loginButton['text']="로그인"
        id = ""

#관리자 모드

def admin():
    adminWindow=Tk()
    adminWindow.title("관리자 모드")
    adminWindow.geometry("700x400")

    menu=ttk.Notebook(adminWindow, width=300, height=300)

    frame1=Frame(adminWindow)
    frame2=Frame(adminWindow)
    frame4=Frame(adminWindow)
    frame5=Frame(adminWindow, padx=20)
    frame6=Frame(adminWindow)

    #동물관리
    #동물(개체/종류)추가

    def addAnm():
        addAnmWindow=Tk()
        addAnmWindow.title("동물 개체 등록")

        #동물 개체 추가
        name=Label(addAnmWindow,text="이름")
        name.grid(row=2, column=0)

        nameentry=Entry(addAnmWindow)
        nameentry.grid(row=2, column=1)

        gender=Label(addAnmWindow,text="성별")
        gender.grid(row=4,column=0)
        gender=IntVar()

        genderM=Radiobutton(addAnmWindow, text='남',variable=gender, value=0)
        genderF=Radiobutton(addAnmWindow, text='여',variable=gender, value=1)

        genderM.grid(row=4, column=1,sticky='w',padx=50)
        genderF.grid(row=4, column=1,sticky='e',padx=50)

        birth=Label(addAnmWindow,text="생년월일")
        birth.grid(row=6, column=0)

        birthframe=Frame(addAnmWindow)
        birthframe.grid(row=6, column=1)

        yearBox=ttk.Combobox(birthframe,height=0, width=4, values=[i for i in range(1950,2023)])
        yearBox.grid(row=0, column=0)

        year=Label(birthframe,text="년")
        year.grid(row=0, column=1)

        monthBox=ttk.Combobox(birthframe, height=0, width=4, values=[i for i in range(1,13)])
        monthBox.grid(row=0, column=2)

        month=Label(birthframe,text="월")
        month.grid(row=0, column=3)

        dayBox=ttk.Combobox(birthframe, height=0, width=4, values=[i for i in range(1,32)])
        dayBox.grid(row=0, column=4)

        day=Label(birthframe,text="일")
        day.grid(row=0, column=5)

        breed=Label(addAnmWindow,text="품종")
        breed.grid(row=9, column=0)

        breedentry=Entry(addAnmWindow)
        breedentry.grid(row=9, column=1)

        tamer=Label(addAnmWindow,text="담당 사육사")
        tamer.grid(row=10, column=0)

        tamerentry=Entry(addAnmWindow)
        tamerentry.grid(row=10, column=1)

        #이름 생일 번호 성별 사육사
        def animalRegisterFunc():
            birth = "{}-{}-{}".format(yearBox.get(), monthBox.get(), dayBox.get())
            selectBreedNoSQL = "select 동물번호 from 종류 where 종류 = '{}'".format(breedentry.get())
            selectTamerNoSQL = "select 직원번호 from 직원 where 이름 = '{}'".format(tamerentry.get())
            cur = con.cursor()
            cur.execute(selectBreedNoSQL)
            breed = cur.fetchone()
            cur.execute(selectTamerNoSQL)
            tamer = cur.fetchone()
            print(birth, breed[0], gender.get(), tamer[0])
            insertSqQL = "insert into 동물 values(0,'{}','{}','{}','{}','{}')".format(nameentry.get(), birth, breed[0], gender.get(), tamer[0])
            cur.execute(insertSqQL)
            con.commit()
            messagebox.showinfo("동물등록", "새로운 동물이 추가되었습니다")

        register=Button(addAnmWindow, text="등록하기", command=animalRegisterFunc)
        register.grid(row=11, column=1, sticky=W+E+N+S)

    #동물 종류 추가
    def addBreed():
        addBreedWindow=Tk()
        addBreedWindow.title("동물 품종 추가")

        breed=Label(addBreedWindow,text="품종")
        breed.grid(row=2, column=0)

        breedEntry=Entry(addBreedWindow)
        breedEntry.grid(row=2, column=1)

        food=Label(addBreedWindow,text="먹이")
        food.grid(row=4, column=0)

        foodEntry=Entry(addBreedWindow)
        foodEntry.grid(row=4, column=1)

        zone=Label(addBreedWindow,text="구역")
        zone.grid(row=6, column=0)

        zoneEntry=Entry(addBreedWindow)
        zoneEntry.grid(row=6, column=1)

        #품종 먹이 구역
        def breedRegisterFunc():
            selectBreedNoSQL = "select 구역번호 from 구역 where 구역이름 = '{}'".format(zoneEntry.get())
            cur = con.cursor()
            cur.execute(selectBreedNoSQL)
            area = cur.fetchone()
            insertSqQL = "insert into 종류 values(0,'{}','{}',{});".format(breedEntry.get(), foodEntry.get(), area[0])
            cur.execute(insertSqQL)
            con.commit()
            messagebox.showinfo("동물등록", "새로운 종류가 추가되었습니다")


        register=Button(addBreedWindow, text="추가하기", command=breedRegisterFunc)
        register.grid(row=8, column=1, sticky=W+E+N+S)

    addAnmButton=Button(frame1,text="새로운 동물 개체\n등록하기",command=addAnm ,bg="white")
    addBreedButton=Button(frame1,text="새로운 동물 종류\n추가하기",command=addBreed ,bg="white")

    addAnmButton.pack(fill="both",expand=True,side="left",pady=50,padx=10)
    addBreedButton.pack(fill="both",expand=True,side="right",pady=50,padx=10)


    #직원관리
    #직원 추가/삭제
    def manageStaff():
        addStaffWindow=Tk()
        addStaffWindow.title("직원 추가")

        #직원 등록
        name=Label(addStaffWindow,text="이름")
        name.grid(row=2, column=0)

        nameentry=Entry(addStaffWindow)
        nameentry.grid(row=2, column=1)

        birth=Label(addStaffWindow,text="생년월일")
        birth.grid(row=4, column=0)

        birthframe=Frame(addStaffWindow)
        birthframe.grid(row=4, column=1)

        yearBox=ttk.Combobox(birthframe,height=0, width=4, values=[i for i in range(1950,2023)])
        yearBox.grid(row=0, column=0)

        year=Label(birthframe,text="년")
        year.grid(row=0, column=1)

        monthBox=ttk.Combobox(birthframe, height=0, width=4, values=[i for i in range(1,13)])
        monthBox.grid(row=0, column=2)

        month=Label(birthframe,text="월")
        month.grid(row=0, column=3)

        dayBox=ttk.Combobox(birthframe, height=0, width=4, values=[i for i in range(1,32)])
        dayBox.grid(row=0, column=4)

        day=Label(birthframe,text="일")
        day.grid(row=0, column=5)

        phone=Label(addStaffWindow,text="전화번호")
        phone.grid(row=6, column=0)

        phoneentry=Entry(addStaffWindow)
        phoneentry.grid(row=6, column=1)

        address=Label(addStaffWindow,text="주소")
        address.grid(row=8, column=0)

        address=Entry(addStaffWindow)
        address.grid(row=8, column=1)

        account=Label(addStaffWindow,text="계좌번호")
        account.grid(row=10, column=0)

        account=Entry(addStaffWindow)
        account.grid(row=10, column=1)

        def registeration():
            birth = "{}-{}-{}".format(yearBox.get(), monthBox.get(), dayBox.get())
            cur = con.cursor()
            insertSqQL = "insert into 직원 values(0,'{}','{}','{}','{}','{}','{}');".format(nameentry.get(),birth,phoneentry.get(), address.get(), account.get(),datetime.now().date())
            cur.execute(insertSqQL)
            con.commit()
            messagebox.showinfo("직원등록", "직원이 등록되었습니다")

        register=Button(addStaffWindow, text="등록하기", command=registeration)
        register.grid(row=12, column=1, sticky=W+E+N+S)

    #직원 검색/삭제
    def searchStaff():
        searchStaffWindow=Tk()
        searchStaffWindow.title("직원 검색")

        searchS=Label(searchStaffWindow,text="직원명")
        searchS.grid(row=2, column=0)

        searchSEntry=Entry(searchStaffWindow)
        searchSEntry.grid(row=2, column=1)

        def search():
            cur = con.cursor()
            sql = "select 이름, 생년월일, 핸드폰번호, 주소 , 계좌번호, 입사일 from 직원 where = '{}'".format(searchSEntry.get())
            cur = con.cursor()
            cur.execute(sql)
            staff = cur.fetchall()
            for i in staff:
                staffTable.insert("","end", i[0], text=0, values=i)

        def delete():
            value = staffTable.item(staffTable.focus())
            cur = con.cursor()
            insertSqQL = "delete from 직원 where 이름 = '{}'".format(value["values"][0])
            cur.execute(insertSqQL)
            con.commit()
            messagebox.showinfo("직원등록", "삭제되었습니다")

        searchButton=Button(searchStaffWindow,text="검색", command=search)
        searchButton.grid(row=2, column=2)

        register=Button(searchStaffWindow, text="삭제하기", command=delete)
        register.grid(row=8, column=1, sticky=W+E+N+S)

        staffColumn = ["이름", "생년월일","핸드폰번호", "주소","계좌번호","입사일"]
        staffTable = ttk.Treeview(searchStaffWindow, columns=staffColumn)
        staffTable.column("#0",width=0, anchor="center")
        for i in staffColumn:
            staffTable.column(i, width=90, anchor="center")
            staffTable.heading(i, text=i)

        sql = "select 이름, 생년월일, 핸드폰번호, 주소 , 계좌번호, 입사일 from 직원"
        cur = con.cursor()
        cur.execute(sql)
        staff = cur.fetchall()
        for i in staff:
            staffTable.insert("","end", i[0], text=0, values=i)
        staffTable.grid(row=3,column=0, columnspan=3)
    
    addStaffButton=Button(frame2,text="새로운 직원\n등록하기",command=manageStaff ,bg="white")
    manageStaffButton=Button(frame2,text="직원 관리/보고서",command=searchStaff ,bg="white")

    addStaffButton.pack(fill="both",expand=True,side="left",pady=50,padx=10)
    manageStaffButton.pack(fill="both",expand=True,side="right",pady=50,padx=10)


    addAnmButton=Button(frame1,text="새로운 동물 개체\n등록하기",command=addAnm ,bg="white")
    addBreedButton=Button(frame1,text="새로운 동물 종류\n추가하기",command=addBreed ,bg="white")

    #고객관리
    #회원 정보(아이디, 비밀번호, 이름, 생년월일, 휴대전화번호)
    userColumn = ['아이디',' 비밀번호',' 이름',' 생년월일',' 핸드폰번호','포인트','등급']
    userTable = ttk.Treeview(frame4, columns=userColumn)
    userTable.column("#0",width=0, anchor="center")
    userTable.heading("#0", text="번호")

    for i in userColumn:
        userTable.column(i, width=90, anchor="center")
        userTable.heading(i, text=i)
    
    sql = "select 아이디, 패스워드, 이름, 생년월일, 핸드폰번호, 포인트, 등급.등급 from 회원 inner join 등급 on 회원.등급번호 = 등급.등급번호"
    cur = con.cursor()
    cur.execute(sql)
    users = cur.fetchall()

    for user in users:
        userTable.insert("","end", user[0], text=0, values=user)
    userTable.pack()

    #예매관리

    #예약목록 테이블
    rsvColumn =["예약자명","예약일자","인원"]
    rsvtable=ttk.Treeview(frame5, columns=rsvColumn)

    rsvtable.column("#0",width=0, anchor="center")
    rsvtable.heading("#0", text="index")

    for i in rsvColumn:
        rsvtable.column(i,width=90, anchor="center")
        rsvtable.heading(i, text=i)

    rsvtable.pack(fill="both")
    
    sql = "select 이름, 입장시기, 동행인_성인, 동행인_아이, 가격 from 회원, 입장객 where 아이디 = 회원번호"
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for i in rows:
        rsvtable.insert("","end",text=0, values=[i[0], i[1], i[2]+i[3], i[4]])

    #동물보고서
    animalColumn = ["이름","생일","종류","성별","사육사","먹이","구역"]
    animalTable = ttk.Treeview(frame6, columns=animalColumn)
    
    for i in animalColumn:
        animalTable.column(i, width=90, anchor="center")
        animalTable.heading(i, text=i)

    sql = "select 동물.이름, 동물.생일, 종류.종류, 동물.성별, 직원.이름, 종류.먹이, 구역.구역이름 from 동물, 직원, 종류, 구역 where 동물.동물번호 = 종류.동물번호 and 동물.담당사육사 = 직원.직원번호 and 종류.구역번호 = 구역.구역번호"
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    animalTable.column("#0", width=0)
    for i in rows:
        animalTable.insert("","end", id=i[0], values=i)
    animalTable.pack()

    menu.add(frame1,text="동물 관리")
    menu.add(frame2,text="직원 관리")
    menu.add(frame6,text="동물 보고서")
    menu.add(frame4,text="고객 보고서")
    menu.add(frame5,text="예매 보고서")

    menu.pack(fill="both")

    adminWindow.mainloop()

#회원가입
def sign():
    idCheck = False
    signWindow = Tk()
    signWindow.geometry("320x178-50+50")
    
    ID=Label(signWindow,text="ID")
    ID.grid(row=0, column=0)

    IDentry=Entry(signWindow)
    IDentry.grid(row=0, column=1)

    def checkID():
        cur = con.cursor()
        sql = "SELECT 아이디 FROM 회원 where 아이디='"+IDentry.get()+"'"
        cur.execute(sql)
        rows = cur.fetchall()
        if len(rows)==0:
            messagebox.showinfo("중복확인","사용 가능한 아이디입니다.")
            IDentry['state']="disabled"
            idCheck = TRUE
        else:
            messagebox.showinfo("중복확인","이미 존재하는 아이디입니다.")

    IDCheck=Button(signWindow, text="중복확인", command=checkID)
    IDCheck.grid(row=0, column=2)

    PW=Label(signWindow,text="PW")
    PW.grid(row=1,column=0)

    PWentry=Entry(signWindow, show="*")
    PWentry.grid(row=1, column=1)

    PWCheck=Label(signWindow,text="PW 확인")
    PWCheck.grid(row=2,column=0)

    PWCheckentry=Entry(signWindow, show="*")
    PWCheckentry.grid(row=2, column=1)

    name=Label(signWindow,text="이름")
    name.grid(row=3, column=0)

    nameentry=Entry(signWindow)
    nameentry.grid(row=3, column=1)

    birth=Label(signWindow,text="생년월일")
    birth.grid(row=4, column=0)

    birthframe=Frame(signWindow)
    birthframe.grid(row=5, column=1)

    yearBox=ttk.Combobox(birthframe,height=0, width=4, values=[i for i in range(1950,2023)])
    yearBox.grid(row=0, column=0)

    year=Label(birthframe,text="년")
    year.grid(row=0, column=1)

    monthBox=ttk.Combobox(birthframe, height=0, width=4, values=[i for i in range(1,13)])
    monthBox.grid(row=0, column=2)

    month=Label(birthframe,text="월")
    month.grid(row=0, column=3)

    dayBox=ttk.Combobox(birthframe, height=0, width=4, values=[i for i in range(1,32)])
    dayBox.grid(row=0, column=4)

    day=Label(birthframe,text="일")
    day.grid(row=0, column=5)

    phone=Label(signWindow,text="휴대폰")
    phone.grid(row=6, column=0)

    phoneentry=Entry(signWindow)
    phoneentry.grid(row=6, column=1)

    def signUp():
        birth="{}-{}-{}".format(yearBox.get(),monthBox.get(),dayBox.get())
        if idCheck==False:
            messagebox.showinfo("가입실패","중복 확인이 필요합니다.")

        elif IDentry.get()!="" and PWentry.get()!="" and nameentry.get()!="" and phoneentry.get()!= "":
            cur = con.cursor()
            sql = 'insert into 회원 values("{}","{}","{}","{}","{}",0,1)'.format(IDentry.get(), PWentry.get(), nameentry.get(), birth, phoneentry.get())
            cur.execute(sql)
            sql="select * from 회원"
            cur.execute(sql)
            rows = cur.fetchall()
            con.commit()
            messagebox.showinfo("가입완료","가입이 완료되었습니다.")
            signWindow.destroy()
        else:
            messagebox.showinfo("가입실패","기입되지않은 항목이 있습니다.")

    # IDentry=Entry(signWindow)
    # IDentry.grid(row=0, column=1)
    sign=Button(signWindow, text="가입", command=signUp)
    sign.grid(row=8, column=1, sticky=W+E+N+S)

#로그인 창
def Login():
    loginWindow = Tk()
    loginWindow.title("로그인")
    loginWindow.geometry("215x64+50+50")
    
    memberID=Label(loginWindow,text="ID")
    memberID.grid(row=0, column=0)

    IDentry=Entry(loginWindow)
    IDentry.grid(row=0, column=1)

    memberPW=Label(loginWindow,text="PW")
    memberPW.grid(row=1,column=0)

    PWentry=Entry(loginWindow, show="*")
    PWentry.grid(row=1, column=1)

    def loginF():

        sql="select * from 회원 where 아이디='{}' && 패스워드='{}'".format(IDentry.get(),PWentry.get())
        cur=con.cursor()
        cur.execute(sql)
        result=cur.fetchone()
        if result!=None:
            messagebox.showinfo("로그인 완료","로그인 되었습니다.")
            global id
            id=IDentry.get()
            loginWindow.destroy()
            loginButton["text"]="로그아웃"
        else: 
            messagebox.showerror("에러","아이디/비밀번호를 다시 확인하여 주세요")

    Login=Button(loginWindow, text="로그인",command=loginF)
    Login.grid(row=0, column=2, rowspan=2,sticky=W+E+N+S)

    signup=Button(loginWindow, text="회원가입", borderwidth=0, command=sign)
    signup.grid(row=2, column=1, sticky="e")
    
    loginWindow.mainloop()


#홈 화면

window=Tk()
window.title("Tukorea Zoo")
window.geometry("500x400+300+200")

titleframe=Frame(window)

font1=font.Font(size=40)
titletext="TuKorea Zoo"
titlecolor=["#5c89ec","#d04f40","#edbc43"]
title=[]

for i in range(len(titletext)):
    title.append(Label(titleframe, text=titletext[i], fg=titlecolor[i%len(titlecolor)],font=font1,compound="top"))
    title[i].pack(side="left")

menu=ttk.Notebook(window, width=400, height=300)

loginframe=Frame(window)
loginButton = Button(loginframe, text="로그인", command=Logout)

adminButton=Button(loginframe, text="관리자모드", borderwidth=0, command=admin)
adminButton.pack(side="left")

frame1=Frame(window)
frame2=Frame(window)
frame3=Frame(window)
frame4=Frame(window)

menu.add(frame1,text="동물원 소개")
menu.add(frame2,text="동물정보")
menu.add(frame3,text="예매")
menu.add(frame4,text="예매 내역")

#동물원 소개
def mapA():
    mapAWindow=Tk()
    mapAWindow.title("꼬마동물마을")

    mapAFrame = Frame(mapAWindow)

    cur = con.cursor()
    sql = "select 이름 from 동물,종류 where 구역번호 = 1 and 동물.동물번호 = 종류.동물번호"
    cur.execute(sql)
    rows = cur.fetchall()

    for i in rows:
        res = requests.get(url.format(i[0]))
        image.append(ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100))))
        pic = Label(mapAFrame, image=image[i])
        pic.pack()

def mapB():
    mapBWindow=Tk()
    mapBWindow.title("원숭이마을")

    mapBFrame = Frame(mapBWindow)

    cur = con.cursor()
    sql = "select 이름 from 동물,종류 where 구역번호 = 2 and 동물.동물번호 = 종류.동물번호"
    cur.execute(sql)
    rows = cur.fetchall()

    for i in rows:
        res = requests.get(url.format(i[0]))
        image.append(ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100))))
        pic = Label(mapBFrame, image=image[i])
        pic.pack()

def mapC():
    mapCWindow=Tk()
    mapCWindow.title("코끼리마을")

    mapCFrame = Frame(mapCWindow)

    cur = con.cursor()
    sql = "select 이름 from 동물,종류 where 구역번호 = 3 and 동물.동물번호 = 종류.동물번호"
    cur.execute(sql)
    rows = cur.fetchall()

    for i in rows:
        res = requests.get(url.format(i[0]))
        image.append(ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100))))
        pic = Label(mapCFrame, image=image[i])
        pic.pack()

def mapD():
    mapDWindow=Tk()
    mapDWindow.title("맹수마을")

    mapDFrame = Frame(mapDWindow)

    cur = con.cursor()
    sql = "select 이름 from 동물,종류 where 구역번호 = 4 and 동물.동물번호 = 종류.동물번호"
    cur.execute(sql)
    rows = cur.fetchall()

    for i in rows:
        res = requests.get(url.format(i[0]))
        image.append(ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100))))
        pic = Label(mapDFrame, image=image[i])
        pic.pack()

def mapE():
    mapEWindow=Tk()
    mapEWindow.title("초식동물마을")

    mapEFrame = Frame(mapEWindow)

    cur = con.cursor()
    sql = "select 이름 from 동물,종류 where 구역번호 = 5 and 동물.동물번호 = 종류.동물번호"
    cur.execute(sql)
    rows = cur.fetchall()

    for i in rows:
        res = requests.get(url.format(i[0]))
        image.append(ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100))))
        pic = Label(mapEFrame, image=image[i])
        pic.pack()

def mapF():
    mapFWindow=Tk()
    mapFWindow.title("바다동물마을")

    mapFFrame = Frame(mapFWindow)

    cur = con.cursor()
    sql = "select 이름 from 동물,종류 where 구역번호 = 6 and 동물.동물번호 = 종류.동물번호"
    cur.execute(sql)
    rows = cur.fetchall()

    for i in rows:
        res = requests.get(url.format(i[0]))
        image.append(ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100))))
        pic = Label(mapFFrame, image=image[i])
        pic.pack()

zoofont=font.Font(size=25)
zoolabel=Label(frame1,text="지도",font=zoofont,fg="green",bg="white")
areaframe=Frame(frame1,bg="gold")
# area1button=Button(areaframe,text="A",command=area(1))
# area2button=Button(areaframe,text="B",command=area(2))
# area3button=Button(areaframe,text="C",command=area(3))
# area4button=Button(areaframe,text="D",command=area(4))

areaname = ['꼬마동물마을','원숭이마을','코끼리마을','맹수마을','초식동물마을','바다동물마을']
areacommand=[mapA,mapB,mapC,mapD,mapE,mapF]
areabutton = []
for i in range(6):
    areabutton.append(Button(areaframe,text=chr(ord('A')+i)+"구역\n"+areaname[i], bg="green", command=areacommand[i],activebackground="#1dff30"))

areaframe.rowconfigure(tuple(range(3)),weight=1)
areaframe.columnconfigure(tuple(range(2)),weight=1)

#동물 상세 정보
def animalInfo(_name):
    infoWindow = Tk()
    infoWindow.title("동물 정보")

    res = requests.get(url.format(_name))
    image = ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100)))

    nameLabel=Label(infoWindow, text=_name)
    img=Label(infoWindow, image=image)
    img.pack(side="left")
    nameLabel.pack()

#next버튼 prev버튼
page = 0
def paging(b):
    global page
    if b == 1 and page<=n//8:
        cur = con.cursor()
        sql="select 이름 from 동물"
        cur.execute(sql)
        rows = cur.fetchall()
        rows = rows[page*8:(page+1)*8]

        pictures = anmPicFrame.grid_slaves()
        image = []

        for i in range(len(rows)):
            res = requests.get(url.format(rows[i][0]))
            image.append(ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100))))
            pic = pictures[i].pack_slaves()
            pic[0]["image"] = image
        page = page + 1

    elif b == 0 and page>=0:
        cur = con.cursor()
        sql="select 이름 from 동물"
        cur.execute(sql)
        rows = cur.fetchall()
        rows = rows[page*8:(page+1)*8]

        pictures = anmPicFrame.grid_slaves()
        image = []

        for i in range(len(rows)):
            res = requests.get(url.format(rows[i][0]))
            image.append(ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100))))
            pic = pictures[i].pack_slaves()
            pic[0]["image"] = image        
        page = page - 1

#동물정보
loginframe.pack(fill="x")
titleframe.pack()
loginButton.pack(side="right")
menu.pack()

zoolabel.pack(fill="both")
areaframe.pack(fill="both",expand=True)
for i in range(6):
    areabutton[i].grid(row=i%3,column=i//3, sticky="news")

# animalFrame=Frame(frame2, bg="yellow")
# animalFrame.columnconfigure(tuple(range(4)),weight=1)
# animalFrame.pack()

anmPicFrame=Frame(frame2, bg="yellow")
anmPicFrame.pack()
animalname=[]#["사자","토끼","곰"]
cur = con.cursor()
sql="select 이름 from 동물"
cur.execute(sql)
rows = cur.fetchall()
n = len(rows)
rows = rows[:8]

#c = ['red','orange','yellow','green','blue','purple']
image = []

for i in range(len(rows)):
    res = requests.get(url.format(rows[i][0]))
    photoframe=Frame(anmPicFrame, bg="skyblue")
    image.append(ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100))))

    name=Label(photoframe,text=rows[i][0])
    img =Button(photoframe,image=image[i], command=lambda:animalInfo(name["text"]))
    img.pack()
    name.pack()
    photoframe.grid(column=i%4, row=i//4)

anmFrame=Frame(frame2, bg="blue")
anmFrame.pack()

prevButton = Button(anmFrame, text="<", command=lambda:paging(0))
nextButton = Button(anmFrame, text=">", command=lambda:paging(1))
prevButton.pack(side="left")
nextButton.pack(side="right")

#예매
#회원/비회원 예매하기 선택, 날짜, 성인/아이, 도보/차량

#로그인
def memberLoginFunc():
    if id=='':
        messagebox.showerror("에러","로그인 후 다시 시도하여 주세요")
    else:
        resvation()

#경우1) 회원 예매하기 선택 시
#회원 예매하기 창
def resvation():
    reservationwindow=Tk()
    reservationwindow.title("예매 정보 입력하기")
    
    rsvDate=Label(reservationwindow,text="입장 시기")
    rsvDate.grid(row=0, column=0)

    rsvDateframe=Frame(reservationwindow)
    rsvDateframe.grid(row=0, column=2)

    yearBox=ttk.Combobox(rsvDateframe,height=0, width=4, values=[2022,2023])
    yearBox.grid(row=0, column=3)

    year=Label(rsvDateframe,text="년")
    year.grid(row=0, column=4)

    monthBox=ttk.Combobox(rsvDateframe, height=0, width=4, values=[i for i in range(1,13)])
    monthBox.grid(row=0, column=5)

    month=Label(rsvDateframe,text="월")
    month.grid(row=0, column=6)

    dayBox=ttk.Combobox(rsvDateframe, height=0, width=4, values=[i for i in range(1,32)])
    dayBox.grid(row=0, column=7)

    day=Label(rsvDateframe,text="일")
    day.grid(row=0, column=8)

    visitM=Label(reservationwindow,text="방문 방법")
    visitM.grid(row=2,column=0)
    visit=StringVar()
    visit1=Radiobutton(reservationwindow, text='도보',variable=visit, value="walk")
    visit2=Radiobutton(reservationwindow, text='차량',variable=visit, value="car")
    visit1.select()

    visit1.grid(row=2, column=2,sticky='w',padx=40)
    visit2.grid(row=2, column=2,sticky='e',padx=40)

    guestnum=Label(reservationwindow,text='방문 인원')
    guestnum.grid(row=4, column=0)

    adult=Label(reservationwindow, text="성인")
    adultEntry=Entry(reservationwindow, width=10)
    adultEntry.insert(0,"0")
    adultnum=Label(reservationwindow, text="명")

    adult.grid(row=4,column=1,padx=10,sticky='e')
    adultEntry.grid(row=4, column=2,padx=10)
    adultnum.grid(row=4, column=3,padx=10)

    kid=Label(reservationwindow, text="아이")
    kidEntry=Entry(reservationwindow,width=10)
    kidEntry.insert(0,"0")
    kidnum=Label(reservationwindow, text="명")

    kid.grid(row=5,column=1,padx=10,sticky='e')
    kidEntry.grid(row=5, column=2,padx=10)
    kidnum.grid(row=5, column=3,padx=10)

    #결제
    def payment():
        payWindow = Tk()
        payWindow.title("결제")

        adultPrice = Label(payWindow, text="성인: 30,000원(인당)")
        kidPrice = Label(payWindow, text="아이: 25,000원(인당)")
        adultPrice.pack()
        kidPrice.pack()

        paytToolFrame = Frame(payWindow)
        paytTool=Label(paytToolFrame,text="결제 수단")
        paytTool.pack(side="left")
        tool=IntVar()
        tool1=Radiobutton(paytToolFrame, text='카드',variable=tool, value=3)
        tool2=Radiobutton(paytToolFrame, text='모바일',variable=tool, value=2)
        tool3=Radiobutton(paytToolFrame, text='무통장',variable=tool, value=1)
        tool1.select()
        tool1.pack(side="left")
        tool2.pack(side="left")
        tool3.pack(side="left")
        paytToolFrame.pack()

        #가격 인원 할인
        adultno = int(adultEntry.get())
        childno = int(kidEntry.get())
        totalPrice = adultno*30000+childno*25000

        if id!="":
            cur=con.cursor()
            cur.execute("select 할인율 from 등급, 회원 where 아이디 = '{}' and 회원.등급번호=등급.등급번호".format(id))
            discount = cur.fetchone()
            totalPrice = int(totalPrice*(1-discount[0]))

        price = Label(payWindow, text="가격:{}".format(totalPrice))
        price.pack()

        def pay():
            birth = "{}-{}-{}".format(yearBox.get(), monthBox.get(), dayBox.get())
            sql = "insert into 입장객 values(0,'{}',{},'{}','{}',{},{},{})".format(id, tool.get(), datetime.now().date(), birth, adultEntry.get(), kidEntry.get(), totalPrice)
            cur=con.cursor()
            cur.execute(sql)
            sql = "update 회원 set 포인트 = 포인트 + {} where 아이디 = '{}'".format(totalPrice/200, id)
            con.commit()
            messagebox.showinfo("결제 완료","결제가 완료되었습니다.")
            payWindow.destroy()
            reservationwindow.destroy()

        payButton = Button(payWindow, text="결제", command=pay)
        payButton.pack(side="bottom")

        payWindow.mainloop()

    resv=Button(reservationwindow, text="확인", command=payment)
    resv.grid(row=8, column=1, sticky=W+E+N+S, columnspan=2)

    reservationwindow.mainloop()

memberButton=Button(frame3,text="회원\n예매하기",command=memberLoginFunc ,bg="white")

#경우2) 비회원 예매하기 선택 시
#비회원 정보(이름, 생일, 전화번호) 입력 창
def guestinfo():
    guestinfoWindow=Tk()
    guestinfoWindow.title("비회원 정보 입력")

    name=Label(guestinfoWindow,text="이름")
    name.grid(row=3, column=0)

    nameentry=Entry(guestinfoWindow)
    nameentry.grid(row=3, column=1)

    birth=Label(guestinfoWindow,text="생년월일")
    birth.grid(row=4, column=0)

    birthframe=Frame(guestinfoWindow)
    birthframe.grid(row=5, column=1)

    yearBox=ttk.Combobox(birthframe,height=0, width=4, values=[i for i in range(1950,2023)])
    yearBox.grid(row=0, column=0)

    year=Label(birthframe,text="년")
    year.grid(row=0, column=1)

    monthBox=ttk.Combobox(birthframe, height=0, width=4, values=[i for i in range(1,13)])
    monthBox.grid(row=0, column=2)

    month=Label(birthframe,text="월")
    month.grid(row=0, column=3)

    dayBox=ttk.Combobox(birthframe, height=0, width=4, values=[i for i in range(1,32)])
    dayBox.grid(row=0, column=4)

    day=Label(birthframe,text="일")
    day.grid(row=0, column=5)

    phone=Label(guestinfoWindow,text="휴대폰")
    phone.grid(row=6, column=0)

    phoneentry=Entry(guestinfoWindow)
    phoneentry.grid(row=6, column=1)

    register=Button(guestinfoWindow, text="확인", command=resvation)
    register.grid(row=8, column=1, sticky=W+E+N+S)

guestButton=Button(frame3,text="비회원\n예매하기",command=guestinfo,bg="white")

memberButton.pack(fill="both",expand=True,side="left",pady=50,padx=10)
guestButton.pack(fill="both",expand=True,side="right",pady=50,padx=10)


#예매 내역
def guestreceipt():
    if id != "":
        table.delete()
        sql = "select 이름, 입장시기, 동행인_성인, 동행인_아이, 가격 from 회원, 입장객 where 아이디 = 회원번호 and 아이디 = '"+id+"'"
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        for i in rows:
            table.insert("","end",text=0, values=[i[0], i[1], i[2]+i[3], i[4]])
        return 0;
    
    receiptwindow=Tk()

    #이름, 생일, 번호

    guestname=Label(receiptwindow,text="이름")
    guestname.grid(row=0, column=0)

    nameentry=Entry(receiptwindow)
    nameentry.grid(row=0, column=1)

    birth=Label(receiptwindow,text="생년월일")
    birth.grid(row=1, column=0)

    birthframe=Frame(receiptwindow)
    birthframe.grid(row=1, column=1)

    yearBox=ttk.Combobox(birthframe,height=0, width=4, values=[i for i in range(1950,2023)])
    yearBox.grid(row=0, column=0)

    year=Label(birthframe,text="년")
    year.grid(row=0, column=1)

    monthBox=ttk.Combobox(birthframe, height=0, width=4, values=[i for i in range(1,13)])
    monthBox.grid(row=0, column=2)

    month=Label(birthframe,text="월")
    month.grid(row=0, column=3)

    dayBox=ttk.Combobox(birthframe, height=0, width=4, values=[i for i in range(1,32)])
    dayBox.grid(row=0, column=4)

    day=Label(birthframe,text="일")
    day.grid(row=0, column=5)

    guestnumber=Label(receiptwindow,text="전화번호")
    guestnumber.grid(row=2, column=0)

    numberentry=Entry(receiptwindow)
    numberentry.grid(row=2, column=1)

    #예매 내역 확인 버튼
    def receipt():
        name = nameentry.get()
        birth = "{}-{}-{}".format(yearBox.get(), monthBox.get(), dayBox.get())
        number = numberentry.get()
        table.delete()

        sql = "select 이름, 입장시기, 동행인_성인, 동행인_아이, 가격 from 회원, 입장객 where 아이디 = 회원번호 and 이름 = '{}' and 생년월일 = '{}' and 휴대폰번호 = '{}'"
        cur = con.cursor()
        cur.execute(sql.format(name, birth, number))
        rows = cur.fetchall()
        for i in rows:
            table.insert("","end",text=0, values=[i[0], i[1], i[2]+i[3], i[4]])
  
    searchreceipt=Button(receiptwindow, text="확인", command=receipt)
    searchreceipt.grid(row=3, column=1, sticky=W+E+N+S)

    receiptwindow.mainloop()

searchButton=Button(frame4, text="조회하기", command=guestreceipt)

#테이블
columnname=["예약자명","예약일자","인원","가격"]
table=ttk.Treeview(frame4, columns=columnname)

table.column("#0", width=0, anchor="center")
table.heading("#0", text="index")

for i in columnname:
    table.column(i, width=90, anchor="center")
    table.heading(i, text=i)

#table.insert("", "end", text=0, values=["김선재","2022.11.17","3명", "9천억"])

table.pack()
searchButton.pack()

window.mainloop()