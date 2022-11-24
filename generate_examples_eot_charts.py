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
		if planet[0] == "Earth":
			orbital_period_planet = muller_eot.calculateOrbitalPeriod(planet[3])

			# Effect of Eccentricity
			eccentricity_y = muller_eot.calculateEffectEccentricity(planet[1], orbital_period_planet)
			muller_eot.plotEOT(planet[0], orbital_period_planet, eccentricity_y, "Eccentricity ({0})".format(planet[1]))

			# Effect of Obliquity
			obliquity_y = muller_eot.generateEffectObliquity(planet[2], orbital_period_planet)
			muller_eot.plotEOT(planet[0], orbital_period_planet, obliquity_y, "Obliquity ({0}°)".format(planet[2]))

			# Combined Effect of Obliquity and Eccentricity
			eot_combined_y = muller_eot.calculateDifferenceEOTMinutes(planet[1], planet[2], orbital_period_planet)
			muller_eot.plotEOT(planet[0], orbital_period_planet, eot_combined_y, "Eccentricity ({0}) and Obliquity ({1}°)".format(planet[1], planet[2]))
