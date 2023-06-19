from NER import predict
import torch.nn as nn
from hanlp_restful import HanLPClient
from news_gpt import run

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.embed = nn.Embedding(VOCAB_SIZE, EMBEDDING_DIM, WORD_PAD_ID)
        self.lstm = nn.LSTM(
            EMBEDDING_DIM,
            HIDDEN_SIZE,
            batch_first=True,
            bidirectional=True,
        )
        self.linear = nn.Linear(2 * HIDDEN_SIZE, TARGET_SIZE)
        self.crf = CRF(TARGET_SIZE, batch_first=True)

    def _get_lstm_feature(self, input):
        out = self.embed(input)
        out, _ = self.lstm(out)
        return self.linear(out)

    def forward(self, input, mask):
        out = self._get_lstm_feature(input)
        return self.crf.decode(out, mask)

    def loss_fn(self, input, target, mask):
        y_pred = self._get_lstm_feature(input)
        return -self.crf.forward(y_pred, target, mask, reduction='mean')

if __name__ == '__main__':
    question = input("Please give me your question for recent news : ")
    ner_info = predict.ner(question)
    need_token = []
    for _info in ner_info:
        need_token.append(_info[1])
    HanLP = HanLPClient('https://www.hanlp.com/api', auth='MjY0OEBiYnMuaGFubHAuY29tOlVtdWNESGdDWjJrbFZEaEE=', language='zh')
    hanlp_result = HanLP(question, tasks='pos')
    tok = hanlp_result['tok/fine'][0]
    pos = hanlp_result['pos/ctb'][0]
    cnt=0
    for po in pos:
        if po=='NN' or po=='VV' or po=='NR':
            need_token.append(tok[cnt])
        cnt+=1
    filter_token = []
    topk2 = HanLP.keyphrase_extraction(question, topk=2).keys()
    topk2 = list(topk2)
    for token in need_token:
        if token in topk2[0] or token in topk2[1]:
            filter_token.append(token)

    keyword = ""
    for token in filter_token:
        keyword += token
        if token == filter_token[-1]:
            break
        keyword += " "
    res = run(keyword, question)
    print(res)
