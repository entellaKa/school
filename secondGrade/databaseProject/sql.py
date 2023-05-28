import pymysql

name = ['미어캣', '토끼', '흰목원숭이', '다람쥐원숭이', '아프리카코끼리', '아시아코끼리', 
'사자', '곰', '알파카', '캥거루', '물개', '바다사자']
area = [1,1,2,2,3,3,4,4,5,5,6,6]
feed = ['초식','초식','바나나','바나나','초식','초식','고기','고기','초식','초식','물고기','물고기']

insertAnimalSQL = '''
INSERT INTO 동물 VALUES(0, '밍키', '2021-03-28', 15,0,1);
INSERT INTO 동물 VALUES(0, '예삐', '2022-05-26', 17,1,2);
INSERT INTO 동물 VALUES(0, '끼돌이', '2020-07-24', 18,0,1);
INSERT INTO 동물 VALUES(0, '코돌이', '2021-09-22', 19,1,2);
INSERT INTO 동물 VALUES(0, '럭키', '2022-11-20', 20,0,1);
INSERT INTO 동물 VALUES(0, '꽃순이', '2020-02-18', 21,1,2);
INSERT INTO 동물 VALUES(0, '돌이', '2021-04-16', 22,0,1);
INSERT INTO 동물 VALUES(0, '사랑이', '2022-06-14', 23,1,2);
INSERT INTO 동물 VALUES(0, '길동', '2020-08-12', 24,0,1);
INSERT INTO 동물 VALUES(0, '리핌', '2021-10-10', 25,1,2);
INSERT INTO 동물 VALUES(0, '코코', '2022-12-8', 26,0,1);
'''



con = pymysql.connect(host='localhost', user='root', password='0000',db='동물원', charset='utf8') # 한글처리 (charset = 'utf8')
cur = con.cursor()
for i in range(len(name)):
    cur.execute("insert into 종류 values(0, '{}', '{}', {})".format(name[i], feed[i], area[i]))
cur.execute(insertAnimalSQL)

con.commit()