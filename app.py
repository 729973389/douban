import sqlite3

from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template('index.html')



@app.route('/index')
def home():
    return index()

@app.route('/movie')
def movie():  # put application's code here
    datalist=[]
    con=sqlite3.connect("movie.db")
    c=con.cursor(    )
    sql="select * from movie250"
    data=c.execute(sql)
    for item in data:
        datalist.append(item)
    c.close()
    con.close()
    return render_template('movie.html',movies=datalist)

@app.route('/score')
def score():  # put application's code here
    scorelist=[]          #评分
    numberlist=[]         #每个评分所统计出的电影数量
    con = sqlite3.connect("movie.db")
    c = con.cursor()
    sql = "select rating,count(rating) from movie250 group by rating"
    data = c.execute(sql)
    for item in data:
        scorelist.append(item[0])
        numberlist.append(item[1])
    c.close()
    con.close()
    return render_template('score.html',score=scorelist,number=numberlist)

@app.route('/word')
def word():  # put application's code here
    return render_template('word.html')


@app.route('/team')
def team():  # put application's code here
    return render_template('team.html')






if __name__ == '__main__':
    app.run(debug=True)









































