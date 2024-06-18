import tkinter as tk
from tkinter import PhotoImage
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import serial
import time
from serial.serialutil import SerialTimeoutException
import mplcursors
import os
import csv
c = 0
global memory
global flag
flag=0
memory = [0.0, 0.0, 0.0, 0.0, 0.0,0.0]
if os.path.exists(r'C:\Users\DELL\OneDrive\Desktop\cansat\Flight_2022ASI-049.csv'):
    with open(r'C:\Users\DELL\OneDrive\Desktop\cansat\Flight_2022ASI-049.csv', 'r') as file:
        reader = csv.reader(file)
        last_row = None
        for row in reader:
            last_row = row

    if last_row is not None:
        data_elements = last_row
        memory[0]= float(data_elements[15])
        memory[1]=float(data_elements[16])
        memory[2]= float(data_elements[17])
        memory[3]= float(data_elements[5])
        memory[4]= float(data_elements[3])
        memory[5]= float(data_elements[18])
else:
    memory = [0.0, 0.0, 0.0, 0.0, 0.0,0.0]

                
def read_data():
    global memory
    ser=serial.Serial('COM4', 9600)
    while True:
        try:
            if ser.in_waiting > 1:
                global data_str
                packet = ser.readline()
                data_str = packet.decode('utf-8').split("<")[1].split(">")[0]
                print(data_str)
                data_elements = data_str.split(",")
                row = [float(data_elements[15]), float(data_elements[16]), float(data_elements[17]), float(data_elements[5]), float(data_elements[3]), int(data_elements[18])]
                print(row)
                memory=row
                
                yield row
            else:
                print(memory)
            
                yield memory
                
            
            
        except serial.SerialException as e:
            print("Serial port error:", e)
            yield memory
        except Exception as e:
            print("An error occurred:", e)
            yield memory


def update_plot():
    scale=0.1
    global flag
    data_packet = next(data_generator)
    ax.cla()
    global c 
    if c == 0:
        roll_deg = np.degrees(0)
        pitch_deg = np.degrees(0)
        yaw_deg = np.degrees(0)
        c = 1
    else:
        roll_deg = np.degrees(data_packet[0]*scale)
        pitch_deg = np.degrees(data_packet[2]*scale)
        yaw_deg = np.degrees(data_packet[1]*scale)

    draw_3d_cylinder(ax, roll_deg, pitch_deg, yaw_deg)
    
  
    time.append(time[-1] + 1)  
    index5_data.append(data_packet[3])  
    index3_data.append(data_packet[4])  
    
    ax1.clear()
    ax1.plot(time, index5_data, label='Temperature', color='#FF5733')  
    ax1.legend()
    ax1.set_xlabel('Time (sec)', color='white')
    ax1.set_ylabel('Temperature (℃)', color='white') 
    ax1.tick_params(axis='x', colors='white') 
    ax1.tick_params(axis='y', colors='white') 

    
    
    ax2.clear()  
    ax2.plot(time, index3_data, label='Altitude/Trajectory', color='#FF5733') 
    ax2.legend()  
    ax2.set_xlabel('Time (sec)', color='white')  
    ax2.set_ylabel('Altitude / Trajectory (m)', color='white')  
    ax2.tick_params(axis='y', colors='white')  
    ax2.tick_params(axis='x', colors='white') 

    if data_packet[4]==6 and flag==0:
        ax2.annotate('Rocket Deployed', xy=(time, index3_data), xytext=(time, index3_data + 10),
                 arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3'), color='white')
        flag=1
    
    canvas.draw()
    root.after(600, update_plot)

def draw_3d_cylinder(ax, roll, pitch, yaw):
    radius = 0.1
    height = 0.2
    half_height = height / 2

    num_vertices = 20
    theta = np.linspace(0, 2 * np.pi, num_vertices)
    circle_x = radius * np.cos(theta)
    circle_y = radius * np.sin(theta)


    vertices_top = np.array([circle_x, circle_y, np.full(num_vertices, half_height)]).T
    vertices_bottom = np.array([circle_x, circle_y, np.full(num_vertices, -half_height)]).T


    rotation_matrix = np.dot(np.dot(
        np.array([[np.cos(yaw), -np.sin(yaw), 0],
                  [np.sin(yaw), np.cos(yaw), 0],
                  [0, 0, 1]]),
        np.array([[np.cos(pitch), 0, np.sin(pitch)],
                  [0, 1, 0],
                  [-np.sin(pitch), 0, np.cos(pitch)]])),
        np.array([[1, 0, 0],
                  [0, np.cos(roll), -np.sin(roll)],
                  [0, np.sin(roll), np.cos(roll)]]))


    rotated_vertices_top = np.dot(vertices_top, rotation_matrix.T)
    rotated_vertices_bottom = np.dot(vertices_bottom, rotation_matrix.T)


    ax.clear()
  
    ax.add_collection3d(Poly3DCollection([rotated_vertices_top], color='orange', alpha=0.6, edgecolor='black'))
    ax.add_collection3d(Poly3DCollection([rotated_vertices_bottom], color='#595959', alpha=0.6, edgecolor='black'))

    for i in range(num_vertices - 1):
        side_vertices = [[rotated_vertices_top[i], rotated_vertices_top[i + 1],
                          rotated_vertices_bottom[i + 1], rotated_vertices_bottom[i]]]
        ax.add_collection3d(Poly3DCollection(side_vertices, color='orange', alpha=0.6, edgecolor='black'))

    side_vertices_last = [[rotated_vertices_top[-1], rotated_vertices_top[0],
                           rotated_vertices_bottom[0], rotated_vertices_bottom[-1]]]
    ax.add_collection3d(Poly3DCollection(side_vertices_last, color='orange', alpha=0.6, edgecolor='black'))\
    

    ax.set_xlim([-radius, radius])
    ax.set_ylim([-radius, radius])
    ax.set_zlim([-half_height, half_height])

    ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.grid(True)
    ax.tick_params(axis='x', colors='white')  # Set x-axis ticks color to white
    ax.tick_params(axis='y', colors='white')  # Set y-axis ticks color to white
    ax.tick_params(axis='z', colors='white')
    # ax.set_axis_off()
    # ax.set_facecolor('#A9A9A9')
    plt.draw()


root = tk.Tk()
root.title("3D Block Animation")
root.configure(bg='#303030') 
root.state('zoomed')

# Load the logo image
logo_image = PhotoImage(file="kalpana.png")

# Create a frame for the logo and label
logo_frame = tk.Frame(root, bg='#303030')
logo_frame.pack(side=tk.TOP, padx=10, pady=10)

# Add the logo to the frame
logo_label = tk.Label(logo_frame, image=logo_image, bg='#303030')
logo_label.pack(side=tk.LEFT)

team_label = tk.Label(logo_frame, text="Team Kalpana - ASI049", font=("Helvetica", 14, "bold"), fg="white", bg='#303030')
team_label.pack(side=tk.RIGHT, padx=(10, 0))

# Create main figure and axes for 3D rendering
fig = plt.Figure(facecolor='#303030',dpi=100)
ax = fig.add_subplot(121, projection='3d')
ax.set_facecolor('#303030')
ax.set_axis_off()

# Create subplot for real-time plots
ax1 = fig.add_subplot(224)  
ax2 = fig.add_subplot(222) 
time = [0]  
index5_data = [0]  
index3_data = [0]  

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

data_generator = read_data()
update_plot()  # Start updating the plot

root.mainloop()