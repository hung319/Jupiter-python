import os
import subprocess

def install_jupyter():
    try:
        # Cài đặt Jupyter Lab
        subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', 'jupyterlab'])
        print("Jupyter Lab đã được cài đặt thành công.")
    except subprocess.CalledProcessError:
        print("Có lỗi xảy ra trong quá trình cài đặt Jupyter Lab.")

def run_jupyter():
    try:
        # Chạy Jupyter Lab
        subprocess.run([os.sys.executable, '-m', "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token='11042006'"])
    except KeyboardInterrupt:
        print("Jupyter Lab đã dừng.")

if __name__ == "__main__":
    install_jupyter()
    run_jupyter()
