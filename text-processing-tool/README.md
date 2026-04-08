# Text Processing Tool

This is a Python-based text processing tool that cleans and analyzes user input step by step.

## Features
- Convert text to lowercase
- Remove punctuation
- Remove common stop words
- Filter long words (length ≥ 4)
- Extract unique words
- Sort words by length (ascending and descending)
- Calculate word frequency

## How it works
The program takes a text input from the user and processes it through multiple stages:
cleaning, filtering, sorting, and analysis.

## How to run

```bash
python text_processing.py

##Example
Enter a text:
Python is great and Python is easy to learn!

Output:
Original words: ['Python', 'is', 'great', 'and', 'Python', 'is', 'easy', 'to', 'learn!']
Lowered words: ['python', 'is', 'great', 'and', 'python', 'is', 'easy', 'to', 'learn!']
Remove punctuation: ['python', 'is', 'great', 'and', 'python', 'is', 'easy', 'to', 'learn']
Removed from stop words: ['python', 'great', 'python', 'easy', 'learn']
Longer words: ['python', 'great', 'python', 'easy', 'learn']
Unique words: ['python', 'great', 'easy', 'learn']
Sorted by length (asc): ['easy', 'learn', 'great', 'python']
Sorted by length (desc): ['python', 'great', 'learn', 'easy']
Frequency: {'python': 2, 'great': 1, 'easy': 1, 'learn': 1}