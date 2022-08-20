from flask import Flask, render_template , request
import sql
app = Flask(__name__)


phone = []
for i in range(len(sql.phone)):
    phone.append({
        "company": sql.phone[i][0],
        "fullname": sql.phone[i][1],
        "memory": sql.phone[i][2],
        "color": sql.phone[i][3],
        "date": sql.phone[i][4],

        "size": sql.phone[i][5],
        "weight": sql.phone[i][6],
        "simcard": sql.phone[i][7],
        "screensize": sql.phone[i][8],
        "screenresolution": sql.phone[i][9],

        "operatingsystem": sql.phone[i][10],
        "chipset": sql.phone[i][11],
        "gpu": sql.phone[i][12],
        "ram": sql.phone[i][13],
        "additionalmemory": sql.phone[i][14],

        "maincamera": sql.phone[i][15],
        "video": sql.phone[i][16],
        "selfiecamera": sql.phone[i][17],
        "selfievideo": sql.phone[i][18],
        "bluthooth": sql.phone[i][19],
    
        "gps": sql.phone[i][20],
        "nfc": sql.phone[i][21],
        "fradio": sql.phone[i][22],
        "part": sql.phone[i][23],
        "sizemah": sql.phone[i][24],

        "price": sql.phone[i][25]
    })

























@app.route('/')
def mainpagebooks():
    
    return render_template("index.html" , hello = "KK KK")


@app.route('/phones')
def phones():
    
    return render_template("pages/store-list.html")
@app.route('/tabs')
def tabs():
    
    return render_template("pages/store-list.html")
@app.route('/laptops')
def laptops():
    
    return render_template("pages/store-list.html")
@app.route('/audio')
def audio():
    
    return render_template("pages/store-list.html")
@app.route('/gaming')
def gaming():
    
    return render_template("pages/store-list.html")
@app.route('/tel-mon')
def telmon():
    
    return render_template("pages/store-list.html")
@app.route('/photo-video')
def photovideo():
    
    return render_template("pages/store-list.html")
@app.route('/others')
def others():
    
    return render_template("pages/store-list.html")



if __name__ == '__main__':
    app.run(debug=True)