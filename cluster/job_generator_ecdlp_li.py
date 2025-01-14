from pathlib import Path

username = ""

path = f"/home/{username}/ba_resource_estimates"

n_list = list(range(3, 9))
seed = 0

jobs = []
for n in n_list:
    # Mamba still stored the python environments here.
    jobs.append((n, f"/home/{username}/.conda/envs/qc/bin/python3 {path}/dlp_ba/resource_estimation/largest_instance/largest_instance_ecdlp.py {n} {seed} /home/{username}/ba_resource_estimates/results_ecdlp/largest_instance/"))
current_node = 0

# 2 jobs per node (we know the number of jobs is even):
while len(jobs) > 0:
    job_file_path = Path(f"{path}/jobs/node_{current_node}.sh")
    job_file_path.parent.mkdir(parents=True, exist_ok=True)
    mode = 'a'
    if not job_file_path.exists():
        mode = 'w'
    f = open(job_file_path, mode)
    f.write(f"cd {path}/dlp_ba/resource_estimation/largest_instance\n")
    # 2 jobs per node (we know the number of jobs is even):
    job_0 = jobs.pop(0) # from front
    f.write(job_0[1])
    f.write("\n")
    f.close()
    current_node += 1