import torch
import torch.nn as nn

model = nn.Transformer(
    d_model=512, 
    nhead=8, 
    num_encoder_layers=6,
    num_decoder_layers=6
)

src = torch.rand((10, 32, 512))  # seq_len, batch, features
tgt = torch.rand((20, 32, 512))

output = model(src, tgt)
print(output.shape)
