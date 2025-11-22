from flask import Flask, render_template, request

app = Flask(__name__)

# Ommaviy OSINT tool listi
tools = [
    {"name": "Google Maps", "url": "https://www.google.com/maps"},
    {"name": "OpenStreetMap", "url": "https://www.openstreetmap.org"},
    {"name": "GeoGuessr", "url": "https://www.geoguessr.com"},
    {"name": "IP Location", "url": "https://www.iplocation.net"},
    {"name": "EXIF Viewer", "url": "https://exif.tools/"},
    {"name": "What3Words", "url": "https://what3words.com/"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    if request.method == "POST":
        query = request.form.get("query")
        # Optional: qidiruvni har bir tool'ga URL query qo'shish mumkin
    return render_template("index.html", tools=tools, query=query)

if __name__ == "__main__":
    app.run(debug=True)
