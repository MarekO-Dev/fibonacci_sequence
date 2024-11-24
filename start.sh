#!/bin/bash

RED="\e[31m"
GREEN="\e[32m"
ENDCLR="\e[0m"

function clr_txt(){

    echo -e "$ENDCLR"
    echo -e "$1 $2 $ENDCLR"
}


python3 -m mypy src/fibonacci_sequence_copy
clr_txt $GREEN 'TYPE CHECK COMPLETE'
python3 -m pytest
clr_txt $GREEN 'PYTESTS COMPLETE'
python3 src
clr_txt $GREEN 'PROJECT RAN'