## Command Line Procedures

0. Check the config_files/user_path_definitions.yml file and make sure EddyPro is installed

1. set exclusion policy if needed.  necessary *on vinimet* to activate the .venv.  This isn't necessary on my personal computer, it depends on how IT has things setup

Set-ExecutionPolicy Unrestricted -Scope Process

2. cd into the API directory, e.g.,

cd C:\Users\labuser\CANFLUX\EddyPro_API

3. activate the .virtual environment

.venv\Scripts\activate

4. Call the API

python eddyProAPI.py --siteID BB --biometUser True --eddyProStaticConfig Templates/ClosedPathStandard.eddypro --dateRange 2023-12-31 2025-01-02 --sourceDir Y:/BB/raw/2023 Y:/BB/raw/2024 --runMode 2


Set-ExecutionPolicy Unrestricted -Scope Process
cd C:\Users\labuser\CANFLUX\EddyPro_API
.venv\Scripts\activate
python eddyProAPI.py --siteID RBM --biometUser True --eddyProStaticConfig Templates/ClosedPathStandard.eddypro --dateRange 2024-01-01 2024-01-02 --sourceDir Y:/RBM/raw/2024 --runMode 2
deactivate





## Installing

1. install python, e.g, miniconda

https://www.anaconda.com/download/success

2. clone the git repo (WinMet Branch)

git clone -b WinMetWorking https://github.com/CANFLUX/EddyPro_API.git --recurse-submodules

3. run the install script (cd into EddyPro_API first)

python EddyPro_API\pyDbTools\setupPyVenv\install.py