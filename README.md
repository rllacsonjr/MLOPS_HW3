# MLOps HW3

This project is designed to implement a machine learning operations (MLOps) pipeline that encompasses data processing, model training, and evaluation. The goal is to streamline the workflow from raw data to a deployed model.

## HW Structure

- **data/**
  - **raw/**: Contains the raw data files used for training and evaluation.
  - **processed/**: Contains the cleaned and transformed data files ready for model training.

- **notebooks/**
  - **exploration.ipynb**: A Jupyter notebook for exploratory data analysis, including code and visualizations to understand the dataset better.

- **src/**
  - **models/**: Contains the model architecture definition.
    - **model.py**: Defines the `Model` class with methods for initialization, training, and prediction.
  - **training/**: Contains the training logic.
    - **train.py**: Handles the training process, including data loading and model fitting.
  - **evaluation/**: Contains the evaluation logic.
    - **evaluate.py**: Exports a function to evaluate the trained model against test data.

- **scripts/**
  - **run_pipeline.sh**: A shell script to run the entire machine learning pipeline, including data processing, model training, and evaluation.

- **requirements.txt**: Lists the Python dependencies required for the project, such as pandas, scikit-learn, and TensorFlow.

- **Dockerfile**: Contains instructions to build a Docker image for the project, specifying the base image, working directory, and commands to install dependencies.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mlops-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the exploratory data analysis notebook:
   ```
   jupyter notebook notebooks/exploration.ipynb
   ```

4. To run the entire pipeline, execute the shell script:
   ```
   bash scripts/run_pipeline.sh
   ```

This README provides a comprehensive overview of the MLOps project, guiding users through setup and usage.
