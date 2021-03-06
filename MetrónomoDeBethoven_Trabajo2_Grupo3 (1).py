from scipy.special import factorial2 #Importación de la librería scipy para ocupar el factorial doble.
import numpy as np #Importación de la librería Numpy para usar linspace para graficar 25 puntos.
from matplotlib import pyplot as plt #Importación de la librería matplotlib para graficar .
from matplotlib.widgets import Slider, Button #Importación de matplotlib.widgets para hacer los slider y button.

def f(theta): #Función de calcular f(theta).
   sumatoria = np.array([(factorial2(2*n-1)/factorial2(2*n)*(np.sin(np.radians(theta/2)))**(2*n))**2 for n in range(1,151)]) 
   return 1 + np.sum(sumatoria)

def Omega(g,theta,M,m,R,u,l,L,r): #Función de calcular Omega(g,theta,M,m,R,u,l,L,r).
    M_prima = M/m
    u_prima = u/m
    a0 = (g/(f(theta)**2))*(((M_prima*R)-(u_prima/2)*(l-L))/((M_prima*(R**2))+(u_prima/3)*(L**2+l**2-l*L)))
    b2 = -(1/(M_prima*(R**2) + (u_prima/3)*(L**2 + l**2 - l*L)))
    omega = (a0 + (b2*g*r)/f(theta)**2) / (1-(b2*r**2))
    return omega


r_grafico = np.linspace(40,208,25) #linspace para graficar 25 puntos, (r[mm]).
#Llamado a la función Omega para Obtener el valor en y, (Omega[Hz]).
omega_grafico=Omega(g=9800,
                    theta=50,
                    M=25,
                    m=6,
                    R=45,
                    u=4.25,
                    l=100,
                    L=20,
                    r=r_grafico)

%matplotlib qt 
fig = plt.figure()  #Creamos una figura y la guardamos en la variable fig.
ax = fig.subplots() #Creamos un subgráfico y lo guardamos en la variable ax.
plt.subplots_adjust(left = 0.05, bottom = 0.44, right=0.95) #Ajustamos el subgráfico para tener una mejor una mejor visión.
p, = ax.plot(r_grafico, omega_grafico,'-ok', label = "Modelo Matemático del Metrónomo de Beethoven",color="darkred") #Graficamos la función, así como su label, color y su tipo de línea.
plt.grid() #Colocamos una cuadrilla.
plt.legend() #Colocamos una leyenda.
plt.xlabel("r [mm]",size=15,color='darkred') #Nombramos al eje x.
plt.ylabel("$Ω^2[Hz^2]$",size=15,color='darkred') #Nombramos al eje y.
plt.title("Metrónomo de Beethoven",weight='bold',size=30,color='darkred') #Nombramos al título de nuestra gráfica.
plt.ylim(-20,150)
#Creamos el esquema de los sliders a utilizar, tamaño y posición.
ax_g = plt.axes([0.06, 0.30, 0.38, 0.045])
ax_Theta = plt.axes([0.05, 0.23, 0.40, 0.045])
ax_M = plt.axes([0.05, 0.16, 0.40, 0.045])
ax_m = plt.axes([0.05, 0.09, 0.40, 0.045])
ax_R = plt.axes([0.55, 0.30, 0.40, 0.045])
ax_u = plt.axes([0.55, 0.23, 0.40, 0.045])
ax_l = plt.axes([0.55, 0.16, 0.40, 0.045])
ax_L = plt.axes([0.55, 0.09, 0.40, 0.045])
ax_Graficar = plt.axes([0.85, 0.90, 0.1, 0.05])

#Creamos los sliders que nos permitan controlar cada una de las variables de nuestra función en el gráfico.
#El primer párametro hace referencia al objeto al cual le asociamos y luego colocamos el nombre, valor mín y max, el valor en el cual comienza y color.
g_= Slider(ax=ax_g,label="$g [mm/s^2]$",valmin=400,valmax=9800,valinit=9800,valstep=100, color="dimgray")
theta_= Slider(ax=ax_Theta,label="θ [°]",valmin=40,valmax=60,valinit=50,valstep=0.1, color="moccasin")
M_= Slider(ax=ax_M,label="M [g]",valmin=23,valmax=36,valinit=25,valstep=0.1, color="turquoise")
m_= Slider(ax=ax_m,label="m [g]",valmin=5,valmax=8,valinit=6,valstep=0.01, color="lime")
R_= Slider(ax=ax_R,label="R [mm]",valmin=35,valmax=70,valinit=45,valstep=0.05, color="slateblue")
u_= Slider(ax=ax_u,label="µ [g]",valmin=3.5,valmax=5,valinit=4.25,valstep=0.01, color="palegreen")
l_= Slider(ax=ax_l,label="l [mm]",valmin=90,valmax=255,valinit=100,valstep=0.01, color="yellow")
L_= Slider(ax=ax_L,label="L [mm]",valmin=15,valmax=70,valinit=20,valstep=0.05, color="teal")
Reinicar_=Button(ax=ax_Graficar,label='REINICIAR')#Procedemos a crear un botón que nos servirá para reiniciar la gráfica.

#Creamos una función que vincule los valores de la gráfica y los sliders.
def restaurar(valores_nuevos):
    p.set_ydata(Omega(g_.val,theta_.val,M_.val,m_.val,R_.val,u_.val,l_.val,L_.val,r_grafico))
    fig.canvas.draw_idle()

#Esta herramienta permite que los valores en cada variable se cambien de acuerdo a la función que establecemos en cada instante.
g_.on_changed(restaurar)
theta_.on_changed(restaurar)
M_.on_changed(restaurar)
m_.on_changed(restaurar)
R_.on_changed(restaurar)
u_.on_changed(restaurar)
l_.on_changed(restaurar)
L_.on_changed(restaurar)

#Creamos una funcion que vincule el botón para actualizar la gráfica y los parámetros.
def reseteo(gráfica):
    g_.reset()
    theta_.reset()
    M_.reset()
    m_.reset()
    R_.reset()
    u_.reset()
    l_.reset()
    L_.reset()
Reinicar_.on_clicked(reseteo) #Reiniciamos la gráfica





