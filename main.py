import webview
from core.Renderer import Renderer

"""
An example of serverless app architecture
"""
renderer = Renderer()

def on_closing():
    print('pywebview window is closing')
    renderer.disable_rendering()

def on_loaded():
    renderer.set_window(webview.windows[0])
    renderer.enable_rendering()
    
    webview.windows[0].events.loaded -= on_loaded
    webview.windows[0].maximize()

class Api:
    def addItem(self, title):
        print('Added item %s' % title)

    def removeItem(self, item):
        print('Removed item %s' % item)

    def editItem(self, item):
        print('Edited item %s' % item)

    def toggleItem(self, item):
        print('Toggled item %s' % item)

    def toggleFullscreen(self):
        webview.windows[0].toggle_fullscreen()


if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Todos magnificos', 'assets/index.html', js_api=api, min_size=(600, 450))

    window.events.closing += on_closing
    window.events.loaded += on_loaded

    webview.start()
