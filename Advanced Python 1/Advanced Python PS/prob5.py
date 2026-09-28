# 5. Store the multiplication tables generated in problem 3 in a file named
#    Tables.txt.

from pathlib import Path

out = Path(__file__).parent / "Tables.txt"

with open(out, "w") as f:
    for i in range(1, 11):
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}\n")
        f.write("\n")

print(f"Tables written to {out}")
