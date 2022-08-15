import markdown, os, asyncio
from flask_server import run

# This will convert the md to an HTML file

def convert():

    for i in os.listdir('md'):
        try:

            with open(f'./md/{i}', 'r') as f:
                text = f.read()
                html = markdown.markdown(text)
                       
            with open(f'./templates/{i[:-3]}.html', 'w') as f:
                f.write(html)


            run()


        except Exception as x:
            print(x)
            


convert()
