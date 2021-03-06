# Robust Learning and Control for Robotic Tasks

---

### Evaluating the robustness of learned control policies for robotic tasks:

The agent is designed according to the standard robotics paradigm Sense-Plan-Act. In this project the Sense and Act
modules are utilized for assessing the planner's robustness against noise and domain shift in observations as well as
during the execution of actions.

---

### How to start:

#### Requirements
* Python 3.6+
* PyTorch 1.0+
* [PyBullet Gymperium](https://github.com/benelot/pybullet-gym), an open-source implementation of the OpenAI Gym MuJoCo

#### Installation:
Create a virtual python environment and install  all requirements with `bash install.sh`. This will also clone and install PyBullet in ./environments/pybulletgym.
(The requirements can alternatively be installed separately with `pip3 install -r requirements.txt`)

#### Run experiments

There are three ways to run the agents:
* __Train__ the agent on an environment.
* __Evaluate__ the agent on an environment.
* __Test__ the agent's generalization capabilities on an environment with different observers and executers.

Experiments for a particular environment can be run using the following command and a config file (`./experiments/configs/exp01.json`) where the experiment paramters are defined.

```
bash run_experiment_train.sh

-m    --mode          Set 'train', 'eval' or 'test' for training, evaluation, or testing generalization respectively
-l    --logging       Select logging level. "info" for  basic output; "debug" for debugging purposes. (default 'info')
-c    --config        Experiment config file. (E.g '/Robust-Robotic-Manipulation/experiments/configs/train_config.json')
-d    --directory     The model and experiment output directory. (E.g.: './experiment_results')
```

---

### Project Overview
#### Agents
* __[TD3](https://arxiv.org/pdf/1802.09477.pdf)__: (successor of DDPG) a state of the art model-free reinforcement learning algorithm for continuous control problems.
 The TD3 focuses on reducing the overestimation bias seen from the DDPG and similar algorithms by:
    * Using a pair of critic networks
    * Delayed updates of the actor
    * Action noise regularisation
    
  As a result the TD3 training should be more stable and less reliant on finding the correct hyper parameters for the current task,
  because it does not continuously over estimates the Q values of the critic (value) network. 
  Otherwise, these estimation errors build up over time and can lead to the agent falling into a local optima 
  or experience catastrophic forgetting. 

#### Observer and Executer
The generalization capabilities of an agent are systematically evaluated, as described in the following schematic.

<img src="https://github.com/LeRyc/Robust-Robotic-Manipulation/blob/master/img/im1.png" height="400">


Therefore, different observer and execution modules are available which can be activated and deactivated as needed. Currently, for both, the observer and the executer, a module for adding noise and for simulating domain shift are implemented and can be futher modified.

<img src="https://github.com/LeRyc/Robust-Robotic-Manipulation/blob/master/img/im3.png" height="250">

#### [Results](https://github.com/LeRyc/Robust-Robotic-Manipulation/blob/master/experiment_results/README.md)
