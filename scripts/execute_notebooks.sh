#!/bin/bash

NOTEBOOKS=$*

for NB in $NOTEBOOKS; do
    NAME=${NB%.ipynb}
    if [[ ! -e ${NAME}.ipynb ]]; then
        echo "${NAME}.ipynb not found"
        exit 1
    fi
    jupyter nbconvert --to notebook \
    --execute ~/kaggle/working/${NAME}.ipynb \
    --output ~/kaggle/working/${NAME}_executed.ipynb
done
