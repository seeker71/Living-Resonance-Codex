#!/usr/bin/env python3
"""
Advanced Neural Network Implementation
Demonstrates attention mechanisms and modern deep learning techniques
"""

import numpy as np
import tensorflow as tf
from typing import Tuple, List, Optional

class AttentionMechanism:
    """Implements multi-head attention mechanism for neural networks"""
    
    def __init__(self, d_model: int, num_heads: int):
        self.d_model = d_model
        self.num_heads = num_heads
        self.depth = d_model // num_heads
        
        # Initialize weight matrices
        self.wq = tf.keras.layers.Dense(d_model)
        self.wk = tf.keras.layers.Dense(d_model)
        self.wv = tf.keras.layers.Dense(d_model)
        self.wo = tf.keras.layers.Dense(d_model)
    
    def scaled_dot_product_attention(self, q: tf.Tensor, k: tf.Tensor, v: tf.Tensor, mask: Optional[tf.Tensor] = None) -> Tuple[tf.Tensor, tf.Tensor]:
        """Compute scaled dot-product attention"""
        matmul_qk = tf.matmul(q, k, transpose_b=True)
        
        # Scale the attention scores
        dk = tf.cast(tf.shape(k)[-1], tf.float32)
        scaled_attention_logits = matmul_qk / tf.math.sqrt(dk)
        
        # Apply mask if provided
        if mask is not None:
            scaled_attention_logits += (mask * -1e9)
        
        # Apply softmax to get attention weights
        attention_weights = tf.nn.softmax(scaled_attention_logits, axis=-1)
        
        # Apply attention weights to values
        output = tf.matmul(attention_weights, v)
        
        return output, attention_weights
    
    def call(self, inputs: tf.Tensor, mask: Optional[tf.Tensor] = None) -> tf.Tensor:
        """Forward pass through attention mechanism"""
        batch_size = tf.shape(inputs)[0]
        
        # Linear transformations
        q = self.wq(inputs)
        k = self.wk(inputs)
        v = self.wv(inputs)
        
        # Reshape for multi-head attention
        q = tf.reshape(q, [batch_size, -1, self.num_heads, self.depth])
        k = tf.reshape(k, [batch_size, -1, self.num_heads, self.depth])
        v = tf.reshape(v, [batch_size, -1, self.num_heads, self.depth])
        
        # Transpose for attention computation
        q = tf.transpose(q, [0, 2, 1, 3])
        k = tf.transpose(k, [0, 2, 1, 3])
        v = tf.transpose(v, [0, 2, 1, 3])
        
        # Apply attention
        scaled_attention, attention_weights = self.scaled_dot_product_attention(q, k, v, mask)
        
        # Reshape back
        scaled_attention = tf.transpose(scaled_attention, [0, 2, 1, 3])
        concat_attention = tf.reshape(scaled_attention, [batch_size, -1, self.d_model])
        
        # Final linear transformation
        output = self.wo(concat_attention)
        
        return output

class TransformerBlock(tf.keras.layers.Layer):
    """Transformer block with attention and feed-forward networks"""
    
    def __init__(self, d_model: int, num_heads: int, dff: int, rate: float = 0.1):
        super(TransformerBlock, self).__init__()
        
        self.att = AttentionMechanism(d_model, num_heads)
        self.ffn = tf.keras.Sequential([
            tf.keras.layers.Dense(dff, activation='relu'),
            tf.keras.layers.Dense(d_model)
        ])
        
        self.layernorm1 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = tf.keras.layers.LayerNormalization(epsilon=1e-6)
        
        self.dropout1 = tf.keras.layers.Dropout(rate)
        self.dropout2 = tf.keras.layers.Dropout(rate)
    
    def call(self, inputs: tf.Tensor, training: bool = False, mask: Optional[tf.Tensor] = None) -> tf.Tensor:
        """Forward pass through transformer block"""
        # Multi-head attention
        attn_output = self.att(inputs, mask)
        attn_output = self.dropout1(attn_output, training=training)
        out1 = self.layernorm1(inputs + attn_output)
        
        # Feed-forward network
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output, training=training)
        out2 = self.layernorm2(out1 + ffn_output)
        
        return out2

def create_transformer_model(vocab_size: int, d_model: int, num_layers: int, num_heads: int, dff: int, maximum_position_encoding: int) -> tf.keras.Model:
    """Create a complete transformer model"""
    
    inputs = tf.keras.layers.Input(shape=(None,))
    
    # Embedding and positional encoding
    embedding = tf.keras.layers.Embedding(vocab_size, d_model)
    pos_encoding = positional_encoding(maximum_position_encoding, d_model)
    
    x = embedding(inputs)
    x = x + pos_encoding[:, :tf.shape(x)[1], :]
    
    # Transformer blocks
    for _ in range(num_layers):
        x = TransformerBlock(d_model, num_heads, dff)(x)
    
    # Output layer
    outputs = tf.keras.layers.Dense(vocab_size)(x)
    
    return tf.keras.Model(inputs=inputs, outputs=outputs)

def positional_encoding(position: int, d_model: int) -> tf.Tensor:
    """Generate positional encoding for transformer model"""
    angle_rads = get_angles(np.arange(position)[:, np.newaxis],
                           np.arange(d_model)[np.newaxis, :],
                           d_model)
    
    # Apply sin to even indices
    angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])
    
    # Apply cos to odd indices
    angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])
    
    pos_encoding = angle_rads[np.newaxis, ...]
    
    return tf.cast(pos_encoding, dtype=tf.float32)

def get_angles(pos: np.ndarray, i: np.ndarray, d_model: int) -> np.ndarray:
    """Calculate angles for positional encoding"""
    angle_rates = 1 / np.power(10000, (2 * (i//2)) / np.float32(d_model))
    return pos * angle_rates

# Example usage
if __name__ == "__main__":
    # Create a small transformer model
    model = create_transformer_model(
        vocab_size=10000,
        d_model=512,
        num_layers=6,
        num_heads=8,
        dff=2048,
        maximum_position_encoding=1000
    )
    
    print("Transformer model created successfully!")
    print(f"Model parameters: {model.count_params():,}")
