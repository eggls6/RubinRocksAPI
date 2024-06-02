About Rubin Rocks API
======================
Rubin Rocks Application  
An :ref:`API` query returns dynamical information for near-Earth Objects with a specific set of orbital parameters.
The results closest to the orbial element set provided by the user are returned. 

Dynamical Model
----------------
#. Greenstreet et al. 2012

The N-body code SWIFT-RMVS4 was used to create the near-Earth asteroid dynamical dataset. The default timestep was 6h,
which allowed high-speed encounters with Earth and Venus to be correctly resolved. 
A record of the orbital elements of all test particles was logged every 1000 years. 
The gravitational perturbations of Venus–Neptune were included. 
Mercury was not present in these integrations for the purpose of the recomputation. 
Once a test particle reached the NEO region it was tracked until it either struck the Sun, 
struck a planet, travelled outside 19 au from the Sun, or the final integration time was reached. 
Test particles were monitored for 150 Myr in each asteroidal source region.

References
----------
Greenstreet, S., Gladman, B., Ngo, H., Granvik, M. and Larson, S., 2012. Production of near-earth asteroids on retrograde orbits. The Astrophysical Journal Letters, 749(2), p.L39. `https://www.sciencedirect.com/science/article/pii/S0019103511004374`_
