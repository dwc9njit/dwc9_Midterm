"""
This module manages the history of calculations.
"""

import os
import logging
import pandas as pd
from decimal import Decimal
from .operation_functions import add, subtract, multiply, divide, exponent
from .calculation import Calculation

class Calculations:
    """
    Class to manage the history of calculations.

    Attributes:
        history_dir (str): Directory to store history files.
        history_file (str): Path to the history file.
        history (pd.DataFrame): DataFrame to store calculation history.
        logger (logging.Logger): Logger for this class.
    """
    history_dir = "data"
    history_file = os.path.join(history_dir, "calculation_history.csv")
    history = pd.DataFrame(columns=["Operation", "Operand_A", "Operand_B", "Result"])
    logger = logging.getLogger(__name__)

    @staticmethod
    def create_empty_history():
        """
        Create an empty history DataFrame with the correct columns.

        Returns:
            pd.DataFrame: Empty history DataFrame.
        """
        return pd.DataFrame(columns=["Operation", "Operand_A", "Operand_B", "Result"])

    @staticmethod
    def load_history():
        """
        Load calculation history from a CSV file.
        """
        Calculations.logger.info("Attempting to load history from %s", Calculations.history_file)
        if os.path.exists(Calculations.history_file) and os.path.getsize(Calculations.history_file) > 0:
            Calculations.history = pd.read_csv(Calculations.history_file)
            Calculations.logger.info("Loaded history from %s:\n%s", Calculations.history_file, Calculations.history)
        else:
            Calculations.logger.warning("No existing history found or file is empty. Creating new history.")
            Calculations.history = Calculations.create_empty_history()

    @staticmethod
    def save_history():
        """
        Save calculation history to a CSV file.
        """
        os.makedirs(Calculations.history_dir, exist_ok=True)
        Calculations.logger.info("Saving history to %s", Calculations.history_file)
        Calculations.history.to_csv(Calculations.history_file, index=False)
        Calculations.logger.info("Saved history to %s:\n%s", Calculations.history_file, Calculations.history)

    @staticmethod
    def add_calculation(calculation: Calculation):
        """
        Add a calculation to the history.

        Args:
            calculation (Calculation): The calculation to add.
        """
        Calculations.logger.info("Adding calculation: %s", calculation)
        result = calculation.perform_operation()
        new_entry = {
            'Operation': calculation.operation.__name__,
            'Operand_A': float(calculation.a),
            'Operand_B': float(calculation.b),
            'Result': float(result)
        }
        Calculations.load_history()
        new_entry_df = pd.DataFrame([new_entry])
        if Calculations.history.empty:
            Calculations.history = new_entry_df
        else:
            Calculations.history = pd.concat([Calculations.history, new_entry_df], ignore_index=True)
        Calculations.save_history()

    @staticmethod
    def clear_history():
        """
        Clear the calculation history.
        """
        Calculations.logger.info("Clearing history.")
        Calculations.history = Calculations.create_empty_history()
        Calculations.save_history()

    @staticmethod
    def delete_history():
        """
        Delete the history file.
        """
        try:
            os.remove(Calculations.history_file)
            Calculations.logger.info("Deleted history file: %s", Calculations.history_file)
        except FileNotFoundError:
            Calculations.logger.warning("No history file found to delete.")

    @staticmethod
    def view_history():
        """
        Return the calculation history.

        Returns:
            pd.DataFrame: The calculation history.
        """
        Calculations.logger.info("Viewing history.")
        Calculations.load_history()
        return Calculations.history

    @staticmethod
    def get_latest():
        """
        Get the latest calculation.

        Returns:
            Calculation: The latest calculation.
        """
        Calculations.load_history()
        if not Calculations.history.empty:
            latest_entry = Calculations.history.iloc[-1]
            operation_map = {
                'add': add,
                'subtract': subtract,
                'multiply': multiply,
                'divide': divide,
                'exponent': exponent
            }
            operation = operation_map.get(latest_entry['Operation'])
            if operation is None:
                raise ValueError(f"Unknown operation '{latest_entry['Operation']}' in history")
            return Calculation(operation, Decimal(latest_entry['Operand_A']), Decimal(latest_entry['Operand_B']))
        return None

    @staticmethod
    def delete_history_entry(index: int):
        """
        Delete a specific entry from the history.

        Args:
            index (int): The index of the entry to delete.
        """
        Calculations.logger.info("Attempting to delete history entry at index %d.", index)
        Calculations.load_history()
        if 0 <= index < len(Calculations.history):
            Calculations.history = Calculations.history.drop(index).reset_index(drop=True)
            Calculations.logger.info("Deleted history entry at index %d.", index)
            Calculations.save_history()
        else:
            Calculations.logger.warning("Index %d is out of range. No entry deleted.", index)

    @staticmethod
    def save_history_to_csv(file_path: str):
        """
        Save the calculation history to a CSV file.

        Args:
            file_path (str): The path to save the history to.
        """
        Calculations.logger.info("Saving history to %s", file_path)
        Calculations.load_history()
        Calculations.history.to_csv(file_path, index=False)
        Calculations.logger.info("History saved to %s", file_path)

    @staticmethod
    def load_history_from_csv(file_path: str = "data/calculation_history.csv"):
        """
        Load the calculation history from a CSV file.

        Args:
            file_path (str): The path to load the history from.
        """
        try:
            Calculations.logger.info("Loading history from %s", file_path)
            Calculations.history = pd.read_csv(file_path)
            Calculations.logger.info("Loaded history from %s:\n%s", file_path, Calculations.history)
        except FileNotFoundError:
            Calculations.logger.warning("No existing history found. Creating new history.")
            Calculations.history = Calculations.create_empty_history()
