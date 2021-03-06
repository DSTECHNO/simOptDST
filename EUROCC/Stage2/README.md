# Stage 2: Optimization of width and hitght of the slots separately.                                 
 
							GENERAL DESCRIPTIONS

1. 	In order to run the system, the Allrun.pre file in the casebase must be run first for the blockMesh process. 
	If there are no geometry and mesh changes, there is no need to rerun.

2. 	In this system prepared for two-variable optimization, coordinates are given in the portscoord.template file located in the templatedir folder.

3. 	The dakota_of.in file is used for the variables to be optimized. 
	The algorithm selected for optimization and the information related to the algorithm should be given in the dakota_of.in file. 
	For additional information, please visit the "https://dakota.sandia.gov/content/64-reference-manual" website.

4. 	Basic operations, Allrun file and EF.py file are called in the simulator_script file. 
	Analysis is done in OpenFOAM with the Allrun file. 
	In order to calculate the Morrill Index, the objective function value is determined with the help of the EF.py file in the casebase. 
	This objective function value (|2-Morrill Index|) is minimized by bringing it closer to 0. Thus, the efficiency of the system is optimized.

5. 	For the optimization process in Dakota, a new folder will be created for each new solution step by copying the casebase with the loop in the dakota.s file at every stage.

6. 	From the getPics.py file, images can be taken for each analysis on systems with Paraview installed.

7.	It is necessary to use dakota_cleanup file to delete all optimization results.



![Phase2](https://user-images.githubusercontent.com/90314532/133221259-5f75a5c5-db23-436b-8aae-aed7b756dcef.gif)


Design and Simulation Technologies Inc. (DSTECH)
    
http://dstechno.net/
