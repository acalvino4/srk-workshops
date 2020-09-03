# conda documentation - https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

# create conda env
conda create -n env-name python=3.8 notebook pylint

# activate enviornment
conda activate env-name

# add package to environment
conda install -n env-name my-package
