#!/bin/bash
file=$1
algo=$2
key=$3
c='CC'
cc='CC'
v='VC'
vc='VC'

if [[ $algo == $cc ]]
then
	python CC_Encrypt.py $key
elif [[ $algo == $vc ]]
then
	python VC_Encrypt.py $key
fi
