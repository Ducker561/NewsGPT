from NER.utils import *
from NER.model import *
from NER.config import *

def ner(text):
    # text = '广州地铁张薇虚构大叔偷拍'
    _, word2id = get_vocab()
    input = torch.tensor([[word2id.get(w, WORD_UNK_ID) for w in text]])
    mask = torch.tensor([[1] * len(text)]).bool()
    input=input.to(DEVICE)
    mask=mask.to(DEVICE)

    ner_model = torch.load(MODEL_DIR + 'model_7499.pth', map_location=DEVICE)
    y_pred = ner_model(input, mask)
    id2label, _ = get_label()

    label = [id2label[l] for l in y_pred[0]]
    info = extract(label, text)

    return info
