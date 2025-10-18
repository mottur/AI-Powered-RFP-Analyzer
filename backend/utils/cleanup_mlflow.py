"""
Utility function to clean up old MLflow runs in classifier training experiment.
Keeps only the most recent N runs and deletes the rest.
"""

import mlflow
from mlflow.tracking import MlflowClient
from core.shared import verbose


def cleanup_old_runs(experiment_name: str = "rfp_analyzer", keep_last_n: int = 10, dry_run: bool = True):
    """
    Cleans up old MLflow runs in the specified experiment.
    Keeps only the most recent `keep_last_n` runs, deletes the rest.
    """
    client = MlflowClient()
    experiment = client.get_experiment_by_name(experiment_name)
    if not experiment and verbose:
        print(f"Experiment '{experiment_name}' not found.")
        return

    experiment_id = experiment.experiment_id
    runs = client.search_runs(
        experiment_ids=[experiment_id],
        order_by=["start_time DESC"],  # Newest first
        max_results=1000  # Adjust if needed
    )

    if len(runs) <= keep_last_n and verbose:
        print(f"Nothing to delete — only {len(runs)} runs found.")
        return

    # Runs to delete: all except the most recent N
    old_runs = runs[keep_last_n:]

    if verbose:
        print(f"Found {len(old_runs)} old runs to delete.")
    for run in old_runs:
        run_id = run.info.run_id
        if verbose:
            print(f"{'Would delete' if dry_run else 'Deleting'} run {run_id}")
        if not dry_run:
            client.delete_run(run_id)