"""run_all.py - menjalankan 4 program milik Anggota 2."""
import os
import subprocess
import sys

base = os.path.dirname(os.path.abspath(__file__))
for k in (2,):
    for prog in ("raw", "war", "waw", "semua"):
        path = os.path.join(base, f"anggota{k}", f"{prog}.py")
        print(f"\n######## anggota{k}/{prog}.py ########")
        subprocess.run([sys.executable, path], check=True)
