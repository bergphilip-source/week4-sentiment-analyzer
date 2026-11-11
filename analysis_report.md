# Sentiment Model Accuracy

The classifier was trained on the six labeled reviews in `test_reviews.txt`
(three positive and three negative).

| Evaluation | Correct | Total | Accuracy |
| --- | ---: | ---: | ---: |
| Training set (resubstitution) | 6 | 6 | 100.0% |
| Leave-one-out cross-validation | 1 | 6 | 16.7% |

## Challenge Set

The analyzer classified 25 examples from `challenge_set.py`:

| Challenge category | Positive | Negative | Total |
| --- | ---: | ---: | ---: |
| Negation | 0 | 5 | 5 |
| Sarcasm | 1 | 4 | 5 |
| Mixed Sentiment | 1 | 4 | 5 |
| Intensity | 2 | 3 | 5 |
| Domain Shift | 3 | 2 | 5 |
| **Total** | **7** | **18** | **25** |

Challenge-set accuracy is **not available** because these examples have no
ground-truth sentiment labels. The counts above are predictions, not accuracy
measurements. Add labeled answers for the challenge examples to calculate it.

Training accuracy measures predictions on reviews the classifier already saw
and overstates its ability to classify new reviews. Leave-one-out validation
retrained the classifier six times, holding out one review each time. Its low
score indicates that this six-review dataset is too small to support reliable
generalization; more labeled training data is needed.