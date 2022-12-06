# Test generate_star_chart functions
# python3 generate_examples_eot_charts.py
import muller_eot

if __name__ == '__main__':
	# Planet Name, Eccentricity, Obliquity, Semimajor Axis (AU)
	planet_lst = [["Mercury", 0.2056, 0.1, 0.3871],
					["Venus", 0.0068, 87.3, 0.7233], 
					["Earth", 0.0167, 23.45, 1.0000001124],
					["Mars", 0.0934, 25.19, 1.5273],
					["Jupiter", 0.0484, 3.12, 5.2028],
					["Saturn", 0.0541, 26.73, 9.5388],
					["Uranus", 0.0472, 97.86, 19.1914],
					["Neptune", 0.0086, 29.56, 30.0611]]

	for planet in planet_lst:
		if True:#planet[0] == "Earth":
			orbital_period_planet = muller_eot.calculateOrbitalPeriod(planet[3])

			# Effect of Eccentricity
			eccentricity_dict = muller_eot.calculateDifferenceEOTMinutes(eccentricity=planet[1],
																	obliquity_deg=0,
																	orbit_period=orbital_period_planet)
			muller_eot.plotEOT(planet_name=planet[0], 
								eot_dict=eccentricity_dict,
								effect_title_str="Eccentricity ({0})".format(planet[1]), 
								save_plot_name="examples/{0}_eccentricity_testing".format(planet[0].lower()))

			# Effect of Obliquity
			obliquity_dict = muller_eot.calculateDifferenceEOTMinutes(eccentricity=0, 
																	obliquity_deg=planet[2], 
																	orbit_period=orbital_period_planet)
			muller_eot.plotEOT(planet_name=planet[0],
								eot_dict=obliquity_dict,
								effect_title_str="Obliquity ({0})".format(planet[2]),
								save_plot_name="examples/{0}_obliquity_testing".format(planet[0].lower()))

			# Combined Effect of Obliquity and Eccentricity
			eot_combined_dict = muller_eot.calculateDifferenceEOTMinutes(eccentricity=planet[1],
																	obliquity_deg=planet[2],
																	orbit_period=orbital_period_planet)
			muller_eot.plotEOT(planet_name=planet[0],
								eot_dict=eot_combined_dict,
								effect_title_str="Eccentricity ({0}) and Obliquity ({1})".format(planet[1], planet[2]),
								save_plot_name="examples/{0}_eot_testing".format(planet[0].lower()))
