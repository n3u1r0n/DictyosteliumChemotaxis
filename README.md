# A particle simulation of Dictyostelium Chemotaxis

Here are all the files corresponding to this project.

The chemotaxis.py file is the main python file containing all the simulation code.

The tex.py file only contains some code for exporting nice latex snippets,
which can be copied into a latex document to display the simulation images.

The parameters.py file contains a list of parameter combinations which can be modified.

The simulation folder contains the animations for all the 8 simulations presented in the paper.

All other files are the latex source code and output.

Note that if you run the chemotaxis.py file as is,
the sub-folders of the simulation folder will be overwritten with the new simulations.

One could also modify the chemotaxis.py file by deleting the last line:
-- main()
and replace it with something like
-- simulation('output.gif', ...some parameters...)
and then run the file.
This will produce a gif as output for the simulation.

Note that with the parameters in the parameters.py file each simulation might take about 1-2 minutes
(most of the time being spend on the generation of the images and not the actual computations).