import os
import subprocess

def run_bash_command_on_folders(main_folder, output_folder):
    # List all subfolders inside the main folder
    subfolders = [folder for folder in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, folder))]

    for subfolder in subfolders:
        # Construct the full path to the subfolder
        subfolder_path = os.path.join(main_folder, subfolder)

        # Construct the bash command to run on the subfolder
        bash_command = f'/Applications/MRIcroGL.app/Contents/Resources/dcm2niix -f "%f" -p y -z y -o "{output_folder}" "{subfolder_path}"'

        try:
            # Execute the bash command using subprocess
            subprocess.run(bash_command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command for folder '{subfolder_path}': {e}")

if __name__ == "__main__":
    # Replace these paths with your actual input and output folder paths
    input_folder = "/Users/sasha/Desktop/DS/Thesis/data.nosync/CN_FOR_BAE_DATA/output_2"
    output_folder = "/Users/sasha/Desktop/DS/Thesis/data.nosync/CN_FOR_BAE_DATA/output_ImageID"

    run_bash_command_on_folders(input_folder, output_folder)

