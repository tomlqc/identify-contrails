# Identify Contrails to Reduce Global Warming

My contribution to the 2023 Kaggle competition:

https://www.kaggle.com/competitions/google-research-identify-contrails-reduce-global-warming

I did not get a significant rank (see [statistics](notebooks/Kaggle-competition-statistics.ipynb)),
but my original goal was to learn some advanced TensorFlow and to get some practice.

It was my first Kaggle competition and it was also an opportunity to explore Google Cloud's Vertex AI.

## Submission notebook

The notebook that I have continuously worked on is

[notebooks/identify-contrails.ipynb](notebooks/identify-contrails.ipynb)

It includes:

- A data pipeline based on TFRecords, as the Keras dataset was not efficient enough for properly feeding the GPU,
  including a multiprocessing parallelized generation of TFRecords
- Data augmentation
- Models:
  - Pseudo-3D ResNet (P3DResNet) implementation inspired by Keras' ResNet50
  - U-Net with self-made encoder, ResNet50 or P3DResNet
  - DeepLabV3+ with ResNet50 or P3DResNet
- Gradient accumulation (the implementation did not show any benefit)

## History

The history of my (yet a bit messy) experiments:

[notebooks-logs/History.ipynb](notebooks-logs/History.ipynb)

A summary of my submissions:

| version | model | augm | epochs | train | valid | (threshold) valid | submission | final score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| v44 | UNet/Basic | light | 30 | 0.5008 | 0.4321 | (0.3) 0.5529 | **0.613** | **0.633** |
| v47 | DeepLab/ResNet50 | no | 50 | 0.7321 | 0.4098 | (0.2) 0.4578 | 0.509 | 0.540 |
| v48 | DeepLab/ResNet50 | light | 50 | 0.5126 | 0.3221 | (0.2) 0.4592 | 0.458 | 0.510 |
| v49 | DeepLab/P3DResNet | no | 32 | 0.5214 | 0.3475 | (0.2) 0.4546 | 0.499 |  0.518 |
| v45 | DeepLab/P3DResNet | light | 40 | 0.4329  | 0.3028 | (0.2) 0.4633 | **0.546** | **0.557** |

I struggled with slow iterations of my U-Net (not yet explained) and
with the data augmentation that did not provide a better generalization as expected.
The latter is probably due to the misalignment of the masks with the images,
as mentioned in this [discussion](https://www.kaggle.com/competitions/google-research-identify-contrails-reduce-global-warming/discussion/430479#2382723).

## Next

I got a first taste of Kaggle and I am excited to participate in one next competition!

Next time I will certainly work more with scripts and not only notebooks,
and explore both Kaggle and gcloud APIs.

See you soon :)

Published under the MIT License, see [LICENSE](LICENSE) in this repository.
