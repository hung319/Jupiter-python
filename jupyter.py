import os
import subprocess

def install_jupyter():
    try:
        # Kiểm tra nếu JupyterLab đã được cài đặt
        subprocess.check_call([os.sys.executable, '-m', 'jupyter', '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("Jupyter Lab đã được cài đặt trước đó.")
    except subprocess.CalledProcessError:
        print("Jupyter Lab chưa được cài đặt. Đang tiến hành cài đặt...")
        try:
            subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
            print("Jupyter Lab đã được cài đặt thành công.")
        except subprocess.CalledProcessError as e:
            print(f"Có lỗi xảy ra trong quá trình cài đặt Jupyter Lab: {e}")

def run_jupyter():
    try:
        # Chạy Jupyter Lab
        subprocess.run([
            os.sys.executable, '-m', "jupyter", "lab", 
            "--ip=0.0.0.0", "--port=8888", "--no-browser", 
            "--allow-root", "--NotebookApp.token='11042006'"
        ])
    except KeyboardInterrupt:
        print("Jupyter Lab đã dừng.")

if __name__ == "__main__":
    install_jupyter()
    run_jupyter()
