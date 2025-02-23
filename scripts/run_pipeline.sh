#!/bin/bash

# Step 1: Data Processing
echo "Starting data processing..."
python src/data_processing/process_data.py

# Step 2: Model Training
echo "Starting model training..."
python src/training/train.py

# Step 3: Model Evaluation
echo "Starting model evaluation..."
python src/evaluation/evaluate.py

echo "Pipeline execution completed."