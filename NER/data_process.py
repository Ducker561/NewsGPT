import pandas as pd
from NER.config import *


def init_process():
    with open(TRAIN_SAMPLE_PATH, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    # 去除空行
    non_empty_lines = list(filter(lambda x: x.strip(), lines))

    with open(TRAIN_SAMPLE_PATH, 'w', encoding='UTF-8') as file:
        file.write(''.join(non_empty_lines))

# 生成词表
def generate_vocab():
    df = pd.read_csv(TRAIN_SAMPLE_PATH, usecols=[0], names=['word'], on_bad_lines='warn', engine='python', sep="\t")
    df['word'] = df['word'].apply(lambda x: x[:1])
    vocab_list = [WORD_PAD, WORD_UNK] + df['word'].value_counts().keys().tolist()
    vocab_list = vocab_list[:VOCAB_SIZE]
    vocab_dict = {v: k for k, v in enumerate(vocab_list)}
    vocab = pd.DataFrame(list(vocab_dict.items()))
    vocab.to_csv(VOCAB_PATH, header=None, index=None)


# 生成标签表
def generate_label():
    df = pd.read_csv(TRAIN_SAMPLE_PATH, usecols=[1], names=['label'], error_bad_lines=False, engine='python', sep="\t")
    label_list = df['label'].value_counts().keys().tolist()
    label_dict = {v: k for k, v in enumerate(label_list)}
    label = pd.DataFrame(list(label_dict.items()))
    label.to_csv(LABEL_PATH, header=None, index=None)


