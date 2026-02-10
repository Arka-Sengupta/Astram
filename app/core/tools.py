import os
import subprocess
import platform

class Tools:
    @staticmethod
    def read_file(path):
        try:
            with open(path, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {e}"

    @staticmethod
    def write_file(path, content):
        try:
            # Ensure directory exists (only if there's a directory component)
            dir_path = os.path.dirname(path)
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
            with open(path, 'w') as f:
                f.write(content)
            return f"Successfully wrote to {path}"
        except Exception as e:
            return f"Error writing file: {e}"

    @staticmethod
    def list_files(directory="."):
        try:
            return os.listdir(directory)
        except Exception as e:
            return f"Error listing files: {e}"

    @staticmethod
    def run_command(command):
        try:
            # Platform specific shell command execution
            system = platform.system()
            if system == "Windows":
                 result = subprocess.run(command, shell=True, capture_output=True, text=True)
            else:
                 result = subprocess.run(command, shell=True, capture_output=True, text=True, executable='/bin/bash')
            
            return f"Output:\n{result.stdout}\nErrors:\n{result.stderr}"
        except Exception as e:
            return f"Error running command: {e}"
