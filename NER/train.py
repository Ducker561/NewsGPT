from NER.utils import *
from NER.model import *
from NER.config import *

if __name__ == '__main__':
    dataset = Dataset()
    loader = data.DataLoader(
        dataset,
        batch_size=100,
        shuffle=True,
        collate_fn=collate_fn,
    )

    model = Model().to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)

    for e in range(EPOCH):
        for b, (input, target, mask) in enumerate(loader):

            input = input.to(DEVICE)
            mask = mask.to(DEVICE)
            target = target.to(DEVICE)

            y_pred = model(input, mask)

            loss = model.loss_fn(input, target, mask)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if b % 10 == 0:
                print('>> epoch:', e, 'loss:', loss.item())
        if (e+1) % 50 == 0:
            torch.save(model, MODEL_DIR + f'model_{e}.pth')
