from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form ="""
<!doctype html> 
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;            
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px
            }}
        </style>
    </head>
    <body>
            <form method="post">
            <label for="rotate-item"><strong>Rotate by:</strong></label>
            <input id="rotate-item" type="text" name="rot" value="0"/>
            <textarea name="text">{0}</textarea>    
            <input type="submit" />   
    </body>
</html>
"""
@app.route("/")
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    roation_value = int(request.form['rot'])
    text = request.form['text']
    encryption = rotate_string(text,roation_value)
    return form.format(encryption)
app.run()