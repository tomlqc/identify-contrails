
# Saved Notebooks

- Notebook executed on GCP.
- Text dumps of Kaggle notebooks' "Save and Run All" versions. 

## How-to execute notebooks in GCP

```
nohup jupyter nbconvert --to notebook --execute ~/identify-contrails/notebooks/identify-contrails.ipynb --output identify-contrails-executed.ipynb &
```

Reference: https://nbconvert.readthedocs.io/en/latest/usage.html#notebook-and-preprocessors

## How to get these notebook dumps

First in the browser:

1. Notebook > "Show versions"
2. Version > "Open in Viewer"
3. Notebook > Make selection and copy

Then in the text editor:

4. Paste and save.

## History

### [v11] U-Net v2.3 cst-lr and threshold 

After 10 epochs:

- train dice_coef: 0.5028
- valid dice_coef: 0.4263

**Submission: 0.558** (threshold of 0.40)

### [v19] DeepLabV3+, w/o preprocessing, resnet50 not trainable

After 10 epochs:

- train dice_coef: 0.2484
- valid dice_coef: 0.0091 - very poor, with a peak inbetween

Conclusion

- Need to train resnet50 weights.

### [v20] DeepLabV3+, w/o preproc, resnet50 trainable

After 10 epochs:

- train dice_coef: 0.4370
- valid dice_coef: 0.2828 - encouraging

After 15 epochs:

- train dice_coef: 0.5254
- valid dice_coef: 0.3614 - encouraging

Wrote contrails_2023-07-20_22-39-56.h5

Conclusion:

- Training resnet50 weights works.
- Linear learning in terms of dice_coef, still after 15 epochs.
- Todo: (re)try with preprocessing.
- Todo: use learning rate scheduler.

### [v20.1] DeepLabV3+, resume training, adapted for GCP

Run on GCP.

Restart from contrails_2023-07-20_22-39-56.h5 (v20)

After 10 more epochs (total of 25):

- train dice_coef: 0.6032
- valid dice_coef: 0.3823 - not so much better then after 15 epochs (0.3614)

WIP

### [v25 = v21] U-Net: 15 epochs (history, auto threshold)

- First "Save and Run All" cancelled because of foreseeable exceeding of GPU quota.
- QuickSave -> **Submit -> Timeout**

### [v24] DeepLabV3+, 20 epochs for submission

QuickSave -> **Submit -> Timeout**

### [v26] U-Net: 10 epochs (TFRecords)

Run on Kaggle in 4h27.

**Benchmark against v11** with refactored notebook and TFRecords

- same number of model parameters
- same constant learning rate (0.1)
- v26 with TFRecords while v11 keras.Sequence

After 10 epochs:

- train dice_coef: 0.4980 vs previously 0.5028
- valid dice_coef: 0.3556 vs previously 0.4263 - not so good (why?)

Conclusion:

- reduced runtime per epoch: from 31 min to 23 min (-26%, less then expected)
- threshold optimization (0.3): 35.85% to 45.95% dice_coef

### [v26.1] DeepLabV3+, 10 epochs (TFRecords)

Run on GCP.

- DeepLabV3+: 250 ms per epoch thanks to TFRecords (at least 4x speedup!)
- U-Net: still 1 s per epoch

After 10 epochs:

- train dice_coef: 0.4458 
- valid dice_coef: 0.3228 - does not generalize as good as U-Net

Conclusion:

- **TFRecords** leads to **significant speedup** for DeepLabV3 model.
- But: **Why does a U-Net training step take so much longer than DeepLabV3?**
- **How can we make DeepLabV3 generalize better?

### [v27] U-Net, 10 epochs, for submission

Features: TFRecords, history, auto-threshold.

- QuickSave -> **Submit -> Timeout**

**Benchmarks against v11** of submission (see also v26)

WIP - Check running time on Kaggle submission hardware

### [v29 = v28] DeepLabV3, 10 epochs, for submission

Features: TFRecords, history, auto-threshold.

- QuickSave -> Submit -> Timeout
- "Save and Run All" in 01:02 -> Submit -> Successful

**Submission: 0.478** (threshold of 0.2)
