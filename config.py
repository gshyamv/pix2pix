import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2

DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
LEARNING_RATE = 4e-4
BATCH_SIZE = 32
NUM_WORKERS = 2
IMAGE_SIZE = 256
CHANNELS_IMG = 3
L1_LAMBDA = 100
NUM_EPOCHS = 100
LOAD_MODEL = True
SAVE_MODEL = True
CHECKPOINT_DISC = "disc.pth.tar"
CHECKPOINT_GEN = "gen.pth.tar"

both_transform = A.Compose(
    [A.Resize(width=256, height=256), A.HorizontalFlip(p=0.5),],additional_targets={"image0": "image"},
)

transpose_only_input = A.Compose(
    [
         A.ColorJitter(p=0.1),
         A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255.0,),
         ToTensorV2(),
     ]
)

transpose_only_mask = A.Compose(
    [
         A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255.0,),
         ToTensorV2(),
    ]
)

