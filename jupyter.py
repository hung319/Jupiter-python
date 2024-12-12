import os
import sys
import subprocess

def check_and_install_jupyterlab():
    try:
        # Kiểm tra nếu JupyterLab đã được cài đặt
        import jupyterlab
        print("JupyterLab is already installed.")
    except ImportError:
        print("JupyterLab is not installed. Installing now...")
        # Cài đặt JupyterLab
        subprocess.check_call([sys.executable, "-m", "pip", "install", "jupyterlab"])
        print("JupyterLab installed successfully.")

def start_jupyterlab():
    try:
        print("Starting JupyterLab...")
        subprocess.run([sys.executable, "-m", "jupyter", "lab", "--ip=0.0.0.0", "--port=80", "--no-browser"])
    except KeyboardInterrupt:
        print("\nStopping JupyterLab...")
        sys.exit(0)

if __name__ == "__main__":
    # Kiểm tra và cài đặt JupyterLab
    check_and_install_jupyterlab()
    # Khởi chạy JupyterLab
    start_jupyterlab()
