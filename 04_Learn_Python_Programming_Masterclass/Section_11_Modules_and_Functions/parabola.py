import tkinter
import math


def parabola(canvas, size):
    for x in range(size):
        y = x * x / size
        plot(canvas, x, y)
        plot(canvas, -x, y)


def old_circle(canvas, radius, g, h):
    for x in range(g * 100, (g + radius) * 100):
        x /= 100
        y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
        plot(canvas, x, y)
        plot(canvas, x, 2 * h - y)
        plot(canvas, 2 * g - x, y)
        plot(canvas, 2 * g - x, 2 * h - y)


def circle(canvas, radius, g, h, color="red"):
    canvas.create_oval(g + radius, -(h + radius), g - radius, -(h - radius),
                       outline=color, width=2)


def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, -y_origin, 0, y_origin, fill="black")


def plot(canvas, x, y):
    canvas.create_line(x, -y, x + 1, -y + 1, fill='red')


main_window = tkinter.Tk()
main_window.title("Parabola")
main_window.geometry("640x480")

canvas = tkinter.Canvas(main_window, width=640, height=480)
canvas.grid(row=0, column=0)
draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100, color="blue")

main_window.mainloop()
