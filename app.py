from flask import Flask,render_template,request,redirect
import pymysql
conn = pymysql.connect(host='localhost', port=3306, db='pyapp', user='root', passwd='java1004')

print(conn)
app = Flask(__name__)

# 1. msp 목록
@app.route('/', methods=['GET'])
def msg_list():
    cursor = conn.cursor()
    cursor.execute('SELECT msg_id, msg_text FROM msg')
    msglist = cursor.fetchall() # cursor.fetchone()
    # print(msglist)
    return render_template('msg_list.html',msglist = msglist)

# 2. msg_add.html 폼
@app.route('/add_msg', methods=['GET','POST'])
def add_msg():
    if request.method == 'GET':
        return render_template('add_msg.html')
    elif request.method == 'POST':
        msg_text = request.form['msg_text']
        # db 입력
        cursor = conn.cursor()
        cursor.execute('INSERT INTO msg(msg_text) VALUES(%s)',[msg_text])
        conn.commit()
        return redirect('/')

# 3. msg_del.html
@app.route('/del_msg', methods=['GET'])
def del_msg():
    msg_id = request.args.get('msg_id')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM msg WHERE msg_id=%s',[msg_id])
    conn.commit()
    return redirect('/')

# 4. msg_mdf.html
@app.route('/mdf_msg', methods=['GET','POST'])
def mdf_msg():
    if request.method == 'GET':
        msg_id = request.args.get('msg_id')
        msg_text = request.args.get('msg_text')
        print(msg_id)
        print(msg_text)
        return render_template('mdf_msg.html')
    elif request.method == 'POST':
        msg_id = request.form['msg_id']
        msg_text = request.form['msg_text']
        print(msg_id)
        print(msg_text)
        cursor = conn.cursor()
        cursor.execute('UPDATE msg SET msg_text = %s WHERE msg_id=%s',[msg_text, msg_id])
        conn.commit()
        return redirect('/')

app.run(host='127.0.0.1', port=80)