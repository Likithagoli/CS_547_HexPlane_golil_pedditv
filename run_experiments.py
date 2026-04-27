script = """#!/usr/bin/env python3
# run_experiments.py
# CS 547 - HexPlane Experiments Automation Script
# Authors: Goli Likitha Reddy, Varsha Reddy Pedditi

import subprocess

experiments = [
    # Experiment 1 - Original Results
    {"name": "dnerf_slim_lego", "datadir": "./data/dnerf/lego", "time_init": 6, "time_final": 12},
    {"name": "dnerf_slim_standup", "datadir": "./data/dnerf/standup", "time_init": 18, "time_final": 36},
    {"name": "dnerf_slim_bouncingballs", "datadir": "./data/dnerf/bouncingballs", "time_init": 18, "time_final": 36},
    # Experiment 2 - Modified Temporal Resolution
    {"name": "dnerf_slim_lego_lowtime", "datadir": "./data/dnerf/lego", "time_init": 3, "time_final": 6},
    {"name": "dnerf_slim_bouncingballs_hightime", "datadir": "./data/dnerf/bouncingballs", "time_init": 24, "time_final": 48},
]

for exp in experiments:
    print(f"Running experiment: {exp['name']}")
    cmd = [
        "python", "main.py",
        "config=config/dnerf_slim.yaml",
        f"data.datadir={exp['datadir']}",
        f"model.time_grid_init={exp['time_init']}",
        f"model.time_grid_final={exp['time_final']}",
        f"expname={exp['name']}"
    ]
    subprocess.run(cmd)
    print(f"Finished: {exp['name']}")

print("All experiments complete!")
"""

with open("/content/CS_547_HexPlane_golil_pedditv/run_experiments.py", "w") as f:
    f.write(script)
print("Created!")
