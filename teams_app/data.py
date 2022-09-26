from teams_app.menu import Menu

def run():
    menu = Menu()
    should_exist = False
    while not should_exist:
        should_exist = menu.process()