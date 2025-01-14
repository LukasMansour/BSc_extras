from pathlib import Path

username = ""

path = f"/home/{username}/ba_resource_estimates"

choice_metrics = ["gate_count", "gate_depth", "cz_count", "cz_depth"]
n_list = list(range(3, 11))
seed = 0
widths = ["low", "medium", "high"]

jobs = []
for choice in choice_metrics:
    for n in n_list:
        for width in widths:
            # Mamba still stored the python environments here.
            jobs.append((n, f"/home/{username}/.conda/envs/qc/bin/python3 {path}/dlp_ba/resource_estimation/resource_estimation_dlp.py {n} {choice} {seed} {width} /home/{username}/ba_resource_estimates/results_dlp/{width}_width/"))
current_node = 0

# 2 jobs per node (we know the number of jobs is even):
while len(jobs) > 0:
    job_file_path = Path(f"{path}/jobs/node_{current_node}.sh")
    job_file_path.parent.mkdir(parents=True, exist_ok=True)
    mode = 'a'
    if not job_file_path.exists():
        mode = 'w'
    f = open(job_file_path, mode)
    f.write(f"cd {path}/dlp_ba/resource_estimation\n")
    # 2 jobs per node (we know the number of jobs is even):
    job_0 = jobs.pop(0) # from front
    job_1 = jobs.pop(-1) # from back
    if job_0[0] <= job_1[0]:
        f.write(job_0[1])
        f.write("\n")
        f.write(job_1[1])
        f.write("\n")
    else:
        f.write(job_1[1])
        f.write("\n")
        f.write(job_0[1])
        f.write("\n")
    f.close()
    current_node += 1