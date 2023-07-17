#Thank you LazyDeveloper for helping developers in this journey !
#Must Subscribe On YouTube @LazyDeveloperr 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@LazyDeveloper'


if __name__ == "__main__":
    rt = int(os.environ.get('PORT', 5000))
    app = Bot()
    app.run(host='0.0.0.0', port=port)
