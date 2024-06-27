# plugin_system/plugin_manager.py

import pluggy

hookspec = pluggy.HookspecMarker("plugin_system")
hookimpl = pluggy.HookimplMarker("plugin_system")

class PluginManager:
    def __init__(self):
        self.pm = pluggy.PluginManager("plugin_system")
        self.pm.add_hookspecs(HookSpecs)
    
    def load_plugins(self, plugin):
        self.pm.register(plugin)

    def execute(self):
        self.pm.hook.say_hello()

class HookSpecs:
    @hookspec
    def say_hello(self):
        """Um hook que diz olá"""
