import os
import numpy as np
import tensorflow as tf

def generate_training_data():
    """Genera y retorna los datos de entrenamiento ficticios."""
    X_train = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0],  # X juega en el centro
        [0, 0, 0, 1, 0, 0, 0, 0, 0],  # X juega en la cuarta posición
        [1, 0, 0, 0, 0, 0, 0, 0, 0],  # X juega en la primera posición
    ]
    y_train = [4, 3, 0]  # Movimientos ideales para los ejemplos anteriores
    return np.array(X_train), np.array(y_train)

def train_model():
    """Entrena y retorna el modelo de Tic Tac Toe."""
    X_train, y_train = generate_training_data()
    
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(18, activation='relu', input_shape=(9,)),
        tf.keras.layers.Dense(18, activation='relu'),
        tf.keras.layers.Dense(9, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=200)
    
    return model

def save_trained_model(model, path='models/tic_tac_toe_model.h5'):
    """Guarda el modelo entrenado en el path especificado."""
    model.save(path)

def load_trained_model(model_path='models/tic_tac_toe_model.h5'):
    """Carga y retorna el modelo entrenado desde el path especificado."""
    return tf.keras.models.load_model(model_path)

def predict_best_move(model, board):
    """Predice el mejor movimiento basado en el modelo y el estado actual del tablero."""
    numeric_board = [1 if cell == 'X' else 2 if cell == 'O' else 0 for cell in board]
    predictions = model.predict(np.array([numeric_board]))
    return np.argmax(predictions)

# Si deseas entrenar y guardar el modelo al ejecutar este archivo:
# if __name__ == "__main__":
#     model = train_model()
#     save_trained_model(model)
