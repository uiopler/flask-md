from flask import Flask, render_template
import os
app = Flask(__name__)

# This will load every file in the 'templates' folder and then render it


#This has the route at "{ip:port}/{md file name}"
for i in os.listdir("templates"):
    name = i[:-5]
    print(name)
    @app.route(f'/{name}')
    def home():
        return render_template(i)


def run():


    #app running on debug mode, set it to False on production
    app.debug = True
    app.run()
