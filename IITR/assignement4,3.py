import shapes

infile = open("input.txt", "r")
outfile = open("output.txt", 'w')

for line in infile:
    a = line.strip().split(",") # seperates each line into an array for processing 
    if a[0].lower() == "circle":
        # cirle requries a radius
        c = shapes.Circle(float(a[1]))
        outfile.write(f"Area of a circle with radius {a[1]} is {c.get_area():.3f}\n")
        outfile.write(f"Perimeter of a circle with radius {a[1]} is {c.get_perimeter():.3f}\n")
    elif a[0].lower() == "rectangle":
        #rectangle requires length and width
        r = shapes.Rectangle(float(a[1]), float(a[2]))
        outfile.write(f"Area of a rectangle with length {a[1]} and width {a[2]} is {r.get_area()}\n")
        outfile.write(f"Perimeter of a rectangle with length {a[1]} and width {a[2]} is {r.get_perimeter()}\n")
    elif a[0].lower() == "square":
        # square requires length
        s = shapes.Square(float(a[1]))
        outfile.write(f"Area of a square with length {a[1]} is {s.get_area()}\n")
        outfile.write(f"Perimeter of a square with length {a[1]} is {s.get_perimeter()}\n")
    elif a[0].lower() == "pentagon":
        # pentagon requires length
        p = shapes.Pentagon(float(a[1]))
        outfile.write(f"Area of a pentagon with length {a[1]} is {p.get_area()}\n")
        outfile.write(f"Perimeter of a pentagon with length {a[1]} is {p.get_perimeter()}\n")
    elif a[0].lower() == "triangle":
        # triangle requires 3 lengths
        t = shapes.Triangle(float(a[1]), float(a[2]), float(a[3]))
        outfile.write(f"Area of a triangle with lengths {a[1]}, {a[2]}, and {a[3]} is {t.get_area()}\n")
        outfile.write(f"Perimeter of a triangle with lengths {a[1]}, {a[2]}, and {a[3]} is {t.get_perimeter()}\n")

infile.close()
outfile.close()