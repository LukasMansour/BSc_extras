#!/bin/bash

# Replace with '47' correct number of generated jobs.
# Replace the sbatch script with the correct script you want to run.
for NODENUM in {0..47}; do
  sbatch --export=NODENUM="$NODENUM" sbatch_script_ra.sh
done