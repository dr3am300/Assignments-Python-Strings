# Task 1: Keyword Highlighter
# Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.
    # reviews = [
       # "This product is really good. I'm impressed with its quality.",
       # "The performance of this product is excellent. Highly recommended!",
       # "I had a bad experience with this product. It didn't meet my expectations.",
       # "Poor quality product. Wouldn't recommend it to anyone.",
       # "The product was average. Nothing extraordinary about it."
# So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."

def keyword_highlighter(reviews):
    keywords = ["good", "excellent", "bad", "Poor", "average"]
    for review in reviews:
        for keyword in keywords:
            if keyword in review:
                review = review.replace(keyword, keyword.upper())
        print(review)

while True:
    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
    keyword_highlighter(reviews)
    break

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
    # positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    # negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar",]
    for review in reviews:
        positive_count = 0
        negative_count = 0
        for word in review.split():
            if word.lower() in positive_words:
                positive_count += 1
            elif word.lower() in negative_words:
                negative_count += 1
        print(f"Positive words: {positive_count}, Negative words: {negative_count}")
        
while True:
    reviews = [ "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]
    sentiment_tally(reviews)
    break


# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

def review_summary(reviews):
    for review in reviews:
        summary = review[:30]
        if len(review) > 30:
            last_space = summary.rfind(" ")
            summary = summary[:last_space] + "..."
        print(summary) 

while True:
    reviews = [ "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]
    review_summary(reviews)
    break



        

              

            
        