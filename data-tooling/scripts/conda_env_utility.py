import subprocess
import sys
import os

# Define print functions for color output
def print_in_color(text):
    print(f"\033[1;36m{text}\033[0m")

def print_error(text):
    print(f"\033[1;31m{text}\033[0m")

def print_success(text):
    print(f"\033[1;32m{text}\033[0m")

# List all conda environments
def list_conda_envs():
    result = subprocess.run(['conda', 'env', 'list'], capture_output=True, text=True)
    envs = result.stdout.splitlines()
    for idx, env in enumerate(envs[2:], start=1):
        env_name = env.split()[0]
        print(f"{idx}: {env_name}")

# Main logic
def main():
    print_in_color("🎉 Welcome to the Conda Environment Utility! 🎉")

    print_in_color("\nAvailable Common Workflows:")
    print("1: Rename an environment")
    print("2: Export an environment to a YAML file")
    print("3: Delete an environment")
    print("4: Clone an environment")
    workflow = int(input("Select a workflow by entering the corresponding number: "))

    if workflow < 1 or workflow > 4:
        print_error("❌ Invalid selection. Exiting...")
        sys.exit(1)

    print_in_color("\nAvailable Conda Environments:")
    list_conda_envs()

    env_number = int(input("\nSelect the number corresponding to the environment you want to work with: "))

    # Get the environment name based on the selection
    result = subprocess.run(['conda', 'env', 'list'], capture_output=True, text=True)
    envs = result.stdout.splitlines()
    try:
        env_name = envs[env_number + 1].split()[0]
    except IndexError:
        print_error("❌ Invalid selection. Exiting...")
        sys.exit(1)

    if workflow == 1:
        print_in_color(f"\nYou selected: {env_name}")

        new_env_name = input("\nEnter the new name for the conda environment: ")

        if not new_env_name:
            print_error("❌ New environment name cannot be empty. Exiting...")
            sys.exit(1)

        # Activate the old environment
        print_in_color(f"\n🔄 Activating the old environment: {env_name}")
        subprocess.run(['conda', 'activate', env_name], shell=True)

        # Export the environment to a YAML file
        print_in_color("📤 Exporting the environment to environment.yml")
        subprocess.run(['conda', 'env', 'export', '--name', env_name, '--file', 'environment.yml'])

        # Deactivate the old environment
        print_in_color("🔄 Deactivating the old environment")
        subprocess.run(['conda', 'deactivate'], shell=True)

        # Create the new environment with the desired name
        print_in_color(f"🆕 Creating the new environment: {new_env_name}")
        subprocess.run(['conda', 'env', 'create', '--file', 'environment.yml', '--name', new_env_name])

        # Remove the old environment
        print_in_color(f"🗑️ Removing the old environment: {env_name}")
        subprocess.run(['conda', 'env', 'remove', '--name', env_name])

        # Activate the new environment
        print_in_color(f"🔄 Activating the new environment: {new_env_name}")
        subprocess.run(['conda', 'activate', new_env_name], shell=True)

        print_success(f"\n✅ Environment has been renamed from {env_name} to {new_env_name} and activated.")

    elif workflow == 2:
        yaml_file_name = input("\nEnter the name for the exported YAML file (without extension): ")

        if not yaml_file_name:
            print_error("❌ YAML file name cannot be empty. Exiting...")
            sys.exit(1)

        # Export the environment to a YAML file
        print_in_color(f"📤 Exporting the environment: {env_name} to {yaml_file_name}.yml")
        subprocess.run(['conda', 'env', 'export', '--name', env_name, '--file', f'{yaml_file_name}.yml'])

        print_success(f"\n✅ Environment has been exported to {yaml_file_name}.yml")

    elif workflow == 3:
        print_in_color(f"\n🗑️ Deleting the environment: {env_name}")
        subprocess.run(['conda', 'env', 'remove', '--name', env_name])

        print_success(f"\n✅ Environment {env_name} has been deleted.")

    elif workflow == 4:
        clone_env_name = input("\nEnter the name for the cloned environment: ")

        if not clone_env_name:
            print_error("❌ Cloned environment name cannot be empty. Exiting...")
            sys.exit(1)

        # Export the environment to a YAML file
        print_in_color("📤 Exporting the environment to environment.yml")
        subprocess.run(['conda', 'env', 'export', '--name', env_name, '--file', 'environment.yml'])

        # Create the new environment with the desired name
        print_in_color(f"🆕 Creating the cloned environment: {clone_env_name}")
        subprocess.run(['conda', 'env', 'create', '--file', 'environment.yml', '--name', clone_env_name])

        print_success(f"\n✅ Environment {env_name} has been cloned to {clone_env_name}")

if __name__ == "__main__":
    main()
