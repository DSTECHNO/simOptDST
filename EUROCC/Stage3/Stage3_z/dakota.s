#!/bin/bash 
#SBATCH -p hamsi
#SBATCH -A eurocc7
#SBATCH -J SlotOpt_z_axis
#SBATCH -N 2
#SBATCH --ntasks-per-node=56
#SBATCH --time=03-00:00:0
#SBATCH --workdir=/truba/home/mkuzay/CfdSim/SlotOpt/model_3_1_z
#SBATCH --output=/truba/home/mkuzay/CfdSim/SlotOpt/model_3_1_z/slurm-%j.out
#SBATCH --error=/truba/home/mkuzay/CfdSim/SlotOpt/model_3_1_z/slurm-%j.err
#SBATCH --mail-user=
#SBATCH --mail-type=ALL

source $HOME/OpenFOAM/OpenFOAM-4.1/etc/bashrc WM_LABEL_SIZE=64 WM_COMPILER_TYPE=ThirdParty FOAMY_HEX_MESH=yes

proc=112
a=$(ls casebase/ | grep system)
for i in $a
do
cd casebase/$i
sed -i "/^numberOfSubdomains/{s/ [^ ]*/ $proc;/1}" decomposeParDict
cd ../..
done
sed -i "/^.\/\Allrun/{s/ [^ ]*/ $proc/1}" simulator_script

if [ -f "*Procs!" ]; then
    mv *Procs! ${proc}Procs!
else 
    touch ${proc}Procs!
fi

dakota.sh -i dakota_of.in -o run.out > stdout.out | tail -f stdout.out
#dakota -i dakota_of.in -r dakota.rst -s 21 -w dakota.rst -o run.out > stdout_2.out | tail -f stdout_2.out
