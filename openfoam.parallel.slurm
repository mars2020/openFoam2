#!/bin/bash
#----------------------------------------------------
# Sample Slurm job script
#   for TACC Stampede2 KNL nodes
#
#   *** MPI Job on Normal Queue ***
# 
# Last revised: 20 Oct 2017
#
# Notes:
#
#   -- Launch this script by executing
#      "sbatch knl.mpi.slurm" on Stampede2 login node.
#
#   -- Use ibrun to launch MPI codes on TACC systems.
#      Do not use mpirun or mpiexec.
#
#   -- Max recommended MPI tasks per KNL node: 64-68
#      (start small, increase gradually).
#
#   -- If you're running out of memory, try running
#      fewer tasks per node to give each task more memory.
#
#----------------------------------------------------

#SBATCH -J of           # Job name
#SBATCH -o of.o%j       # Name of stdout output file
#SBATCH -e of.e%j       # Name of stderr error file
#SBATCH -p normal          # Queue (partition) name
#SBATCH -N 1               # Total # of nodes
#SBATCH -n 2               # Total # of mpi tasks
#SBATCH -t 00:10:00        # Run time (hh:mm:ss)
###  #SBATCH --mail-user=youremail@utexas.edu
###  #SBATCH --mail-type=all    # Send email at begin and end of job
#SBATCH -A COE-347-SP2019       # Allocation name (req'd if you have more than 1)

# Other commands must follow all #SBATCH directives...

module purge
module load intel/18.0.2  impi/18.0.2 openfoam/6.0
module list

pwd
date

# Launch MPI code... 

blockMesh # create the mesh
checkMesh # check the mesh
decomposePar # decompose the domain
ibrun icoFoam -parallel # run the solver 
reconstructPar # reconstruct the solution

# ---------------------------------------------------
