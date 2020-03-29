import sqlite3 as base
#from os import startfile
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

conectar=base.connect("Cliente.dat")
print(conectar)
cursor=conectar.cursor()
#cursor.execute("drop table if exists empleados")
cursor.execute("create table if not exists empleados  (Dni text primary key not null,nombre text,departamento text)")
#cursor.execute("insert into empleados values('927023k','Loquillo','Jefe 1A')")
conectar.commit()

class salida(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Arbol")
        tupla=cursor.execute("select * from empleados")
        todo=[]
        store = Gtk.ListStore(str, str, str)

        #obtener el número de filas
        for imprimir in tupla:
            store.append(imprimir)
            columna=imprimir
           #todos los elementos
            for b in imprimir:
                elemento=b
        columna=len(columna)
        elemento=len(elemento)
        print(columna)
        #obtenemos columnas
        fila=int(elemento/columna)
        print(fila)


        # forma Treeview
        tree = Gtk.TreeView(store)
        lista="dni","Nombre","Departamento"
        for a in range (columna):
        # forma celda
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(lista[a], renderer, text=a)
            tree.append_column(column)


        self.add(tree)
        self.show_all()
        self.connect("destroy", Gtk.main_quit)
        cursor.close()
def hello(c):
    from reportlab.lib.units import inch
    # move the origin up and to the left
    c.translate(inch,inch)
    # define a large font
    c.setFont("Helvetica", 14)
    # choose some colors
    c.setStrokeColorRGB(0.2,0.5,0.3)
    c.setFillColorRGB(1,0,1)
    #draw some lines
    c.line(0,0,0,1.7*inch)
    c.line(0,0,1*inch,0)
    #draw rectangle
    c.rect(0.2*inch,0.2*inch,1*inch,1.5*inch,fill=1)
    #make text go straight up
    c.rotate(90)
    c.setFillColorRGB(0,0,0.77)
    #say f
    c.drawString(0.3*inch,1*inch,"fffffffff")
    #dibuja una caja
    c.grid(xlist=(30,23),ylist=(16,8))
    #dibuja una linea asando por las diferentes coordenadas
    c.bezier(x1=10,y1=10,x2=20,y2=20,x3=3,y3=30,x4=40,y4=40)
    #dibuja una línea curva
    c.arc(x1=2,y1=10,x2=20,y2=100)
    #dibuja un rectángulo
    c.rect(x=23,y=45,width=100,height=10,stroke=1,fill=0)
    imprimir()
def imprimir():
 doc = SimpleDocTemplate("simple_table_grid2.pdf", pagesize=A4)
 elements = []
 cursor.execute("select * from empleados")
 #a=cursor.execute("select * from empleados")
 #lista=cursor.fetchall()
 #cosa=[]
 #for cosas in lista:
 #    cosa.append(cosas)
 #print(cosa[0])
 titulo=("DNI","Nombre","Departamento")
 data=[]
 data.append(titulo)
 for tupla in cursor.fetchall():
    data.append(tupla)
 print(tupla)
 x=(len(tupla))
 i=len(data)
 t=Table(data,x*[3*cm], i*[1.5*cm])
 t.setStyle(TableStyle([
     ('BACKGROUND',(0,0),(4,0),colors.gray),
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ]))

 elements.append(t)

 doc.build(elements)
#User Guide Chapter 2 Graphics and Text with pdfgen
#Page 11
    # draw some lines
# c.line(0,0,0,1.7*inch)
# c.line(0,0,1*inch,0)
# draw a rectangle
# c.rect(0.2*inch,0.2*inch,1*inch,1.5*inch, fill=1)
# make text go straight up
# c.rotate(90)
# change color.css
# c.setFillColorRGB(0,0,0.77)
# say hello (note after rotate the y coord needs to be negative!)
# c.drawString(0.3*inch, -inch, "Hello World"
c=canvas.Canvas("Celso1.pdf")
c.showPage()
c.save()
imprimir()
#startfile("Celso1.pdf")
conectar.close()
win = salida()
win.connect("destroy",Gtk.main_quit)
win.show_all()
Gtk.main()