"""
A confusion matrix is a summary of prediction results on a classification problem.
The number of correct and incorrect predictions are summarized with count values and
broken down by each class. This is the key to the confusion matrix. The confusion matrix shows the ways in which
your classification model is confused when it makes predictions. It gives us insight not only into the errors being
made by a classifier but more importantly the types of errors that are being made.

Positive (P) : Observation is positive (for example: is an apple).
Negative (N) : Observation is not positive (for example: is not an apple).
True Positive (TP) : Observation is positive, and is predicted to be positive.
False Negative (FN) : Observation is positive, but is predicted negative.
True Negative (TN) : Observation is negative, and is predicted to be negative.
False Positive (FP) : Observation is negative, but is predicted positive.

-------------------------------
|Class 1      |               |
|Prediced             |               |
|             |               |
-------------------------------
|             |               |
|             |               |
|             |               |
|             |               |
-------------------------------


"""

