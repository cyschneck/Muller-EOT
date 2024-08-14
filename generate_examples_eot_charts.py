# Test generate_star_chart functions
# python generate_examples_eot_charts.py
import muller_eot
import matplotlib.pyplot as plt

if __name__ == '__main__':
	# plt.style.use('dark_background')
	# Planet Name, Eccentricity, Obliquity, Semimajor Axis (AU)
	#planet_lst = [["Mercury", 0.2056, 0.1, 0.3871],
	#				["Venus", 0.0068, 87.3, 0.7233], 
	#				["Earth", 0.0167, 23.45, 1.0000001124],
	#				["Mars", 0.0934, 25.19, 1.5273],
	#				["Jupiter", 0.0484, 3.12, 5.2028],
	#				["Saturn", 0.0541, 26.73, 9.5388],
	#				["Uranus", 0.0472, 97.86, 19.1914],
	#				["Neptune", 0.0086, 29.56, 30.0611]]

	eccentricity_earth = 0.0167
	obliquity_earth = 23.45
	orbit_period_earth = 365.25

	# Quickstart
	earth_eot = muller_eot.EOT(eccentricity=eccentricity_earth, obliquity=obliquity_earth, orbit_period=orbit_period_earth)
	earth_eot.plotEOT(save_plot_name="examples/earth_quickstart.png")

	# Eccentricity and Obliquity
	earth_eot = muller_eot.EOT(eccentricity=eccentricity_earth, obliquity=obliquity_earth, orbit_period=orbit_period_earth)
	title = f"Earth: Effect of Eccentricity ({eccentricity_earth}) and Obliquity ({obliquity_earth}) (Min={min(earth_eot.eotDayAndMinutes.values()):.4f}, Max={max(earth_eot.eotDayAndMinutes.values()):.4f})"
	# Only Eccentricity, no Obliquity
	earth_eot.plotEOT(plot_title=title,
					save_plot_name="examples/earth_eot.png")

	earth_eot = muller_eot.EOT(eccentricity=eccentricity_earth, obliquity=0, orbit_period=orbit_period_earth)
	title = f"Earth: Effect of Eccentricity ({eccentricity_earth}) (Min={min(earth_eot.eotDayAndMinutes.values()):.4f}, Max={max(earth_eot.eotDayAndMinutes.values()):.4f})"
	earth_eot.plotEOT(plot_title=title,
					save_plot_name="examples/earth_eccentricity.png")
	
	# Only Obliquity, no Eccentricity
	earth_eot = muller_eot.EOT(eccentricity=0, obliquity=obliquity_earth, orbit_period=orbit_period_earth)
	title = f"Earth: Effect of Obliquity ({obliquity_earth}) (Min={min(earth_eot.eotDayAndMinutes.values()):.4f}, Max={max(earth_eot.eotDayAndMinutes.values()):.4f})"
	earth_eot.plotEOT(plot_title=title,
					save_plot_name="examples/earth_obliquity.png")
