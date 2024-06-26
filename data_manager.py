from typing import Any, Tuple

from flops_utils.ml_repo_building_blocks import load_dataset
from flops_utils.ml_repo_templates import DataManagerTemplate


class DataManager(DataManagerTemplate):
    def __init__(self):
        (self.x_train, self.x_test), (self.y_train, self.y_test) = self._prepare_data()

    def _prepare_data(self, partition_id=1) -> Any:  # TODO adjust
        """Reference: https://github.com/adap/flower/blob/main/examples/sklearn-logreg-mnist/client.py"""
        dataset = load_dataset()
        dataset.set_format("numpy")

        x, y = dataset["image"].reshape((len(dataset), -1)), dataset["label"]
        # Split the on edge data: 80% train, 20% test
        train_split = int(0.8 * len(x))
        x_train, x_test = x[:train_split], x[train_split:]
        eval_split = int(0.8 * len(y))
        y_train, y_test = y[:eval_split], y[eval_split:]
        return (x_train, x_test), (y_train, y_test)

    def get_data(self) -> Tuple[Any, Any]:
        return (self.x_train, self.x_test), (self.y_train, self.y_test)
