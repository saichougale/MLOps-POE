from pathlib import Path
import pandas as pd

from evidently import Dataset, DataDefinition, Report
from evidently.presets import DataSummaryPreset

def run_monitoring():
    data = pd.DataFrame({
        "response_time_ms": [100, 120, 110, 105, 115],
        "requests": [10, 12, 11, 15, 13],
        "status": ["success"] * 5
    })

    dataset = Dataset.from_pandas(
        data,
        data_definition=DataDefinition(
            numerical_columns=[
                "response_time_ms", "requests"
            ],
            categorical_columns=["status"]
        )
    )

    report = Report([DataSummaryPreset()])
    snapshot = report.run(dataset, None)

    Path("reports").mkdir(exist_ok=True)
    snapshot.save_html("reports/monitoring.html")

    print("Evidently report generated successfully!")

if __name__ == "__main__":
    run_monitoring()
