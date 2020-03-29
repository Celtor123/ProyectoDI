import webbrowser as wb

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import sqlite3 as base

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import doctest

conectar = base.connect("Cliente.dat")
print(conectar)
cursor = conectar.cursor()
#cursor.execute("drop table if exists clientes")
#cursor.execute("drop table if exists servicios")
cursor.execute("create table if not exists clientes  (dni text primary key not null unique,nombre text,departamento text)")
cursor.execute("create table if not exists servicios  (producto text not null,servicio text not null)")
# cursor.execute("insert into clientes values('4345636H','Celo','Casero')")
#cursor.execute("insert into servicios values('Rueda','Material')")
conectar.commit()

"""
Clase principal en la que una ventana contiene 3 botones para salir, ir a xestión de clientes o productos;
además de pasar el estilo en css para modelar las ventanas y sus componentes

"""



class Pepe(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,name="ventanaprincipal", border_width=23)
        self.set_default_size(800, 500)
        self.grid = Gtk.Grid(row_homogeneous=True, column_homogeneous=True, row_spacing=10, column_spacing=10,border_width=5)
        header=Gtk.HeaderBar(title="Ventana Principal",name="barra")
        self.set_titlebar(header)



        Boton1 = Gtk.Button(label="Xestión de clientes", name="boton1")
        self.Boton2 = Gtk.Button(label="Productos/servizos", name="boton2")
        botonsalir = Gtk.Button(label="Salir", name="salir")
        css_provider = Gtk.CssProvider()
        css = """
        #impresion:focus{
         color:red;
         background:orange;
        }
        window treeview{
         background:#c7dce7;
        }
        window entry{
        color:orange;
        }
        #ventanaterciaria label{
        color:orange;
        }
        #ventanaterciaria button label{
        color:red;
        }
        window entry{
         background:black;
        }
        #ventanaterciaria button:active{
        background:black;
        }
        window treeview:hover{
         color:blue;
         background:white;
        }
        window treeview:focus{
         color:orange;         
        }
         #ventanaprincipal {
        background: #f4e06d; 
         }
          #barra {
        background: #81a0bd; 
        color:#0d0d0f;
        font-size:30px;
        font-family: "garamond open"
         }
         #arbol{
         color:green;
         background:white;
         }
          #arbol:hover{
         background:grey;
         }
          #arbol:focus{
         background:grey;
         
        }
         .entry{
         background:red;
         }
        
          #ventanasecundaria{
        background: #f4e06d;
         }
          #combo:hover{
          color: #f4e06d;
         }
           #paquete{
        background: #f4e06d;
         }
         
        #boton1 {
        color:#f594ec; 
        background:#e2eef2;
        font-size:40px;
        font-family: "garamond open";
        
        }
        #boton1:hover{
        background:white;
        }
        #boton2:hover{
        background:white;
        }
        #boton2{
        color: #f594ec; 
        background:#e2eef2;
        font-size:40px;
        font-family: univers;
        }
        #salir{
        color:red;
        background: #f3edca;  
        font-size: 70px;     
        font-style: normal; 
        font-family: Bodony MT Black;          
        }
     #salir:active {
     background:red;
     
}
        """
        # Información sobre css ->https://developer.mozilla.org/es/docs/Web/CSS/:focus       BORRAR AL ACABAR¡¡¡¡¡¡¡¡¡¡¡¡
        # LInk informacion señales de widgets https://lazka.github.io/pgi-docs/Gtk-3.0/classes/ComboBox.html (Este es el de Combobox)

        css_provider.load_from_data(bytes(css.encode()))
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        # print(dir(css_provider))
        Boton1.connect("clicked", self.Xestion)
        self.Boton2.connect("clicked", self.Producto)
        # Boton3.connect("clicked",self.imprimir)
        # Boton4.connect("clicked",self.arbol)
        botonsalir.connect("clicked", self.salir)
        self.grid.attach(Boton1, 0, 0, 8, 8)
        self.grid.attach(self.Boton2, 8, 0, 8, 8)
        # self.grid.add(Boton3)
        # self.grid.add(Boton4)
        self.grid.attach(botonsalir, 4, 8, 8, 4)
        self.add(self.grid)


    def salir(self, widget):
        Gtk.main_quit()



        """
        Esta es la ventana donde aparencen los servicios y productos a través de  un treeview, 
        los cuales el usuario decide que hacer en el combobox               
        """

    class Producto(Gtk.Window):
        def __init__(self, widget):
              Gtk.Window.__init__(self, title="Xestión de clientes", name="ventanaproductos")


              cerrado=win
              cerrado.set_visible(False)
              def cerrar(self):
                  cerrado.set_visible(True)
              self.connect("destroy", cerrar)
              re = []
              raa={"asd","ass","afae"}
              self.set_default_size(150,70)
              grid=Gtk.Grid()
              label=Gtk.Label("Lista de Servicios")
              lista=Gtk.ListStore(str,str)
              boton1=Gtk.Button("Nuevo")
              boton1.connect("clicked",self.nuevoser)
              boton2=Gtk.Button("Eliminar")
              boton2.connect("clicked", self.eliminarser)
              botonimprimir=Gtk.Button("Imprimir")
              botonimprimir.connect("clicked",self.imprimir)

              "TreeView"
              #Donde se guarda el nombre de columnas,
              # importante cambiarlo si se cambian estas
              titulos=["Producto","Servicio"]
              pregunta=cursor.execute("select * from servicios")
              cont=type
              columna=0

              for cont in pregunta:
                lista.append(cont)
                re.append(cont)
                columna=len(cont)
              arbolito = Gtk.TreeView(lista)
              print(re)
              for a in range(columna):
                  renderer=Gtk.CellRendererText()
                  column=Gtk.TreeViewColumn(titulos[a],renderer,text=a)
                  column.set_clickable(True)
                  arbolito.append_column(column)


              grid.attach(label,0,0,4,2)
              grid.attach(arbolito,0,2,4,4)
              grid.attach(boton1, 0, 6, 2, 4)
              grid.attach(boton2, 2, 6, 2, 4)
              grid.attach(botonimprimir,1,10,2,4)
              self.add(grid)
              self.show_all()

        def imprimir(self, widget):
                  """
                      >>> imprimir()
                      2
                      """

                  doc = SimpleDocTemplate("Facturacion2.pdf", pagesize=A4)
                  presentacion = [["Aqui aparece una tabla con todos los clientes que tienen ahora mismo productos"] + [
                      "Cualquier duda o sugerencia comentársela al creador Celso.S.R."]]
                  elements = []
                  cursor.execute("select * from servicios")
                  # a=cursor.execute("select * from empleados")
                  # lista=cursor.fetchall()
                  # cosa=[]
                  # for cosas in lista:
                  #    cosa.append(cosas)
                  # print(cosa[0])
                  titulo = ("Productos","Servicios")
                  data = []
                  data.append(titulo)
                  for tupla in cursor.fetchall():
                      data.append(tupla)

                  # print(tupla)
                  x: int = len(tupla)

                  i = len(data)
                  t = Table(data, x * [3 * cm], i * [1.5 * cm])
                  t.setStyle(TableStyle([
                      ('BACKGROUND', (0, 0), (4, 0), colors.violet),
                      ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                      ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                  ]))

                  elements.append(t)
                  doc.build(elements)
                  wb.open_new("Facturacion2.pdf")
                  return x
                  """
                  def _test_imprimir():
                        doctest.testmod(verbose=True)
                        if __name__ == "__main__":
                            test_imprimir()
                                    """





        class nuevoser(Gtk.Window):
            def __init__(self, widget):
                Gtk.Window.__init__(self,title="Ingresar Producto y Servicio")
                #asado=win.Producto(self)
                #print(esc)
                self.set_default_size(300,300)
                def acepta(widget):
                    a=cursor.execute("insert into servicios values('"+entrada1.get_text()+"','"+entrada2.get_text()+"')")
                    conectar.commit()
                grid=Gtk.Grid()
                label1=Gtk.Label("Servicio")
                label2=Gtk.Label("Producto")
                entrada1=Gtk.Entry()
                entrada2=Gtk.Entry()


                aceptar=Gtk.Button("Aceptar")
                aceptar.connect("clicked",acepta)
                grid.attach(label1,0,0,2,1)
                grid.attach(label2,2,0,2,1)
                grid.attach(entrada1,0,2,2,1)
                grid.attach(entrada2,2,2,2,1)
                grid.attach(aceptar,1,3,2,1)
                self.add(grid)

                self.show_all()
        class eliminarser(Gtk.Window):
            def __init__(self,widget):
                Gtk.Window.__init__(self,title="Elimina Producto y Servicio")
                self.set_default_size(300,300)

                grid=Gtk.Grid()
                def elimina(widget):
                    a=cursor.execute("delete from servicios where producto='"+entrada2.get_text()+"' or servicio='"+entrada2.get_text()+"'")
                    conectar.commit()


                label1 = Gtk.Label("Servicio")
                label2 = Gtk.Label("Producto")
                entrada1 = Gtk.Entry()
                entrada2 = Gtk.Entry()


                borrar = Gtk.Button("Eliminar")
                borrar.connect("clicked", elimina)
                grid.attach(label1,2,0,2,1)
                grid.attach(label2,0,0,2,1)
                grid.attach(entrada1,2,1,2,1)
                grid.attach(entrada2,0,1,2,1)
                grid.attach(borrar,1,2,2,1)
                self.add(grid)
                self.show_all()




    """Clase Xesatión hace que aparezca un listado de clientes y unas acciones para hacer con ellos que son añadir, elminir y consultarlos"""

    class Xestion(Gtk.Window):
        def __init__(self,widget):
            Gtk.Window.__init__(self, title="Xestión de clientes",name="ventanasecundaria")
            clase=win
            clase.set_visible(False)
            def salir(self):
                clase.set_visible(True)
            self.connect("destroy",salir)

            self.b = None
            self.set_default_size(800, 500)
            paquete = Gtk.Grid(row_homogeneous=True, column_homogeneous=True, orientation=Gtk.Orientation.VERTICAL,row_spacing=2,name="paquete")
            print(dir(paquete))
            self.destino = False
            lista = Gtk.ListStore(str)
            listado = ["Insertar", "Consultar", "Borrar"]
            for algo in listado:
                lista.append([algo])
            combo = Gtk.ComboBox.new_with_model(lista)
            combo.set_name("combo")
            combo.connect("changed", self.combo_changed)
            renderer_text = Gtk.CellRendererText()
            combo.pack_start(renderer_text, True)
            combo.add_attribute(renderer_text, "text", 0)
            combo.set_entry_text_column(0)

            label = Gtk.Label(label="Lista de Clientes")
            paquete.attach(combo, 0, 0, 1, 1)
            paquete.attach_next_to(label, combo, Gtk.PositionType.BOTTOM, 1, 1)

            store = Gtk.ListStore(str, str, str)
            titulo = ("DNI", "Nombre", "Departamento")
            data = []
            data.append(titulo)
            tupla = cursor.execute("select * from clientes")
            for algo in tupla:
                store.append(algo)
                columna = len(algo)
            print(columna)
            # forma Treeview
            tree = Gtk.TreeView(store)
            conectar.commit()

            def on_tree_selection_changed(selection):
                model, treeiter = selection.get_selected()
                self.destino = True
                if treeiter is not None and self.destino is True:
                    print("You selected", model[treeiter][0])
                    self.b = model[treeiter][0]

            for a in range(columna):
                # forma celda
                renderer = Gtk.CellRendererText()
                # crea una fila
                column = Gtk.TreeViewColumn(titulo[a], renderer, text=a)
                # Ordena las filas
                column.set_sort_column_id(a)
                column.set_clickable(True)
                # añade al treeview el contenido de la columna
                tree.append_column(column)
            select = tree.get_selection()
            select.connect("changed", on_tree_selection_changed)
            boton=Gtk.Button(label="Imprimir",name="impresion")
            boton.connect("clicked",self.imprimir)

            paquete.attach(tree, 0, 2, 1, 10)
            paquete.attach_next_to(boton,tree, Gtk.PositionType.BOTTOM, 1, 1)
            self.add(paquete)
            self.show_all()

        def combo_changed(self,combo):
             tree_iter = combo.get_active_iter()
             self.destino = True
             if tree_iter is not None:
                model = combo.get_model()
                country = model[tree_iter][0]
                self.Opciones(country,self.b)

        def imprimir(self, widget):
            """
                >>> imprimir()
                2
                """

            doc = SimpleDocTemplate("Facturacion.pdf", pagesize=A4)
            presentacion=[["Aqui aparece una tabla con todos los clientes que tienen ahora mismo productos"]+["Cualquier duda o sugerencia comentársela al creador Celso.S.R."]]
            elements = []
            cursor.execute("select * from clientes")
            # a=cursor.execute("select * from empleados")
            # lista=cursor.fetchall()
            # cosa=[]
            # for cosas in lista:
            #    cosa.append(cosas)
            # print(cosa[0])
            titulo = ("DNI", "Nombre", "Departamento")
            data = []
            data.append(titulo)
            for tupla in cursor.fetchall():
                data.append(tupla)

            # print(tupla)
            x = len(tupla)

            i = len(data)
            t = Table(data, x * [3 * cm], i * [1.5 * cm])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (4, 0), colors.gray),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
            ]))

            elements.append(t)
            doc.build(elements)
            wb.open_new("Facturacion.pdf")
            return x;

        """def _test_imprimir():
            doctest.testmod(verbose=True)
        if __name__ == "__main__":
            _test_imprimir()"""


        class Opciones(Gtk.Window):
            def __init__(self, string,strar):
                Gtk.Window.__init__(self, title=string + " cliente",name="ventanaterciaria")
                self.set_default_size(200,74)
                #win.set_visible(False)



                if string == "Consultar":

                    def cliente(self):

                        tree_iter = comba.get_active_iter()


                        if tree_iter is not None:
                            model = comba.get_model()
                            pais = model[tree_iter][0]
                            d = cursor.execute("select * from clientes where dni ='" + pais + "'")
                            for i in d:
                                liston.append(i)
                                print(i)
                            listo=liston
                            # forma celda
                            renderer = Gtk.CellRendererText()
                            print("al")
                            a=arbol.get_columns()
                            if a is not None:
                             for te in a:
                              arbol.remove_column(te)
                            for al in range(3):
                                print(al)
                                columna = Gtk.TreeViewColumn(titulo[al], renderer, text=al)
                                # Ordena las filas
                                columna.set_sort_column_id(al)
                                columna.set_clickable(True)
                                arbol.append_column(columna)


                                # crea una fila



                    grid = Gtk.Grid()

                    lista = Gtk.ListStore(str)
                    liston = Gtk.ListStore(str, str, str)
                    a = cursor.execute("select dni from clientes ")
                    for u in a:
                        lista.append(u)
                    con = (len(lista))
                    titulo = ("DNI", "Nombre", "Departamento")
                    liston.clear()

                    comba = Gtk.ComboBox.new_with_model(lista)
                    comba.connect("changed", cliente)
                    renderer_text = Gtk.CellRendererText()
                    comba.pack_start(renderer_text, True)
                    comba.add_attribute(renderer_text, "text", 0)
                    comba.set_entry_text_column(0)
                    arbol = Gtk.TreeView(liston)
                    arbol.set_name("arbol")
                    grid.attach(comba, 0, 0, 1, 1)
                    grid.attach(arbol, 1, 2, 4, 4)
                    self.add(grid)
                elif string == "Insertar":
                    def ingresar(self):
                        s = cursor.execute(
                            "Insert into clientes (Dni,nombre,departamento) values ('"+dni.get_text()+"','"+nombre.get_text()+"','"+depar.get_text()+"')")
                        #LO DEJÉ AQUÍ
                    grid=Gtk.Grid(border_width=20,row_spacing=10,column_spacing=10)
                    labdni=Gtk.Label("DNI")
                    labnomb=Gtk.Label("NOMBRE")
                    labdepar=Gtk.Label("DEPARTAMENTO")
                    dni=Gtk.Entry()
                    nombre=Gtk.Entry()
                    depar=Gtk.Entry()
                    Ok=Gtk.Button(label="Ingresar")
                    Ok.connect("clicked",ingresar)
                    grid.attach(labdni,0,0,1,1)
                    grid.attach(labnomb,1,0,1,1)
                    grid.attach(labdepar,2,0,1,1)
                    grid.attach(dni, 0, 1, 1, 1)
                    grid.attach(nombre, 1, 1, 1, 1)
                    grid.attach(depar, 2, 1, 1, 1)
                    grid.attach(Ok, 0, 2, 3, 3)
                    self.add(grid)
                elif string == "Borrar":
                    def ingresar(self):
                        s = cursor.execute(
                            "delete from clientes where Dni = '"+dni2.get_text()+"'")
                        k = cursor.execute(
                            "delete from clientes where nombre = '"+nombre2.get_text()+ "';")
                        l = cursor.execute(
                            "delete from clientes where departamento = '"+depar2.get_text()+"';")
                        #LO DEJÉ AQUÍ


                    grid=Gtk.Grid(border_width=20,row_spacing=10,column_spacing=10)
                    labdni=Gtk.Label("DNI")
                    labnomb=Gtk.Label("NOMBRE")
                    labdepar=Gtk.Label("DEPARTAMENTO")
                    dni2=Gtk.Entry()
                    nombre2=Gtk.Entry()
                    depar2=Gtk.Entry()
                    Ok=Gtk.Button(label="Eliminar")


                    Ok.connect("clicked",ingresar)
                    grid.attach(labdni,0,0,1,1)
                    grid.attach(labnomb,1,0,1,1)
                    grid.attach(labdepar,2,0,1,1)
                    grid.attach(dni2, 0, 1, 1, 1)
                    grid.attach(nombre2, 1, 1, 1, 1)
                    grid.attach(depar2, 2, 1, 1, 1)
                    grid.attach(Ok, 0, 2, 3, 3)

                    self.add(grid)






                self.show_all()



win = Pepe()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
