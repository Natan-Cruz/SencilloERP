from plugin_manager import hookimpl

class HelloPlugin:
    @hookimpl
    def say_hello(self):
        print("Hello, World from HelloPlugin!")