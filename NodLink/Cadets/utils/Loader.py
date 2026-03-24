import torch
import json
import numpy as np
class Loader(torch.utils.data.Dataset):
    def __init__(self):
        super(Loader, self).__init__()
        self.dataset = ''
        self.idx2processnum = []
    
    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, idx):
        data = self.dataset[self.idx2processnum[idx]]
        return data
    
class Train_Loader(Loader):
    def __init__(self, path):
        super(Train_Loader, self).__init__()

        self.dataset = json.load(open(path,'r'))
        for i in self.dataset:
            self.idx2processnum += [i]
            self.dataset[i] = torch.FloatTensor(self.dataset[i])

# from torch.nn.utils.rnn import pad_sequence

# class Train_Loader:
#     def __init__(self, path):
#         with open(path, 'r') as f:
#             self.dataset = json.load(f)
#         self.keys = list(self.dataset.keys())
        
#         # Convert all embeddings to tensors and pad them
#         self.embeddings = [torch.FloatTensor(emb) for emb in self.dataset.values()]
#         self.embeddings = pad_sequence(self.embeddings, batch_first=True, padding_value=0)

#     def __len__(self):
#         return len(self.keys)

#     def __getitem__(self, idx):
#         return self.embeddings[idx]