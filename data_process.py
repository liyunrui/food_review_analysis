import pandas as pd
from utils import to_txt

train_path = "dataset/training data.csv"
test_path = "dataset/test data.csv"
train = pd.read_csv(train_path, delimiter = ";", header = None).rename(columns = {0:"review",1:"rating"})


to_txt(train,
    file_path = "dataset/restaurant/thai_restaurant_train.txt", 
    text_columns = "review", 
    label_columns = "rating")