#!/bin/bash
#SBATCH --partition=maxcpu
#SBATCH --time=96:00:00
#SBATCH --nodes=1
#SBatch --mem=250GB
unset LD_PRELOAD
source /etc/profile.d/modules.sh
module purge

# use 'sbatch --export=NODENUM='X' sbatch_script.sh' for node X.
/home/username/ba_resource_estimates/jobs/node_$NODENUM.sh