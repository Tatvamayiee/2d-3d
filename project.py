import math as m
print('                 Geomentrical    shapes                     ')
print('Geometric shapes are the figures which demonstrate the shape of the objects we see in our everyday life.\n In geometry, shapes are the forms of objects which have boundary lines, angles and surfaces.\n There are different types of 2d shapes and 3d shapes')
print('Shapes are also classified with respect to their regularity or uniformity. \nA regular shape is usually symmetrical such as a square, circle, etc.\n Irregular shapes are unsymmetrical. They are also called freeform shapes or organic shapes. \nFor example, the shape of a tree is irregular or organic.')
print('In plane geometry, the two-dimensional shapes are flat shapes and closed figures such as circles, squares, rectangles, rhombus, etc.\n  In solid geometry, the three-dimensional shapes are cube, cuboid, cone, sphere and cylinder. \nWe can observe all these shapes in our daily existence also. \nFor example books (cuboid shape), glasses (cylindrical shape), traffic cones (conical shape) and so on. In this article, you will learn about different geometric shapes ')
while True:
    a=(input("Do you Want to Continue?[yes/no]"))
    if a=="yes":
        n=(input('enter your choice[2d/3d]'))
        if n=='2d':       #enter input in lowercase i.e,smallletters (for all inputs)
            shape=(input(' enter a 2d shape name'))   
            if shape== "rectangle":
                    print("The fundamental properties of rectangles are:\n\
A rectangle is a quadrilateral\n\
The opposite sides are parallel and equal to each other\n\
Each interior angle is equal to 90 degrees\n\
The sum of all the interior angles is equal to 360 degrees\n\
The diagonals bisect each other\
Both the diagonals have the same length")
                    l = int(input("Enter rectangle's length: "))
                    b = int(input("Enter rectangle's breadth: "))
                    area = l * b
                    per=2*(l+b)
                    print("The area of rectangle is", area)
                    print('perimeter:',per)
            elif shape == "square":
                    print("The most important properties of a square are listed below:\
All four interior angles are equal to 90°\n\
All four sides of the square are congruent or equal to each other\n\
The opposite sides of the square are parallel to each other\n\
The diagonals of the square bisect each other at 90°\n\
The two diagonals of the square are equal to each other\n\
The square has 4 vertices and 4 sides\n\
The diagonal of the square divide it into two similar isosceles triangles\n\
The length of diagonals is greater than the sides of the square")
                    s = int(input("Enter square's side length: "))
                    area = m.pow(s,2)
                    per=4*s
                    print("The area of square is",area)
                    print('perimeter:',per)
            elif shape == "triangle":
                    print('All the properties of a triangle are based on its sides and angles.\n\
By the definition of triangle, we know that, it is a closed polygon that consists of three sides \
and three vertices. \n\
Also, the sum of all three internal angles of a triangle equal to 180°')
                    h = (int(input("Enter triangle's height length: ")))
                    b = (int(input("Enter triangle's breadth length: ")))
                    area = int(0.5 * b * h)
                    print("The area of triangle is ",area)
            elif shape == "circle":
                    print('Some of the important properties of the circle are as follows:\n\
The circles are said to be congruent if they have equal radii\n\
The diameter of a circle is the longest chord of a circle\n\
Equal chords of a circle subtend equal angles at the centre\n\
The radius drawn perpendicular to the chord bisects the chord\n\
Circles having different radius are similar\n\
A circle can circumscribe a rectangle, trapezium, triangle, square, kite\n\
A circle can be inscribed inside a square, triangle and kite\n\
The chords that are equidistant from the centre are equal in length\n\
The distance from the centre of the circle to the longest chord (diameter) is zero\n\
The perpendicular distance from the centre of the circle decreases\
             when the length of the chord increases\n\
If the tangents are drawn at the end of the diameter, they are parallel to each other\n\
An isosceles triangle is formed when the radii joining the ends of a chord to the centre of a circle')
                    r = (int(input("Enter circle's radius length: ")))
                    area = m.pi*m.pow(r,2)
                    print("The area of circle is ",area)
            elif shape == 'parallelogram':
                print(' The properties of a parallelogram are as follows:\n\
The opposite sides are parallel and equal\n\
The opposite angles are equal\n\
The consecutive or adjacent angles are supplementary\n\
If any one of the angles is a right angle, then all the other angles will be at right angle\n\
The two diagonals bisect each other\n\
Each diagonal bisects the parallelogram into two congruent triangles\n\
The Sum of the square of all the sides of a parallelogram is equal to the sum of the square of its diagonals.\
It is also called parallelogram law')
                b = int(input("Enter parallelogram's base length: "))
                h = int(input("Enter parallelogram's height length: "))
                area = b * h
                per=2*(b+h)
                print("The area of parallelogram is",area)
                print('perimeter:',per)
            else:
                print("Sorry! This shape is not available")
            
        elif n=='3d':
            shape=(input(' enter a 3d shape name'))
            if shape=='cone':
                print('A cone is a shape formed by using a set of line segments or the lines whichconnects a common point,\n\
called the apex or vertex, to all the points of a circular base(which does not contain the apex).\
The distance from the vertex of the cone to the base is the height of the cone. The circular base has measured value of radius. And the length of the cone from apex to any point on the circumference of the base is the slant height. Based on these quantities, there are formulas derived for surface area and volume of the cone. In the figure you will see, \
the cone which is defined by its height, the radius of its base and slant height')
                h = float(input("What is the height of the cone? "))
                r = float(input("What is the radius of the cone? "))
                volume= (1/3 *m.pi * m.pow(r,2) * h)
                sur_area = (m.pi* r * (r + l))
                print("Volume:",volume)
                print("Surface Area:", sur_area)

            elif shape=='cube':
                print('The following are the important properties of cube:\n\
It has all its faces in a square shape.\n\
All the faces or sides have equal dimensions.\n\
The plane angles of the cube are the right angle.\n\
Each of the faces meets the other four faces.\n\
Each of the vertices meets the three faces and three edges.\n\
The edges opposite to each other are parallel.')
                s= float(input("What is the length of one side of the cube? "))
                volume= (m.pow(s,3))
                sur_area= (6* m.pow(s,2))
                print("Volume:",volume)
                print("Surface Area:", sur_area )

            elif shape== 'cylinder':
                print('cylinders properties:\n\
The bases are always congruent and parallel.\n\
If the axis forms a right angle with the bases, \n\
                      which are exactly over each other, then it is called a “Right Cylinder”.\n\
It is similar to the prism since it has the same cross-section everywhere.\n\
If the bases are not exactly over each other but sideways, and the axis does not produce\n\
the right angle to the bases, then it is called “Oblique Cylinder”.\n\
If the bases are circular in shape, then it is called a right circular cylinder.\n\
If the bases are in an elliptical shape, then it is called an “Elliptical Cylinder”.\n\
To learn more properties of cylinder.')
                h = float(input("enter the height of the cylinder? "))
                r = float(input("enter the radius of the cylinder? "))
                volume= (m.pi * m.pow(r,2) * h)
                sur_area= (2 * m.pi* r * h + 2 * m.pi* m.pow(r,2))
                print("Volume:",volume)
                print("Surface Area:", surface_area)

            elif shape == 'cuboid':
                print('Properties of Cuboid\n\
A cuboid has 6 faces, 12 edges and 8 vertices\n\
The faces of the cuboid are all rectangular in shape\n\
Opposite edges of the cuboid are parallel to each other\n\
Cuboid has three dimensions: length, width and height\n\
Angles formed at the vertices of the cuboid are all 90 degrees')
                l = int(input("enter the length "))
                b = int(input("enter  the breath  "))
                h = int(input("enter the height  "))
                volume= (l * b * h)
                sur_area = (2 *(l*b+b*h+h*l))
                print("Volume:",volume)
                print("Surface Area:", sur_area)    

            elif shape== 'pyramid':
                print('A pyramid is a three-dimensional shape.\n A pyramid has a polygonal base and flat triangular faces, which join at a common point called the apex.\n A pyramid is formed by connecting the bases to an apex.\n Each edge of the base is connected to the apex, and forms the triangular face, called the lateral face.\n If a pyramid has an n-sided base, then it has n+1 faces, n+1 vertices, and 2n edges.A pyramid is a three-dimensional shape. \nA pyramid has a polygonal base and flat triangular faces, which join at a common point called the apex. \n\
A pyramid is formed by connecting the bases to an apex.\n\Each edge of the base is connected to the apex, and forms the triangular face, called the lateral face.\
If a pyramid has an n-sided base, then it has n+1 faces, n+1 vertices, and 2n edges.')
                l = int(input("enter the length of the pyramid's base? "))
                w = int(input(" enter the width of the pyramid's base? "))
                h = int(input("What is the height of the pyramid? "))
                vol= (l * w * h / 3)
                sur_area = ((l * w) + l * sqrt(m.pow(w/2,2) +m.pow(h,2)) + w * sqrt(m.pow(l/2,2) + m.pow(h,2)))
                print("Volume:", vol)
                print("Surface Area:", sur_area)

            elif shape=='sphere':
                print('The important properties of the sphere are given below.\n\
These properties are also called attributes of the sphere.\n\
A sphere is perfectly symmetrical\n\
A sphere is not a polyhedron\n\
All the points on the surface are equidistant from the center\n\
A sphere does not have a surface of centers\n\
A sphere has constant mean curvature\n\
A sphere has a constant width and circumference')
                print(' it has 1 curved surface')
                r = float(input("What is the radius of the sphere? "))
                vol= (4 * m.pi* m.pow(r,3) / 3)
                sur_area = (4 *m.pi * m.pow(r,2))
                print("Volume:",vol)
                print("Surface Area:", sur_area)

            elif shape=='hemisphere':
                print('Properties of a Hemisphere:\n\
    A hemisphere has one curved surface and one flat circular base\n\
    Just like a sphere a hemisphere has no edges or vertices\n\
    A line segment that connects two opposite points on the circumference of the circular base of a hemisphere and passes through its center is said to be the diameter of the hemispher e\n\A line segment from the center of the circular base to any point on its curved surface is the radius of the hemisphere')
                r = int(input("enter the radius of the hemisphere? "))
                volume= ((2 *m.pi* m.pow(r,3)) / 3)
                sur_area = (3 *m.pi* m.pow(r,2))
                print("Volume:", volume)
                print("Surface Area:",sur_area)
            else:
                print('sorry! shape not found')
        else:
            print('wrong choice')
    elif a=="no":
        break
    else:
        print('wrong choice')
