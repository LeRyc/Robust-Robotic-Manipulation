#!/bin/bash
PYTHONPATH=$PYTHONPATH:$PWD python ./experiments/run_pybulletgym.py --mode train -d ./experiment_results/obs_shift/td3_1 -c ./experiments/configs/train_conf_obs_shift.json
PYTHONPATH=$PYTHONPATH:$PWD python ./experiments/run_pybulletgym.py --mode train -d ./experiment_results/obs_shift/td3_2 -c ./experiments/configs/train_conf_obs_shift.json
PYTHONPATH=$PYTHONPATH:$PWD python ./experiments/run_pybulletgym.py --mode train -d ./experiment_results/obs_shift/td3_3 -c ./experiments/configs/train_conf_obs_shift.json
