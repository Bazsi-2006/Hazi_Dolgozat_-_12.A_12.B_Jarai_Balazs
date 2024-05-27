from flask import Flask, request, make_response, send_file

app = Flask(__name__)

# GET végpont paraméterek nélkül
@app.get("/hello")
def hello():
    return "Hello, World!"

# GET végpont útvonal paraméterrel
@app.get("/user/<username>")
def get_user(username):
    return f"Hello, {username}!"

# GET végpont query paraméterrel
@app.get("/search")
def search():
    query = request.args.get("q")
    return f"Keresési eredmények: {query}"

# POST végpont form adatok kezeléséhez
@app.post("/submit_form")
def submit_form():
    password = request.form.get("password")
    return f"Form benyújtva a következő jelszóval: {password}"

# POST végpont JSON adatok kezeléséhez
@app.post("/submit_json")
def submit_json():
    data = request.get_json()
    return f"Kapott JSON: {data}"

# Végpont süti beállításához
@app.get("/set_cookie")
def set_cookie():
    response = make_response("Süti beállítva")
    response.set_cookie("token", "SessionToken")
    return response

# Végpont süti lekéréséhez
@app.get("/get_cookie")
def get_cookie():
    token = request.cookies.get("token")
    return f"Sütiből származó token: {token}"

# A test.html fájl kiszolgálása
@app.get("/test")
def test():
    return send_file("test.html")

if __name__ == "__main__":
    app.run(debug=True)
