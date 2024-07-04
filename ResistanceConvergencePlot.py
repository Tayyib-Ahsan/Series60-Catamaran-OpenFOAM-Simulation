import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use('ggplot')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
	f = open( 'C:/Users/ASUS/Desktop/ForGithub/S60_M_0.30_New_0.971/postProcessing/forces/0/force.dat' , "r" )
	g = f.readlines()
	del g[ :30 ]
	
	x  = []
	y0 = []
	# y1 = []
	for lines in g :
		reading = lines.split()
		x.append(float(reading[0]))
		y0.append(-float(reading[1])*2)

	# for i in x: y1.append( sum(y0[-100:]) / len(y0[-100:]) )
	
	# print( sum(y0[-100:]) / len(y0[-100:]) )



	ax1.clear()
	plt.xlabel("TimeStep")
	plt.ylabel("Resistance")
	ax1.plot(x, y0, linestyle = 'dashed')
	# ax1.plot(x, y1, linestyle = 'dashed')



ani = animation.FuncAnimation(fig, animate, interval = 10000) 
plt.show()




