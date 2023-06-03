import pygame
# Inicializar Pygame
pygame.init()
# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie
width = 800 
height = 600
surface = pygame.display.set_mode((width, height))
background_color = (255,23,100)
surface.fill(background_color)
# colours
colours = { 
    "black"     : (000,000,000),
    "red"       : (255,000,000),
    "green"     : (000,255,000),
    "blue"      : (000,000,255),
    "yellow"    : (255,255,000),
    "magenta"   : (255,000,255),
    "cyan"      : (000,255,255),
    "white"     : (255,255,255)
}
def colour_set(colour):
    print(f"setting drawing color to... {colour}")
def colours_ls():
    while True:
        print("aviable colours are...")
        for index, element in enumerate(colours):
            print(f"{index+1}.{element}")
        print("please enter the number of the corresponding colour or 'q' to cancel: ")
        answer = input()
        if answer == 'q':
            break
        try:
            index = int(answer)-1
            if 0 <= index < len(colours):
                selection = colours[index]
                colour_set(selection)
                break
            else:
                print("invalid choice")
        except ValueError:
            print("invalid choice")
#help funtion
commands = {
    "help",
    "colours ls",
    "background colour",
    "draw line",
    "draw square",
    "draw rectangle",
    "draw circle",
    "draw triangle",
    "undo",
    "re size"
}
def p_help():
    print("alfa version of paint made by Roberto Romero")
    print("soported commands are...")
    for elements in commands:
        print(elements)
def bgcolour_set(colour):
    pygame.display.set.caption(f"setting background color to... {colour}")
    surface.fill(colours[colour])
    pygame.display.flip()
def change_bg():
    while True:
        print("aviable colours are...")
        for index, element in enumerate(colours):
            print(f"{index+1}.{element}")
        print("please enter the number of the corresponding colour or 'q' to cancel: ")
        answer = input()
        if answer == 'q':
            break
        try:
            index = int(answer)-1
            if 0 <= index < len(colours):
                selection = colours[index]
                bgcolour_set(selection)
                break
            else:
                print("invalid choice")
        except ValueError:
            print("invalid choice")
menuitems = {
    "dibujar",
    "ayuda",
    "colores",
    "salir"
}
def menu():
    while True:
        print("las opciones son...")
        for num, items in enumerate(menuitems):
            print(f"{num+1}.{items}")
        print("ingrese el numero de la opcion que desea realizar...")
        opcion = input()
        if opcion == '4':
            pygame.quit()
            break
        if opcion == '1':
            print("Hi")
while True:
    cmd = input("cmd> ")
    if cmd == "exit":
        pygame.quit()
    if cmd == "colours ls":
        colours_ls()
    if cmd == "help":
        p_help()
    if cmd == "background colour":
        change_bg()
    if cmd == "menu":
        menu()