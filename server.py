
from flask import Flask, render_template, request, jsonify, send_file
import io
from Captcha import get_captcha, validate

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/captcha_image")
def captcha_image():
    # generate a new captcha image (this also sets captcha_text in Captcha module)
    image, _text = get_captcha()
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

@app.route("/validate", methods=["POST"])
def validate_captcha():
    user_input = request.form.get("captcha_input", "")
    is_valid, message = validate(user_input)
    return jsonify({"is_valid": is_valid, "message": message})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
