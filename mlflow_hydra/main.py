import mlflow
import os
import wandb
import hydra
from omegaconf import DictConfig


# This automatically reads in the configuration
@hydra.main(config_name="config")
def go(config: DictConfig):

    # In order to group runs in the same project and same experiment
    os.environ["WANDB_PROJECT"] = config["main"]["project_name"]
    os.environ["WANDB_RUN_GROUP"] = config["main"]["experiment_name"]

    # You can get the path at the root of the MLflow project with this:
    root_path = hydra.utils.get_original_cwd()

    _ = mlflow.run(
        uri=os.path.join(root_path, "download_data"),
        entry_point="main",
        parameters={
            "file_url": config["data"]["file_url"],
            "artifact_name": "iris.csv",
            "artifact_type": "raw_data",
            "artifact_description": "Input data",
        },
    )

    _ = mlflow.run(
        uri=os.path.join(root_path, "process_data"),
        entry_point="main",
        parameters={
            "input_artifact": "iris.csv:latest",
            "artifact_name": "clean_data.csv",
            "artifact_type": "processed_data",
            "artifact_description": "Cleaned data",
        },
    )


if __name__ == "__main__":
    go()
