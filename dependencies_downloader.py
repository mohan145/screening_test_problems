import subprocess
import json
import sys


def install_package(package, installation_failed_packages):
    try:
        status_code = subprocess.check_call(['pip', "install", package])
    except subprocess.CalledProcessError:
        installation_failed_packages.append(package)


# usage dependecies_downloader.py file_name.json
def main():
    file_name = sys.argv[1]
    file = open(file_name)
    dependencies = json.loads(file.read())

    dependencies = dependencies["Dependencies"]
    installation_failed_packages = []
    status_code = subprocess.check_call(["python", "-m", "pip", "install", "--upgrade", "pip"])

    for dependency in dependencies:
        install_package(dependency, installation_failed_packages)

    print(installation_failed_packages)


if __name__ == '__main__':
    main()

