import os
import subprocess

def install_jupyter():
    try:
        subprocess.run(["jupyter", "lab", "--version"], check=True, stdout=subprocess.DEVNULL)
        print("Jupyter Lab đã được cài đặt.")
    except subprocess.CalledProcessError:
        print("Jupyter Lab chưa được cài đặt. Đang tiến hành cài đặt...")
        subprocess.run(["pip", "install", "jupyterlab"])

def start_jupyter():
    os.system("jupyter lab")

if __name__ == "__main__":
    install_jupyter()
    start_jupyter()
