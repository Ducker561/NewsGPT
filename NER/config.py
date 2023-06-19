TRAIN_SAMPLE_PATH = 'NER/Weibo_data/weiboNER_2nd_conll.train'
TEST_SAMPLE_PATH = 'NER/Weibo_data/weiboNER_2nd_conll.test'

VOCAB_PATH = 'NER/Weibo_data/vocab.txt'
LABEL_PATH = 'NER/Weibo_data/label.txt'

WORD_PAD = '<PAD>'
WORD_UNK = '<UNK>'

WORD_PAD_ID = 0
WORD_UNK_ID = 1
LABEL_O_ID = 0

VOCAB_SIZE = 10000
EMBEDDING_DIM = 100
HIDDEN_SIZE = 256
TARGET_SIZE = 17
LR = 1e-4
EPOCH = 100

MODEL_DIR = 'NER/model/'

import torch

DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'