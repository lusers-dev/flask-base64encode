import re
import base64
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "super-secret-flask-key-e3b0c44298fc1c149afbf4c8996fb9"


def base64_encode(encode_to_b64):
    encoded_bytes = None
    encoded_data = None
    encoded_bytes = base64.b64encode(encode_to_b64.encode("utf-8"))
    encoded_data = str(encoded_bytes, "utf-8")
    return str(encoded_data)


@app.route("/", methods=['POST', 'GET'])
def process():
    output = None
    entry = None
    try:
        entry = str(request.form['64base_encode'])
    except Exception as e:
        pass

    if entry:
        try: 
            if entry:
                try:
                    output = base64_encode(entry)
                    flash(output)

                except Exception as e:
                    flash(e)
                    pass
            else:
                flash('Invalid entry!')
      
        except Exception as e:
            flash(e)
            pass

    return render_template("index.html")


