# plugin_system/main.py

from plugin_manager import PluginManager
from plugins.hello_plugin import HelloPlugin
from flask import Flask
from flask import send_from_directory

app = Flask(__name__,
            static_url_path='', 
            static_folder='public',
            template_folder='public')
def main():
    manager = PluginManager()
    manager.load_plugins(HelloPlugin())
    manager.execute()

@app.route('/')
def hello_world():
    return send_from_directory("public", 'index.html')

if __name__ == "__main__":
    main()
    app.run(debug=True)
