import subprocess

def generate_objects_with_dd(base_file_path, num_objects, object_size):
    for i in range(num_objects):
        file_path = f"{base_file_path}_{i+1}.bin"
        dd_command = f"dd if=/dev/zero of={file_path} bs={object_size} count=1"
        subprocess.run(dd_command, shell=True)

base_file_path = 'object'  # Specify the base file path without the file extension
num_objects = 50
object_size = 10 * 1024 * 1024  # 10MB size in bytes

generate_objects_with_dd(base_file_path, num_objects, object_size)
