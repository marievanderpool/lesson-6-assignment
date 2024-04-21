# 1. Product Review Analysis

# Objective:
# The aim of this assignment is to extract insights from product reviews by using 
# string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter

# Write a program that searches through a series of product reviews for keywords such as "good",
#  "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase
#  so they stand out.

reviews = ["This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.","The product was average. Nothing extraordinary about it."]


def review_highlight(reviews):
    key_words = ["good", "excellent", "bad", "poor", "average"]
    for review in reviews:
        for kw in key_words:
            if kw in review:
               review = review.replace(kw, kw.upper())
            elif kw.title() in review:
               review = review.replace(kw.title(), kw.upper())
        print(review)
        

review_highlight(reviews)

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review.
#  Use a predefined list of positive and negative words to check against. 
# The function should return the count of positive and negative words for each review.

def word_count (reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    return positive_words, negative_words

print(positive_words.count(reviews)) 
print(negative_words.count(reviews)) 


# Task 3: Review Summary

# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary.
#  Ensure that the summary does not cut off in the middle of a word.

def create_summary(reviews):
    if len(reviews) > 30:
        print(len(30))
    else:
        summary = reviews
        return(summary)

