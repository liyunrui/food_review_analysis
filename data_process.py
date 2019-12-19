import re
import pandas as pd
from utils import to_txt

train_path = "dataset/training data.csv"
test_path = "dataset/test data.csv"
train = pd.read_csv(train_path, delimiter = ";", header = None).rename(columns = {0:"review",1:"rating"})
test = pd.read_csv(test_path,delimiter=",,,,,,,,,,,,,,^M",skipinitialspace = True)

to_txt(train,
    file_path = "dataset/restaurant/thai_restaurant_train.txt", 
    text_columns = "review", 
    label_columns = "rating")

document = ""
for ix, row in test.iterrows():
    document+= str(row["reviewID;review,,,,,,,,,,,,,,"])+""

str_delimiters = re.findall(r'[0-9]+;', document)

str_delimiter_index = [(document.index(str_delimiter)
                        , document.index(str_delimiter)+ len(str_delimiter))
                       for str_delimiter in str_delimiters[:]]
reviewID = [int(re.findall(r'[0-9]+', str_delimiter)[0]) for str_delimiter in str_delimiters[:]]

reviews = []
for i in range(len(str_delimiter_index)):
    if i!= len(str_delimiter_index)-1:
        s_ix, e_ix = str_delimiter_index[i]
        next_s_ix, next_e_ix = str_delimiter_index[i+1]
        review = document[e_ix:next_s_ix]
    else:
        review = document[next_e_ix:len(document)]

    review = review.strip().replace(",,,,,,,,,,,,,,"," ")
    reviews.append(review)

test = pd.DataFrame({
    "reviewID":reviewID,
    "review":reviews
})
test.review = test.review.apply(lambda x: x.replace('"', ""))
test.to_csv("result/submission.csv", index = False)

