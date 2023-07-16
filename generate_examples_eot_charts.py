# Test generate_star_chart functions
# python3 generate_examples_eot_charts.py
import muller_eot

if __name__ == '__main__':
	# Planet Name, Eccentricity, Obliquity, Semimajor Axis (AU)
	#planet_lst = [["Mercury", 0.2056, 0.1, 0.3871],
	#				["Venus", 0.0068, 87.3, 0.7233], 
	#				["Earth", 0.0167, 23.45, 1.0000001124],
	#				["Mars", 0.0934, 25.19, 1.5273],
	#				["Jupiter", 0.0484, 3.12, 5.2028],
	#				["Saturn", 0.0541, 26.73, 9.5388],
	#				["Uranus", 0.0472, 97.86, 19.1914],
	#				["Neptune", 0.0086, 29.56, 30.0611]]


	earth_eot = muller_eot.EOT(eccentricity=0.0167, obliquity=23.45, orbit_period=365.25)
	earth_eot.plotEOT(save_plot_name="examples/earth_quickstart.png")

	earth_eot = muller_eot.EOT(eccentricity=0.0167, obliquity=23.45, orbit_period=365.25)
	title = "Earth: Effect of Eccentricity ({0}) and Obliquity ({1}) (Min={2:.4f}, Max={3:.4f})".format(0.0167, 
																								23.45,
																								min(earth_eot.eotDayAndMinutes.values()), 
																								max(earth_eot.eotDayAndMinutes.values()))
	earth_eot.plotEOT(plot_title=title,
					save_plot_name="examples/earth_eot_testing.png")

	earth_eot = muller_eot.EOT(eccentricity=0.0167, obliquity=0, orbit_period=365.25)
	title = "Earth: Effect of Eccentricity ({0}) (Min={1:.4f}, Max={2:.4f})".format(0.0167, 
																			min(earth_eot.eotDayAndMinutes.values()), 
																			max(earth_eot.eotDayAndMinutes.values()))
	earth_eot.plotEOT(plot_title=title,
					save_plot_name="examples/earth_eccentricity_testing.png")

	earth_eot = muller_eot.EOT(eccentricity=0, obliquity=23.45, orbit_period=365.25)
	title = "Earth: Effect of Obliquity ({0}) (Min={1:.4f}, Max={2:.4f})".format(23.45, 
																		min(earth_eot.eotDayAndMinutes.values()), 
																		max(earth_eot.eotDayAndMinutes.values()))
	earth_eot.plotEOT(plot_title=title,
					save_plot_name="examples/earth_obliquity_testing.png")
