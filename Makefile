# train model
train:
		python3 train.py --model_name bert_ssc --dataset restaurant --valset_ratio 0.2 --pretrained_bert_name bert-base-multilingual-cased --polarities_dim 5


