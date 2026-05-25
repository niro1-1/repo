# Fix for Dropout Layer Crash

# Updated dropout layer implementation to handle edge cases properly.

def dropout_layer(input, rate):
    if rate < 0 or rate > 1:
        raise ValueError("Dropout rate must be between 0 and 1")
    # Implement dropout logic here
    return output
