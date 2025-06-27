from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/api/call-handler", methods=["POST"])
def call_handler():
    # Twilio'dan gelen çağrıyı burada işleriz
    return Response("<Response><Say>Hello, this is your AI assistant speaking from Print2Walls.</Say></Response>", mimetype="text/xml")

if __name__ == "__main__":
    app.run()
