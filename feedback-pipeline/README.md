# Feedback Pipeline

This is a simple Python-based feedback processing pipeline.

## Features
- Accepts user feedback input
- Cleans and processes text data
- Applies multiple transformation steps
- Outputs structured results

## How it works

The program takes feedback input from the user and processes it through a series of steps such as:
- Text cleaning
- Filtering
- Transformation
- Analysis

Each step is applied sequentially, forming a simple data processing pipeline.

## How to run

```bash
python feedback_pipeline.py

Enter feedback:
This product is amazing but a bit expensive!

Output:
Cleaned text: this product is amazing but a bit expensive
Filtered words: ['product', 'amazing', 'expensive']
Analysis: Positive feedback with minor concern