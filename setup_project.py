import os
import subprocess
import sys
import requests

# ==========================
# Configuration and Constants
# ==========================

PROJECT_STRUCTURE = {
    'src': [
        '__init__.py',
        'cli.py',
        'csv_utils.py',
        'transformations.py',
        'bigquery_data.py',
    ],
    'src/utils': [
        '__init__.py',
        'data_processing.py',
        'file_management.py',
        'interactive_shell.py',
        'logging_utils.py',
    ],
    'src/data_management': [
        '__init__.py',
        'data_cleaning.py',
        'data_validation.py',
        'data_loading.py',
    ],
    'src/etl': [
        '__init__.py',
        'extract.py',
        'transform.py',
        'load.py',
    ],
    'data': [],
    'data/raw': [],
    'data/processed': [],
    'data/samples': [],
    'data/templates': [],
    'config': [],
    'scripts': [],
    'tests': [
        '__init__.py',
        'test_csv_utils.py',
        'test_transformations.py',
        'test_bigquery_data.py',
        'test_data_processing.py',
        'test_etl.py',
    ],
    'docs': [],
    'notebooks': [],
}

GITIGNORE_URL = 'https://raw.githubusercontent.com/iTrauco/data-dirtying-tool/targeted-col-dirty-transformation/.gitignore'

REQUIREMENTS = [
    'blessed==1.20.0',
    'cachetools==5.4.0',
    'certifi==2024.7.4',
    'charset-normalizer==3.3.2',
    'colorama==0.4.6',
    'db-dtypes==1.3.0',
    'editor==1.6.6',
    'git-filter-repo==2.45.0',
    'google-api-core==2.19.1',
    'google-api-python-client==2.140.0',
    'google-auth==2.33.0',
    'google-auth-httplib2==0.2.0',
    'google-auth-oauthlib==1.2.1',
    'google-cloud-bigquery==3.25.0',
    'google-cloud-core==2.4.1',
    'google-cloud-resource-manager==1.12.5',
    'google-cloud-storage==2.18.2',
    'google-crc32c==1.5.0',
    'google-resumable-media==2.7.2',
    'googleapis-common-protos==1.63.2',
    'grpc-google-iam-v1==0.13.1',
    'grpcio==1.65.4',
    'grpcio-status==1.65.4',
    'httplib2==0.22.0',
    'idna==3.7',
    'inquirer==3.4.0',
    'joblib==1.4.2',
    'numpy==2.0.1',
    'oauthlib==3.2.2',
    'packaging==24.1',
    'pandas==2.2.2',
    'pandas-gbq==0.23.1',
    'proto-plus==1.24.0',
    'protobuf==5.27.3',
    'pyarrow==17.0.0',
    'pyasn1==0.6.0',
    'pyasn1_modules==0.4.0',
    'pydata-google-auth==1.8.2',
    'pyfiglet==1.0.2',
    'pyparsing==3.1.2',
    'python-dateutil==2.9.0.post0',
    'pytz==2024.1',
    'readchar==4.2.0',
    'requests==2.32.3',
    'requests-oauthlib==2.0.0',
    'rsa==4.9',
    'runs==1.2.2',
    'scikit-learn==1.5.1',
    'scipy==1.14.0',
    'setuptools==72.2.0',
    'six==1.16.0',
    'threadpoolctl==3.5.0',
    'tzdata==2024.1',
    'uritemplate==4.1.1',
    'urllib3==2.2.2',
    'wcwidth==0.2.13',
    'xmod==1.8.1',
]

# ==========================
# Utility Functions
# ==========================

def create_project_structure(base_dir):
    """
    Creates the directory structure for the project.
    
    Args:
    base_dir (str): The base directory where the project will be created.
    """
    for folder, files in PROJECT_STRUCTURE.items():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, 'w') as f:
                pass  # Create an empty file
        print(f"Created directory and files in: {folder_path}")

def download_gitignore(base_dir):
    """
    Downloads the .gitignore file from the specified URL and saves it to the base directory.
    
    Args:
    base_dir (str): The base directory where the .gitignore will be saved.
    """
    response = requests.get(GITIGNORE_URL)
    gitignore_path = os.path.join(base_dir, '.gitignore')
    with open(gitignore_path, 'w') as f:
        f.write(response.text)
    print(".gitignore file downloaded.")

def install_requirements():
    """
    Installs the required Python packages for the project using pip.
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + REQUIREMENTS)

def initialize_git_repo(base_dir):
    """
    Initializes a git repository in the base directory.
    
    Args:
    base_dir (str): The base directory where the git repository will be initialized.
    """
    subprocess.check_call(['git', 'init'], cwd=base_dir)
    subprocess.check_call(['git', 'add', '.'], cwd=base_dir)
    subprocess.check_call(['git', 'commit', '-m', 'Initial project setup'], cwd=base_dir)
    print("Git repository initialized and initial commit made.")

# ==========================
# Main Program Execution
# ==========================

def main():
    """
    Main function to set up the project structure and environment.
    """
    if len(sys.argv) != 2:
        print("Usage: python setup_project.py <directory>")
        sys.exit(1)

    base_dir = sys.argv[1]
    os.makedirs(base_dir, exist_ok=True)

    create_project_structure(base_dir)
    download_gitignore(base_dir)
    install_requirements()
    initialize_git_repo(base_dir)

    print(f"Project setup completed in {base_dir}")

if __name__ == "__main__":
    main()

