import pygame
import math
# Inicializar Pygame
pygame.init()
# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie
width = 800 
height = 600
surface = pygame.display.set_mode((width, height))
background_color = (255, 23, 100)
surface.fill(background_color)
# Definir colores
color = (255, 120, 10)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
grosor_linea = 1
def dibujar_cuadrado(pos_x, pos_y, lado):
    pygame.draw.rect(surface, color, (pos_x, pos_y, lado, lado), grosor_linea)
    pygame.display.flip()
def dibujar_circulo(pos_x, pos_y, radio):
    pygame.draw.circle(surface, color, (pos_x, pos_y), radio, grosor_linea)
    pygame.display.flip()
def dibujar_linea(punto_a, punto_b):
    pygame.draw.line(surface, color, punto_a, punto_b, grosor_linea)
    pygame.display.flip()
def dibujar_rectangulo(pos_x, pos_y, ancho, alto):
    pygame.draw.rect(surface, color, (pos_x, pos_y, ancho, alto), grosor_linea)
    pygame.display.flip()
def dibujar_triangulo_equilatero(pos_x, pos_y, lado):
    altura = lado * math.sqrt(3) / 2
    punto_a = (pos_x, pos_y)
    punto_b = (pos_x + lado, pos_y)
    punto_c = (pos_x + lado / 2, pos_y - altura)
    pygame.draw.polygon(surface, color, [punto_a, punto_b, punto_c], grosor_linea)
    pygame.display.flip()
def dibujar_triangulo_isoceles(pos_x, pos_y, base, altura):
    punto_a = (pos_x, pos_y)
    punto_b = (pos_x + base, pos_y)
    punto_c = (pos_x + base / 2, pos_y - altura)
    pygame.draw.polygon(surface, color, [punto_a, punto_b, punto_c], grosor_linea)
    pygame.display.flip()
def dibujar_triangulo_escaleno(pos_x1, pos_y1, pos_x2, pos_y2, pos_x3, pos_y3):
    punto_a = (pos_x1, pos_y1)
    punto_b = (pos_x2, pos_y2)
    punto_c = (pos_x3, pos_y3)
    pygame.draw.polygon(surface, color, [punto_a, punto_b, punto_c], grosor_linea)
    pygame.display.flip()
def cambiar_fondo(color):
    surface.fill(color)
    pygame.display.flip()
def cambiar_color_linea(nuevo_color):
    global color
    color = nuevo_color
def cambiar_grosor_linea(grosor):
    global grosor_linea
    grosor_linea = grosor
def mostrar_menu():
    print("-------- MENU --------")
    print("1. Draw")
    print("2. Help")
    print("3. Exit")
def mostrar_opciones():
    print("-------- DRAWING OPTIONS --------")
    print("1. Square")
    print("2. Circle")
    print("3. Line")
    print("4. Rectangle")
    print("5. Triangle")
    print("6. Change background color")
    print("7. Change draw color")
    print("8. Change thickness")
    print("9. Main menu")
def mostrar_tipos_triangulos():
    print("-------- TRIANGLE TYPES --------")
    print("1. Equilateral triangle")
    print("2. Isoceles triangle")
    print("3. Scalene triangle")
def mostrar_help():
    print("-------- HELP --------")
    print("The background has the next colors: Black, White, Red, Blue")
    print("The drawing color has the next colors: Green, Blue, White, Red")
# Esperar a que el usuario cierre la ventana
while True:
    mostrar_menu()
    cmd = input("Select an option: ")
    if cmd == "1":
        while True:
            mostrar_opciones()
            opcion = input("Select an option:: ")
            if opcion == "1":
                pos_x = int(input("Enter the X position: "))
                pos_y = int(input("Enter the Y position: "))
                lado = int(input("Enter the size of de side: "))
                dibujar_cuadrado(pos_x, pos_y, lado)
            elif opcion == "2":
                pos_x = int(input("Enter the X position: "))
                pos_y = int(input("Enter the Y position: "))
                radio = int(input("Enter the radius of the circle: "))
                dibujar_circulo(pos_x, pos_y, radio)
            elif opcion == "3":
                x1 = int(input("Enter the X coordinate of the A point: "))
                y1 = int(input("Enter the Y coordinate of the A point: "))
                x2 = int(input("Enter the X coordinate of the B point: "))
                y2 = int(input("Enter the Y coordinate of the B point: "))
                punto_a = (x1, y1)
                punto_b = (x2, y2)
                dibujar_linea(punto_a, punto_b)
            elif opcion == "4":
                pos_x = int(input("Enter the X position: "))
                pos_y = int(input("Enter the Y position: "))
                ancho = int(input("Enter the base of the rectangle: "))
                alto = int(input("Enter the height of the rectangle: "))
                dibujar_rectangulo(pos_x, pos_y, ancho, alto)
            elif opcion == "5":
                mostrar_tipos_triangulos()
                tipo_triangulo = input("Choose a triangle type: ")
                if tipo_triangulo == "1":
                    pos_x = int(input("Enter the X position: "))
                    pos_y = int(input("Enter the Y position: "))
                    lado = int(input("Enter the size of the sides: "))
                    dibujar_triangulo_equilatero(pos_x, pos_y, lado)
                elif tipo_triangulo == "2":
                    pos_x = int(input("Enter the X position: "))
                    pos_y = int(input("Enter the Y position: "))
                    base = int(input("Enter the base of the triangle: "))
                    altura = int(input("Enter the height: "))
                    dibujar_triangulo_isoceles(pos_x, pos_y, base, altura)
                elif tipo_triangulo == "3":
                    pos_x1 = int(input("Enter the X coordinate of the A point: "))
                    pos_y1 = int(input("Enter the Y coordinate of the A point: "))
                    pos_x2 = int(input("Enter the X coordinate of the B point: "))
                    pos_y2 = int(input("Enter the Y coordinate of the B point: "))
                    pos_x3 = int(input("Enter the X coordinate of the C point: "))
                    pos_y3 = int(input("Enter the Y coordinate of the C point: "))
                    dibujar_triangulo_escaleno(pos_x1, pos_y1, pos_x2, pos_y2, pos_x3, pos_y3)
                else:
                    print("Invalid option. Please, choose a valid option.")
            elif opcion == "6":
                print("Avaiable colors:")
                print("1. Black")
                print("2. White")
                print("3. Red")
                print("4. Blue")
                color_opcion = input("Choose a color: ")
                if color_opcion == "1":
                    cambiar_fondo(black)
                elif color_opcion == "2":
                    cambiar_fondo(white)
                elif color_opcion == "3":
                    cambiar_fondo(red)
                elif color_opcion == "4":
                    cambiar_fondo(blue)
                else:
                    print("Invalid option. The color won't change.")
            elif opcion == "7":
                print("Avaiable colors:")
                print("1. Green")
                print("2. Blue")
                print("3. White")
                print("4. Red")
                color_opcion = input("Choose a color: ")
                if color_opcion == "1":
                    cambiar_color_linea(green)
                elif color_opcion == "2":
                    cambiar_color_linea(blue)
                elif color_opcion == "3":
                    cambiar_color_linea(white)
                elif color_opcion == "4":
                    cambiar_color_linea(red)
                else:
                    print("Invalid option. The color won't change.")
            elif opcion == "8":
                grosor = int(input("Enter the line thickness: "))
                cambiar_grosor_linea(grosor)
            elif opcion == "9":
                break
            else:
                print("Invalid option. Please, choose a valid option.")
    elif cmd == "2":
        mostrar_help()
    elif cmd == "3":
        pygame.quit()
        break
    else:
        print("Invalid option. Please, choose a valid option.")