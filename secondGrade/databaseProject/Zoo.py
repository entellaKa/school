from tkinter import *
from tkinter import ttk, messagebox, font
from PIL import ImageTk,Image
import pymysql
import requests
from io import BytesIO

id=""

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

    menu=ttk.Notebook(adminWindow, width=300, height=300)
        
    frame1=Frame(adminWindow)
    frame2=Frame(adminWindow)
    frame3=Frame(adminWindow)
    frame4=Frame(adminWindow)
    frame5=Frame(adminWindow)
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
        gender=StringVar()

        genderM=Radiobutton(addAnmWindow, text='남',variable=gender)
        genderF=Radiobutton(addAnmWindow, text='여',variable=gender)

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

        register=Button(addAnmWindow, text="등록하기")
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

        register=Button(addBreedWindow, text="추가하기")
        register.grid(row=8, column=1, sticky=W+E+N+S)


    
    addAnmButton=Button(frame1,text="새로운 동물 개체\n등록하기",command=addAnm ,bg="white")
    addBreedButton=Button(frame1,text="새로운 동물 종류\n추가하기",command=addBreed ,bg="white")

    addAnmButton.pack(fill="both",expand=True,side="left",pady=50,padx=10)
    addBreedButton.pack(fill="both",expand=True,side="right",pady=50,padx=10)


    menu.add(frame1,text="동물 관리")
    menu.add(frame2,text="직원 관리")
    menu.add(frame3,text="주차 관리")
    menu.add(frame4,text="고객 관리")
    menu.add(frame5,text="예매 관리")
    menu.add(frame6,text="보고서")

    menu.pack()

    adminWindow.mainloop()


    #직원관리
    #직원 추가/삭제
    def manageStaff():
        addAnmWindow=Tk()
        addAnmWindow.title("직원 관리")

        #직원 등록
        name=Label(addAnmWindow,text="이름")
        name.grid(row=2, column=0)

        nameentry=Entry(addAnmWindow)
        nameentry.grid(row=2, column=1)

        birth=Label(addAnmWindow,text="생년월일")
        birth.grid(row=4, column=0)

        birthframe=Frame(addAnmWindow)
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

        phone=Label(addAnmWindow,text="전화번호")
        phone.grid(row=6, column=0)

        phoneentry=Entry(addAnmWindow)
        phoneentry.grid(row=6, column=1)

        zoneM=Label(addAnmWindow,text="담당구역")
        zoneM.grid(row=8, column=0)

        zoneM=Entry(addAnmWindow)
        zoneM.grid(row=8, column=1)


        register=Button(addAnmWindow, text="등록하기")
        register.grid(row=10, column=1, sticky=W+E+N+S)

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

        register=Button(addBreedWindow, text="추가하기")
        register.grid(row=8, column=1, sticky=W+E+N+S)


    
    addAnmButton=Button(frame1,text="새로운 동물 개체\n등록하기",command=addAnm ,bg="white")
    addBreedButton=Button(frame1,text="새로운 동물 종류\n추가하기",command=addBreed ,bg="white")

    addAnmButton.pack(fill="both",expand=True,side="left",pady=50,padx=10)
    addBreedButton.pack(fill="both",expand=True,side="right",pady=50,padx=10)







    #주차관리




    #고객관리




    #예매관리




    #보고서


#회원가입
def sign():
    idCheck = False
    signWindow = Tk()
    signWindow.geometry("320x178-150+150")
    
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
            print(rows) 
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

    Login=Button(loginWindow, text="로그인",command=loginF)
    Login.grid(row=0, column=2, rowspan=2,sticky=W+E+N+S)

    signup=Button(loginWindow, text="회원가입", borderwidth=0, command=sign)
    signup.grid(row=2, column=1, sticky="e")

    loginWindow.mainloop()


#홈 화면


con = pymysql.connect(host='localhost', user='root', password='1234',db='동물원', charset='utf8') # 한글처리 (charset = 'utf8')

window=Tk()
window.title("Tukorea Zoo")
window.geometry("500x400+100+100")

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
    
def mapB():
    mapBWindow=Tk()
    mapBWindow.title("원숭이마을")

def mapC():
    mapCWindow=Tk()
    mapCWindow.title("코끼리마을")

def mapD():
    mapDWindow=Tk()
    mapDWindow.title("맹수마을")

def mapE():
    mapEWindow=Tk()
    mapEWindow.title("초식동물마을")

def mapF():
    mapFWindow=Tk()
    mapFWindow.title("바다동물마을")


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
def animalInfo(name):
    infoWindow = Tk()
    infoWindow.title("동물 정보")

    url = 'https://github.com/entellaKa/school/blob/main/secondGrade/databaseProject/{}.png?raw=true'.format(name)
    res = requests.get(url)
    image = ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100)))

    name=Label(photoframe,text=name)
    img = Label(photoframe,image=image,bg=c[i%len(c)])
    img.pack(side="left")
    name.pack()

#next버튼 prev버튼
page = 0;
def paging(b):
#    if page==0 and b == 0:
    if b == 1 and 0<=page<=3:
        cur = con.cursor()
        #sql = 'insert into 회원 values("{}","{}","{}","{}","{}",0,1)'.format(IDentry.get(), PWentry.get(), nameentry.get(), birth, phoneentry.get())
        #cur.execute(sql)
        sql="select 이름 from 개체"
        cur.execute(sql)
        rows = cur.fetchall()
        #print(rows) 
        #con.commit()
        rows = rows[page*8:(page+1)*8]

        pictures = anmPicFrame.grid_slaves()
        for i in pictures:
            i["image"] = url = 'https://github.com/entellaKa/school/blob/main/secondGrade/databaseProject/{}.png?raw=true'.format(rows[i%len(rows)])
            res = requests.get(url)
            image.append(ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100))))

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
animalname=["lion","토끼","곰"]
c = ['red','orange','yellow','green','blue','purple']
image = []
for i in range(8):
    photoframe=Frame(anmPicFrame, bg="skyblue")
    url = 'https://github.com/entellaKa/school/blob/main/secondGrade/databaseProject/{}.png?raw=true'.format(animalname[i%len(animalname)])
    res = requests.get(url)
    image.append(ImageTk.PhotoImage(Image.open(BytesIO(res.content)).resize((94,100))))

    name=Label(photoframe,text=animalname[i%3])
    img = Button(photoframe,image=image[i],bg=c[i%len(c)], command=lambda: animalInfo(name["text"]))
    img.pack()
    name.pack()
    photoframe.grid(column=i%4, row=i//4)
anmFrame=Frame(frame2, bg="blue")
anmFrame.pack()
prevButton = Button(anmFrame, text="<")
nextButton = Button(anmFrame, text=">")
prevButton.pack(side="left")
nextButton.pack(side="right")

#예매
#회원/비회원 예매하기 선택, 날짜, 성인/아이, 도보/차량

#경우1) 회원 예매하기 선택 시
#회원 예매하기 창
def memberresv():
    reservationwindow=Tk()
    
    rsvDate=Label(reservationwindow,text="입장시기")
    rsvDate.grid(row=0, column=0)

    rsvDateframe=Frame(reservationwindow)
    rsvDateframe.grid(row=1, column=2)

    yearBox=ttk.Combobox(rsvDateframe,height=0, width=4, values=[2022,2023])
    yearBox.grid(row=0, column=0)

    year=Label(rsvDateframe,text="년")
    year.grid(row=0, column=1)

    monthBox=ttk.Combobox(rsvDateframe, height=0, width=4, values=[i for i in range(1,13)])
    monthBox.grid(row=0, column=2)

    month=Label(rsvDateframe,text="월")
    month.grid(row=0, column=3)

    dayBox=ttk.Combobox(rsvDateframe, height=0, width=4, values=[i for i in range(1,32)])
    dayBox.grid(row=0, column=4)

    day=Label(rsvDateframe,text="일")
    day.grid(row=0, column=5)

    visitM=Label(reservationwindow,text="방문 방법")
    visitM.grid(row=2,column=0)
    visit=StringVar()

    visit1=Radiobutton(reservationwindow, text='도보',variable=visit)
    visit2=Radiobutton(reservationwindow, text='차량',variable=visit)

    visit1.grid(row=2, column=2,sticky='w')
    visit2.grid(row=2, column=1,sticky='e')

    guestnum=Label(reservationwindow,text='방문 인원')
    guestnum.grid(row=4, column=0)

    adult=Label(reservationwindow, text="성인")
    adultEntry=Entry(reservationwindow, width=10)
    adultnum=Label(reservationwindow, text="명")

    adult.grid(row=4,column=1,padx=10,sticky='e')
    adultEntry.grid(row=4, column=2,padx=10)
    adultnum.grid(row=4, column=3,padx=10)


    kid=Label(reservationwindow, text="아이")
    kidEntry=Entry(reservationwindow,width=10)
    kidnum=Label(reservationwindow, text="명")

    kid.grid(row=5,column=1,padx=10,sticky='e')
    kidEntry.grid(row=5, column=2,padx=10)
    kidnum.grid(row=5, column=3,padx=10)

    resv=Button(reservationwindow, text="확인", command=memberresv)
    resv.grid(row=8, column=1, sticky=W+E+N+S)

    reservationwindow.mainloop()

#로그인

def memberLoginFunc():
    print(id)
    if id=='':
        Login()
        if id!="":
            memberresv()
    else:
        memberresv()

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

    register=Button(guestinfoWindow, text="확인", command=guestresv)
    register.grid(row=8, column=1, sticky=W+E+N+S)

#비회원 예매하기 창

def guestresv():
    reservationwindow=Tk()
    
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

    #############################################################
    '''
    라디오버튼 - 도보/차량 고르기
    

    성인+아이 인원 각각 입력받는 위젯
    '''
    visitM=Label(reservationwindow,text="방문 방법")
    visitM.grid(row=2,column=0)
    visit=StringVar()

    visit1=Radiobutton(reservationwindow, text='도보',variable=visit)
    visit2=Radiobutton(reservationwindow, text='차량',variable=visit)

    visit1.grid(row=2, column=2,sticky='w',padx=40)
    visit2.grid(row=2, column=2,sticky='e',padx=40)

    guestnum=Label(reservationwindow,text='방문 인원')
    guestnum.grid(row=4, column=0)

    adult=Label(reservationwindow, text="성인")
    adultEntry=Entry(reservationwindow, width=10)
    adultnum=Label(reservationwindow, text="명")

    adult.grid(row=4,column=1,padx=10,sticky='e')
    adultEntry.grid(row=4, column=2,padx=10)
    adultnum.grid(row=4, column=3,padx=10)

    kid=Label(reservationwindow, text="아이")
    kidEntry=Entry(reservationwindow,width=10)
    kidnum=Label(reservationwindow, text="명")

    kid.grid(row=5,column=1,padx=10,sticky='e')
    kidEntry.grid(row=5, column=2,padx=10)
    kidnum.grid(row=5, column=3,padx=10)

    resv=Button(reservationwindow, text="확인", command=guestresv)
    resv.grid(row=8, column=1, sticky=W+E+N+S, columnspan=2)

    reservationwindow.mainloop()
guestButton=Button(frame3,text="비회원\n예매하기",command=guestinfo,bg="white")

memberButton.pack(fill="both",expand=True,side="left",pady=50,padx=10)
guestButton.pack(fill="both",expand=True,side="right",pady=50,padx=10)

#예매 내역 확인 버튼
def receipt(name, birth, number):
    globals.name = name
    globals.birth = birth
    globals.number = number

#예매 내역
def guestreceipt():
    receiptwindow=Tk()

    #이름, 생일, 번호

    guestname=Label(receiptwindow,text="이름")
    guestname.grid(row=0, column=0)

    nameentry=Entry(receiptwindow)
    nameentry.grid(row=0, column=1)

    guestbirth=Label(receiptwindow,text="생일")
    guestbirth.grid(row=1,column=0)

    birthentry=Entry(receiptwindow)
    birthentry.grid(row=1, column=1)

    guestnumber=Label(receiptwindow,text="번호")
    guestnumber.grid(row=2, column=0)

    numberentry=Entry(receiptwindow)
    numberentry.grid(row=2, column=1)
  
    searchreceipt=Button(receiptwindow, text="확인")
    searchreceipt.grid(row=3, column=1, sticky=W+E+N+S)

    receiptwindow.mainloop()

searchButton=Button(frame4,text="비회원 조회하기",command=guestreceipt)
if id=="":
    guestreceipt

#테이블
columnname=["예약자명","예약일자","인원"]
table=ttk.Treeview(frame4, columns=columnname)

table.column("#0",width=10, anchor="center")
table.heading("#0", text="index")
for i in columnname:
    table.column(i,width=100, anchor="center")
    table.heading(i, text=i)

table.insert("", "end",text=0,values=["김선재","2022.11.17","3명"])

table.pack()
searchButton.pack()

window.mainloop()