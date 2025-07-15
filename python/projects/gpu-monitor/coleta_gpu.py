import subprocess
import sys


def get_gpu_info():
    """
    Get GPU information using nvidia-smi command.
    Returns:
        str: GPU information as a string.
    """
    command = [
        "nvidia-smi",
        "--query-gpu=timestamp,name,temperature.gpu,utilization.gpu,memory.used,memory.total,power.draw",
        "--format=csv,noheader"
    ]

    try:
        result = subprocess.run(
            command, 
            capture_output=True,
            text=True,
            check=True
        )
        
        gpu_info = result.stdout.strip()
        print("GPU Information:")
        print(gpu_info)
    
    except FileNotFoundError:
        print("nvidia-smi command not found. Please ensure NVIDIA drivers are installed and in system PATH.")
        sys.exit(1)

    except subprocess.CalledProcessError as e:
        print(f"Error executing nvidia-smi: {e}")
        sys.exit(1)    

if __name__ == "__main__":
        get_gpu_info()