import os
import os.path

pydir = []

for current_dir, dirs, files in os.walk("main"):

    for i in files:
        if ".py" in i:
            pydir.append(current_dir)
            break

with open("main_answer.txt", "w") as ma:
    ma.write("\n".join(sorted(pydir)))
