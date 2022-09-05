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


apple = []
for i in range(len(phone)):
    if phone[i]["company"] == "Apple":
        apple.append(phone[i])

samsung = []
for i in range(len(phone)):
    if phone[i]["company"] == "Samsung":
        samsung.append(phone[i])

huawei = []
for i in range(len(phone)):
    if phone[i]["company"] == "Huawei":
        huawei.append(phone[i])

xiaomi = []
for i in range(len(phone)):
    if phone[i]["company"] == "Xiaomi":
        xiaomi.append(phone[i])

oneplus = []
for i in range(len(phone)):
    if phone[i]["company"] == "Oneplus":
        oneplus.append(phone[i])

google = []
for i in range(len(phone)):
    if phone[i]["company"] == "Google":
        google.append(phone[i])


realme = []
for i in range(len(phone)):
    if phone[i]["company"] == "Realme":
        realme.append(phone[i])




























@app.route('/')
def mainpagebooks():
    
    return render_template("index.html" , phone = phone)

@app.route('/apple')
def phones():
    
    return render_template("pages/store-list.html" , phone = apple)

@app.route('/samsung')
def tabs():
    
    return render_template("pages/store-list.html" , phone = samsung)

@app.route('/huawei')
def laptops():
    
    return render_template("pages/store-list.html" , phone = huawei)

@app.route('/xiaomi')
def audio():
    
    return render_template("pages/store-list.html" , phone = xiaomi)

@app.route('/oneplus')
def gaming():
    
    return render_template("pages/store-list.html" , phone = oneplus)

@app.route('/google')
def telmon():
    
    return render_template("pages/store-list.html" , phone = google)

@app.route('/realme')
def photovideo():
    
    return render_template("pages/store-list.html" , phone = realme)

@app.route('/all')
def others():
    
    return render_template("pages/store-list.html" , phone = phone)




if __name__ == '__main__':
    app.run(debug=True)