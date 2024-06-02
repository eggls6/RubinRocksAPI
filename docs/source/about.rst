About Rubin Rocks API
======================
Rubin Rocks Application  
An :ref:`API` query returns dynamical information for near-Earth Objects with a specific set of orbital parameters.
The results closest to the orbial element set provided by the user are returned. 

Dynamical Model
----------------
#. Greenstreet et al. (2012) / NEOSSat1
This model contains the probability distribution of residence time held
by near-Earth object like test-particles in (a,e,i) cells of size (0.05 au,0.02, 2.0 degrees), respectively, 
orinnating in the five source regions, i.e. Intermediate Mars Crosser (IMC) population, Jupiter Family Comet (JFC) population, The 3:1 mean-motion resonance with Jupiter, Outer Main-Belt (OMB) population,
and the secular resonance nu6. Here, a is the semimajor axis, e the orbital eccentricity and i the inclination of a test particle.	
The N-body code SWIFT-RMVS4 was used to create the dynamical dataset. The default timestep was 6h,
which allowed high-speed encounters with Earth and Venus to be correctly resolved. 
A record of the orbital elements of all test particles was logged every 1000 years. 
The gravitational perturbations of Venus–Neptune were included. 
Mercury was not present in these integrations. 
Once a test particle reached the NEO region it was tracked until it either struck the Sun, 
struck a planet, travelled outside 19 au from the Sun, or the final integration time was reached. 
Test particles were monitored for 150 Myr in each asteroidal source region.
For details see Greenstreet at al. (2012).

API Output
------------
Estimated probabilities that a given near-Earth Object comes from a particular source region:
* IMC: Intermediate Mars Crosser (IMC) population,	
* JFC: Jupiter Family Comet (JFC) population,
* MMR3to1: The 3:1 mean-motion resonance with Jupiter,
* OMB: Outer Main-Belt (OMB) population,
* nu6: secular resonance nu6,
* residence_time: residence time probability distribution R_NEO (a,e,i),
* cumulative_residence_time: cumulative residence time.	



References
----------
`Greenstreet, S., Ngo, H. and Gladman, B., 2012. The orbital distribution of near-Earth objects inside Earth’s orbit. Icarus, 217(1), pp.355-366. <https://www.sciencedirect.com/science/article/pii/S0019103511004374>`_
