import pymysql

name = ['미어캣', '토끼', '흰목원숭이', '다람쥐원숭이', '아프리카코끼리', '아시아코끼리', 
'사자', '곰', '알파카', '캥거루', '물개', '바다사자']
area = [1,1,2,2,3,3,4,4,5,5,6,6]
feed = ['초식','초식','바나나','바나나','초식','초식','고기','고기','초식','초식','물고기','물고기']
con = pymysql.connect(host='localhost', user='root', password='0000',db='동물원', charset='utf8') # 한글처리 (charset = 'utf8')
cur = con.cursor()
for i in range(len(name)):
    cur.execute("insert into 종류 values(0, '{}', '{}', {})".format(name[i], feed[i], area[i]))