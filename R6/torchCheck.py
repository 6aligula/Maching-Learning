import torch

if torch.cuda.is_available():
    print(f"PyTorch detectó GPU: {torch.cuda.get_device_name(0)}")
else:
    print("PyTorch no detecta ninguna GPU.")
