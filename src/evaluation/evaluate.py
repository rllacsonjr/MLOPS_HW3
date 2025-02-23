def evaluate_model(model, test_data):
    predictions = model.predict(test_data)
    # Assuming test_data has true labels for evaluation
    true_labels = test_data['labels']
    
    accuracy = (predictions == true_labels).mean()
    # You can add more metrics like precision, recall, F1-score, etc.
    
    return {
        'accuracy': accuracy,
        # Add other metrics here as needed
    }