
# Saved Notebooks

Text dumps of the notebooks' "Save and Run All" versions. 

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

Conclusion:

- Training resnet50 weights works.
- Linear learning in terms of dice_coef, still after 15 epochs.
- Todo: (re)try with preprocessing.
- Todo: use learning rate scheduler.

### [v20.1] DeepLabV3+, resume training, adapted for GCP

WIP

### [v21] U-Net: 15 epochs (history, auto threshold)

WIP
