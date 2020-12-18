#!/bin/bash
start=`date +%s%N`
file=$1
algo=$2
key=$3
c='CC'
cc='CC'
v='VC'
vc='VC'

if [[ $algo == $cc ]]
then
        python CC_Decrypt.py $key
elif [[ $algo == $vc ]]
then
        python VC_Decrpyt.py $key
fi
end=`date +%s.%N`
