# Muller-EOT
![PyPi](https://img.shields.io/pypi/v/muller-eot)
![license](https://img.shields.io/github/license/cyschneck/Muller-EOT)

A Python package for [M. Müller implementation of the "Equation of Time - Problem in Astronomy"](http://info.ifpan.edu.pl/firststep/aw-works/fsII/mul/mueller.pdf) to calculate EOT and the effect of eccentricity/obliquity

The combined effect of eccentricity and obliquity create the Equation of Time components. This package uses Müller implementation to allow for the components to be graphed seperately as well as the final EOT

| Effect of Eccentricity | Effect of Obliquity |
| ------------- | ------------- |
| ![effect_eccentricity](https://raw.githubusercontent.com/cyschneck/Muller-EOT/main/examples/earth_eccentricity_testing.png) | ![effect_obliquity](https://raw.githubusercontent.com/cyschneck/Muller-EOT/main/examples/earth_obliquity_testing.png) |

![effect_eot](https://raw.githubusercontent.com/cyschneck/Muller-EOT/main/examples/earth_eot_testing.png)

## Overview

There are only four times of year where the length of the day is almost exactly 24 hours. 
The rest of the year when the sun is at its highest point (solar noon), a clock can run 
as much as 16 minutes ahead (12:16pm) or 13 minutes behind (11:47am). This discrepency is 
the result of combined effect of a planet's obliquity (axial tilt) and its eccentricity (as
well as other smaller gravitional forces like moons that are ignored here). Both of thsee 
features form two sine curves that oscillate throughout the year. The combined sum
of these two curves form the Equation of Time, a non-uniform change in time to fix to a clock.
A planet with an obliquity of 0° and perfectly circular orbit (zero eccentricity) would have
no difference in the Expected Solar Noon and the Actual Solar Noon.

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

The effect of obliquity and eccentricity are the caused as a result of Kepler's law:

"Two well-known features of our solar system are at the basis of the variations
 in the apparent motion of the sun: 1.) According to Kepler's second law, the angular
 velocity of the Earth relative to the sun varies throughout a year. 2) Equal angles
 which the sun in its apparent movement goes through in the eclipitic do not correspond
 to equal angles we measure on the equatorial plane. However, it is these latter angles
 which are relevant for the measure of time, since the daily movement of the sun is
 parallel to the equatorial plane" (Müller, 1995)
 
**Effect on Angular Velocity:**

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

## Documentation
## Dependencies
## Install
PyPi pip install at [pypi.org/project/muller-eot/](https://pypi.org/project/muller-eot/)

```
pip install muller-eot
```
## Examples
## Tests
## TODO:

calculateDistanceBetweenSolisticePerhelion() function

calculatePerihelionDay() function

calculateEccentricity() function
