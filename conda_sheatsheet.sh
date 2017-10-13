# CLONE CONDA ENVIRONMENT
# https://stackoverflow.com/questions/24664072/how-do-i-clone-a-conda-environment-from-one-python-release-to-another
conda create -n clonedenv --clone oldenv
conda install -n clonedenv python=3.4
conda update -n clonedenv --all

# https://stackoverflow.com/questions/40089212/anaconda-python-3-5-install-pyqt4
conda install --channel https://conda.anaconda.org/conda-forge pyqt