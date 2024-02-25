"""
Run using mlflow.run instead of cli commands
"""

#!/usr/bin/env python
import argparse
import logging
import pathlib
import wandb
import requests
import tempfile
import mlflow

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    # Derive the base name of the file from the URL
    basename = pathlib.Path(args.file_url).name.split("?")[0].split("#")[0]

    # Download file, streaming so we can download files larger than
    # the available memory. We use a named temporary file that gets
    # destroyed at the end of the context, so we don't leave anything
    # behind and the file gets removed even in case of errors
    logger.info(f"Downloading {args.file_url} ...")
    with tempfile.NamedTemporaryFile(mode="wb+") as fp:

        logger.info("Creating run exercise_2")
        with wandb.init(project="exercise_2", job_type="download_data") as run:
            # Download the file streaming and write to open temp file
            with requests.get(args.file_url, stream=True) as r:
                for chunk in r.iter_content(chunk_size=8192):
                    fp.write(chunk)

            # Make sure the file has been written to disk before uploading
            # to W&B
            fp.flush()

            logger.info("Creating artifact")
            artifact = wandb.Artifact(
                name=args.artifact_name,
                type=args.artifact_type,
                description=args.artifact_description,
                metadata={"original_url": args.file_url},
            )
            artifact.add_file(fp.name, name=basename)

            logger.info("Logging artifact")
            run.log_artifact(artifact)

            artifact.wait()


if __name__ == "__main__":

    mlflow.run(
        # URI can be a local path or the URL to a git repository
        # here we are going to use a local path
        uri="./",
        entry_point="main",
        parameters={
            "file_url": "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv",
            "artifact_name": "iris",
            "artifact_description": "iris dataset csv",
        },
    )
