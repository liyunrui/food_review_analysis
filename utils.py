
def to_txt(df, file_path, text_columns, label_columns):
    f = open(file_path, "w")
    for ix, row in df.iterrows():
        text = row[text_columns].strip()
        text = text.replace('\n',' ')
        text = text.replace('\r',' ')
        label = str(row[label_columns])
        f.write(text)
        f.write('\n')
        f.write(label)
        f.write('\n')
    f.close()
    print ("writing txt finished")