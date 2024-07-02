import os
import pandas as pd
from decimal import Decimal
from .operation_functions import add, subtract, multiply, divide, exponent
from .calculation import Calculation

class Calculations:
    """Class to manage the history of calculations."""
    history_dir = "data"
    history_file = os.path.join(history_dir, "calculation_history.csv")
    history = pd.DataFrame(columns=["Operation", "Operand_A", "Operand_B", "Result"])

    @staticmethod
    def create_empty_history():
        """Create an empty history DataFrame with the correct columns."""
        return pd.DataFrame(columns=["Operation", "Operand_A", "Operand_B", "Result"])
    
    @staticmethod
    def load_history():
        """Load calculation history from a CSV file."""
        #print(f"Attempting to load history from {Calculations.history_file}")
        if os.path.exists(Calculations.history_file) and os.path.getsize(Calculations.history_file) > 0:
            with open(Calculations.history_file, 'r') as file:
                file_contents = file.read()
                #print(f"Contents of {Calculations.history_file} before loading:\n{file_contents}")
            Calculations.history = pd.read_csv(Calculations.history_file)
            #print(f"Loaded history from {Calculations.history_file}:\n{Calculations.history}")
        else:
            #print(f"No existing history found or file is empty. Creating new history.")
            Calculations.history = Calculations.create_empty_history()

    @staticmethod
    def save_history():
        """Save calculation history to a CSV file."""
        os.makedirs(Calculations.history_dir, exist_ok=True)
        #print(f"Saving history to {Calculations.history_file}")
        Calculations.history.to_csv(Calculations.history_file, index=False)
        #print(f"Saved history to {Calculations.history_file}:\n{Calculations.history}")
    
        # Print the contents of the file to verify
        with open(Calculations.history_file, 'r') as file:
            file_contents = file.read()
            #print(f"Contents of {Calculations.history_file} after saving:\n{file_contents}")

    @staticmethod
    def add_calculation(calculation: Calculation):
        """Add a calculation to the history."""
        #print(f"Adding calculation: {calculation}")
        result = calculation.perform_operation()
        new_entry = {
            'Operation': calculation.operation.__name__,
            'Operand_A': float(calculation.a),
            'Operand_B': float(calculation.b),
            'Result': float(result)
        }
        #print(f"Adding new calculation entry: {new_entry}")
        Calculations.load_history()
        #print(f"History before adding new entry:\n{Calculations.history}")
        new_entry_df = pd.DataFrame([new_entry])
        #print(f"New entry DataFrame:\n{new_entry_df}")
        if Calculations.history.empty:
            Calculations.history = new_entry_df
        else:
            Calculations.history = pd.concat([Calculations.history, new_entry_df], ignore_index=True)
        #print(f"History after adding new entry:\n{Calculations.history}")
        Calculations.save_history()


    @staticmethod
    def clear_history():
        """Clear the calculation history."""
        #print("Clearing history.")
        Calculations.history = Calculations.create_empty_history()
        Calculations.save_history()
        #print(f"Cleared history:\n{Calculations.history}")

    @staticmethod
    def delete_history():
        """Delete the history file."""
        try:
            os.remove(Calculations.history_file)
            #print(f"Deleted history file: {Calculations.history_file}")
        except FileNotFoundError:
            print(f"No history file found to delete.")

    @staticmethod
    def view_history():
        """Return the calculation history."""
#         print("Viewing history.")
        Calculations.load_history()
#         print(f"Current history:\n{Calculations.history}")
        return Calculations.history

    @staticmethod
    def get_latest():
        """Get the latest calculation."""
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
        else:
            return None

    @staticmethod
    def delete_history_entry(index: int):
        """Delete a specific entry from the history."""
#         print(f"Attempting to delete history entry at index {index}.")
        Calculations.load_history()
        if 0 <= index < len(Calculations.history):
            Calculations.history = Calculations.history.drop(index).reset_index(drop=True)
#             print(f"Deleted history entry at index {index}.")
            Calculations.save_history()
        else:
            print(f"Index {index} is out of range. No entry deleted.")

    @staticmethod
    def save_history_to_csv(file_path: str):
        """Save the calculation history to a CSV file."""
        print(f"Saving history to {file_path}")
        Calculations.load_history()
        Calculations.history.to_csv(file_path, index=False)
        print(f"History saved to {file_path}")

    @staticmethod
    def load_history_from_csv(file_path: str = "data/calculation_history.csv"):
        """Load the calculation history from a CSV file."""
        try:
#             print(f"Loading history from {file_path}")
            Calculations.history = pd.read_csv(file_path)
#             print(f"Loaded history from {file_path}:\n{Calculations.history}")
        except FileNotFoundError:
#             print("No existing history found. Creating new history.")
            Calculations.history = Calculations.create_empty_history()
