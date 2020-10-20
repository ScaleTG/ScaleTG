from modules.core import Update
from config import enabled_apps
from importlib import import_module

# Load all enabled apps
processors = []

for app in enabled_apps:
    processors.append(import_module('apps.{}.app'.format(app)))

def main(telegramObject):
    u = Update(telegramObject)

    results = []
    for processor in processors:
        results.append(processor.process(u))
    
    for result in results:
        if result is not None:
            return result
    return ''