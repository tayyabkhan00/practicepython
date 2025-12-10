import torch
import torch.nn as nn

model = nn.Transformer(
    d_model=512,
    nhead=8,
    num_encoder_layers=6,
    num_decoder_layers=6,
    batch_first=True
)

src = torch.rand((32, 10, 512))  # batch, seq_len, features
tgt = torch.rand((32, 20, 512))

output = model(src, tgt)
print(output.shape)
