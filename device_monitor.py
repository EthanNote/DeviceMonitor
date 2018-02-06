import htmlPy
import os

device_list=[
    ('Device A', [        ('IP','192.168.1.1'),        ('position', 'F1')    ]),
    ('Device B', [        ('IP','192.168.1.2'),        ('position', 'F2')    ]),
    ('Device C', [        ('IP','192.168.1.3'),        ('position', 'F3')    ]),
    ('Device D', [        ('IP','192.168.1.4'),        ('position', 'F4')    ])
]

class JavascriptBuildinAPI(htmlPy.Object):
    @htmlPy.Slot(str)
    def print_to_terminal(self, data):
        print(data)

    @htmlPy.Slot(str)
    def jump(self, url):
        app.template=(url, {})

app=htmlPy.AppGUI(width=960, height=720)
app.template_path = os.path.abspath("templates")
app.static_path = os.path.abspath("static")
app.template = ('sensor_network_01.htmltemplate', {'devices':device_list*2})
app.bind(JavascriptBuildinAPI())
app.start()