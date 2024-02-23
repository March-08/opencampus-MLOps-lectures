Create env:

conda env create -n download_data --file conda.yml

Run:
mflow run .

Change hydra hyyperparameters:
mflow run . -P hydra_options="main.experiment_name=prod"
