Run this script with:

mlflow run mlflow_exercise -P file_url=https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv -P artifact_name=iris -P artifact_description="iris dataset csv"

If you get errors try to run:
conda update -n base -c defaults conda

Or you can use mlflow.run() and so only lunch:
python download_data_2.py
