import os
import pandas as pd
from src.models.model import Model

def load_data(data_path):
    # Load the training data from the specified path
    return pd.read_csv(data_path)

def train_model(data_path):
    # Load the training data
    data = load_data(data_path)
    
    # Initialize the model
    model = Model()
    
    # Train the model on the loaded data
    model.train(data)
    
    # Save the trained model (optional)
    model.save('model.pkl')

if __name__ == "__main__":
    # Define the path to the training data
    data_path = os.path.join('data', 'processed', 'training_data.csv')
    
    # Train the model
    train_model(data_path)