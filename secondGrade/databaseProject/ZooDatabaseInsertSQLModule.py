import pymysql

membership = [['아이언',0,0],['브론즈',0.10, 100],['실버',0.25, 300],['골드',0.20, 1000],['다이아',0.30, 5000]]
#user = [['inchol321','1234','가인철','2000-03-21','01029275208']] #회원 정보(아이디, 비밀번호, 이름, 생년월일, 휴대전화번호)
zone  = ['꼬마동물마을','원숭이마을','코끼리마을','맹수마을','초식동물마을','바다동물마을']

worker = ["'가인철','2000-03-21','01029275208','경기도 시흥시 신흥마을 1길 34-1','NH 302-1307-4986-11','2019-02-28'",
"'이예림','2002-12-11','01071546855','인천광역시 남동구 구월동 힐스테이트 아파트 어딘가','NH 302-1307-4986-11','2021-02-28'"]

BFZ = [['곰','연어','맹수마을'],['사자','고기','맹수마을'],['토끼','당근','꼬마동물마을']] #Breed and Food and Zone 종류와 먹이와 구역
#animal = [] #동물 정보(이름, 생년월일, 종류, 성별, 담당 사육사)


sqlMembership = "insert into 멤버십 values(0,,'{}',{},{})"

sqlZone = "insert into 구역 values(0, '{}');"

sqlWorker = "insert into 직원 values(0, {})"

con = pymysql.connect(host="localhost", user="root", passwd="0000", charset="utf8")
cur = con.cursor()
for i in zone:
    cur.execute(sqlZone.format(i))

for i in membership:
    cur.execute(sqlMembership.format(i[0], i[1], i[2]))

for i in worker:
    cur.execute(sqlWorker.format(i))
con.commit()