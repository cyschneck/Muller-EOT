# Muller-EOT
![PyPi](https://img.shields.io/pypi/v/muller-eot)
![license](https://img.shields.io/github/license/cyschneck/Muller-EOT)
![PyPi-Versions](https://img.shields.io/pypi/pyversions/Muller-EOT)

A Python package for [M. Müller implementation of the "Equation of Time - Problem in Astronomy"](http://info.ifpan.edu.pl/firststep/aw-works/fsII/mul/mueller.pdf) to calculate the Equation of Time based on the individual effect of eccentricity and obliquity

## Quickstart: muller-eot

Get a list of differences in time for each day of the Earth's orbit and then plot it as a function of days in orbit

```
import muller_eot

earth_eot = muller_eot.EOT(eccentricity=0.0167, obliquity=23.45, orbit_period=365.25)
earth_eot.plotEOT()
```
![effect_eot](https://raw.githubusercontent.com/cyschneck/Muller-EOT/main/examples/earth_quickstart.png)

## Install
PyPi pip install at [pypi.org/project/muller-eot/](https://pypi.org/project/muller-eot/)

```
pip install muller-eot
```

## Functions
The combined effect of eccentricity and obliquity create the Equation of Time components.

| Effect of Eccentricity | Effect of Obliquity |
| ------------- | ------------- |
| ![effect_eccentricity](https://raw.githubusercontent.com/cyschneck/Muller-EOT/main/examples/earth_eccentricity.png) | ![effect_obliquity](https://raw.githubusercontent.com/cyschneck/Muller-EOT/main/examples/earth_obliquity.png) |

Combined Effect of the Eccentricity and Obliquity = Equation of Time
![effect_eot](https://raw.githubusercontent.com/cyschneck/Muller-EOT/main/examples/earth_eot.png)

### EOT Object
All Equation of Time calculations are done as a part of the EOT class object. First, create an EOT object for a specific eccentricity, obliquity, and orbit period (in days)
```python
import muller_eot
muller_eot.EOT(eccentricity=None,
		obliquity=None,
		orbit_period=None)
```
- **[REQUIRED]** eccentricity (float/int): eccentricity of the planet's orbit
- **[REQUIRED]** obliquity (float/int): obliquity/axial tilt of the planet
- **[REQUIRED]** orbit_period (float/int): days in a solar year


### EOT Class Attributes and Functions

**eotDayAndMinutes**
Returns a dictionary for the difference in time for each day in a year {number_day: time difference}
```python
EOT.eotDayAndMinutes
```

**plotEOT**
Plot the differences in time for the EOT as well as the individual effect of obliquity and eccentricity
```python
EOT.plotEOT(plot_title=None,
		plot_x_title=None,
		plot_y_title=None,
		show_plot=True,
		fig_plot_color="cornflowerblue",
		figsize_n=12,
		figsize_dpi=100,
		save_plot_name=None)
```
- *[OPTIONAL]* plot_title (string): Title of plot, defaults to `EOT Minute Difference (Min = <negative minutes>, Max = <postive minutes>)`
- *[OPTIONAL]* plot_x_title (string): X-axis title, defaults to `Days in the Sidereal Year`
- *[OPTIONAL]* plot_y_title (string): Y-axis title, defaults to `Time Difference (Minutes)`
- *[OPTIONAL]* show_plot (boolean): Show plot (triggers plt.show()), useful when generating multiple plots at once in the background, defaults to True
- *[OPTIONAL]* fig_plot_color (string): Scatter plot color, defaults to `cornflowerblue` blue
- *[OPTIONAL]* figsize_n (int/float): Figure size nxn, defaults to 12x12
- *[OPTIONAL]* figsize_dpi (int/lfoat): Figure DPI, defaults to 100
- *[OPTIONAL]* save_plot_name (boolean): Save plot as output, defaults to None (does not save)

## Background

The length of a day on Earth is only close to being 24 hours four times a year. For the rest of the year when the sun is at its highest point (solar noon), a clock can run as much as 16 minutes ahead (12:16pm) or 13 minutes behind (11:47am). This discrepancy is the result of the combined effect of a planet's obliquity (axial tilt) and its eccentricity (as well as other smaller gravitational forces like moons that are ignored here). Both of these features form two sine curves that oscillate throughout the year. The combined sum
of these two curves form the Equation of Time, a non-uniform change in time to fix to a clock.
A planet with an obliquity of 0° and perfectly circular orbit (zero eccentricity) would have
no difference in the Expected Solar Noon and the Actual Solar Noon.

To calculate the difference in time for an individual day:
<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203877814-c2d710f3-0681-4f72-8607-0f96e2a33256.png" />
</p>

Equation of Time = (Apparent Solar Time) - (Mean Solar Time) 

**Effect of Eccentricity:**
<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203484492-bf0f6098-fe13-44d3-b372-bcb8cc4120f8.png" />
</p>

**Effect of Obliquity:**
<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203484389-613ffb3e-9719-4962-a316-eeeb887af1c5.png" />
</p>

"Equation of time is determined by the following parameters: the eccentricity of 
the orbit of the Earth, the angle between the ecliptic and the equatorial planes, the 
angle P between the winter solstice and the perihelion relative to the sun or: 
the time span ∆t from the beginning of winter to the passage through periehlion" (Müller, 1995)

<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203484797-23c81e99-0eee-4431-bc21-31429a615e4f.png" />
</p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203484692-b07bad99-3c6c-43e5-904f-04200f72c571.png" />
</p>

The effect of eccentricity is the result of Kepler's Law where:

"Two well-known features of our solar system are at the basis of the variations
 in the apparent motion of the sun: 1.) According to Kepler's second law, the angular
 velocity of the Earth relative to the sun varies throughout a year. 2) Equal angles
 which the sun in its apparent movement goes through in the eclipitic do not correspond
 to equal angles we measure on the equatorial plane. However, it is these latter angles
 which are relevant for the measure of time, since the daily movement of the sun is
 parallel to the equatorial plane" (Müller, 1995)
 
**Effect on Angular Velocity (on Eccentricity):**

As a result of Kepler's law, planets moving in an ellipitc orbit will have variable angular velocity 
as a result of the second law where the area swept during a constant period of time is constant (=dA/dt)

<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203687968-4055d194-afe0-49e8-8b73-94f1b58a3969.png" />
</p>

"1.) parameter: the eccentricity. If e = 0 a regular variation results that is caused by
the inclination of the ecliptic plane. The deviations of the apparent solar time from the
mean solar time increase with growing e in winter and autumn. Thus, the yearly variation
becomes dominant. Since at the perihelion and aphelion the equation of time is only a
function of the ecliptic inclination and the angle P, all plots have the same value at these
two points.
2.) parameter: the inclination of the ecliptic. ε = 0 yields a plot which is symmetric to
the passage through the aphelion. The greater ε the more dominant the variation with a
period of half a year. All plots have four common points at the beginning of each season,
for the equation of time depends only on the two other parameters there (eccentricity
and P). As the projection from the ecliptic plane onto the equatorial plane does not
change the polar angle relative to the winter solstice, ε does not influence the value of the
equation of time at the beginning of a season.
3.) parameter: the time interval between the beginning of winter and the passage
through the perihelion. If ∆t = 0 the two main variations vanish both at the beginning
of winter and summer (because winter begins when the earth passes the perihelion; the
aphelion is the summer solstice). Therefore, the resulting function is symmetric and the
extreme values are in autumn and winter. If ∆t increases, the two components tend to
compensate each other in winter whereas the negative value in summer begins to dominate." (Müller, 1995)

Equation of Time is the combination of the effect of eccentricity and obliquity
<p align="center">
  <img src="https://user-images.githubusercontent.com/22159116/203484851-c96be35a-2d4a-44df-a2ee-a9d88974aa9e.png" />
</p>

### TODO:
- Pytests
- calculateOrbitalPeriod(semimajor_axis)
- calculateDistanceBetweenSolisticePerhelion()
- calculatePerihelionDay()
- calculateWinterSolsticeDay()
- calculateEccentricity()

## Development Environment

To run or test against `muller_eot` github repo/fork, a development environment can be created via conda/miniconda

First, [install Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html)

Then, using the existing `environment.yml`, a new conda environment can be create to run/test scripts against

```
conda env create --file environment.yml
```
Once the environment has been built, activate the environment:
```
conda activate muller_eot
```
