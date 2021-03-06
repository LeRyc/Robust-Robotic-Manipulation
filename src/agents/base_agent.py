from abc import ABCMeta, abstractmethod

from src.executer.base_executer import BaseExecuter
from src.observer.base_observer import BaseObserver

class BaseAgent(metaclass=ABCMeta):
  """This agent implements the Sense-Plan-Act architecture."""

  def __init__(self,
               observation_space,
               action_space,
               observer=None,
               executer=None):
    # TODO: add action_space and check if given action limits do not exceed the action_space
    self.observer = observer or BaseObserver(observation_space=observation_space)
    self.executer = executer or BaseExecuter(action_space=action_space)

  def sense(self, state):
    """
    Add variability to the state based on the observation module.

    :param state:
      The environment's current state.

    :return obs:
      The state observation.
    """
    obs  = self.observer(state)
    return obs

  @abstractmethod
  def plan(self, obs, prev_obs=None, prev_action=None):
    """
    Choose a next action given a observation of the environment.

    :param obs:
      A observation of the environment at the current time step.
      The observation is an altered stated produced by the observer.
    :param prev_obs:
      The observation of the environment at the previous time step.
    :param prev_oactions:
      The observation of the environment at the previous time step.

    :return action:
      Next action to be executed by the agent.
    """
    raise NotImplementedError

  def act(self, action):
    """
    Add variability to the action based on the executer module.

    :param action:
      The action chosen by the agent.

    :return control_action:
      The actual action that is executed.
    """
    control_action = self.executer(action)
    return control_action

  def run(self, state):
    """
    Run the agent sense-plan-act pipeline.

    :param state:
      The current state of the environment.

    :return control_action:
      Return the action that is next executed.
    """
    obs = self.sense(state)
    action = self.plan(obs)
    control_action = self.act(action)
    return control_action


class RandomAgent(BaseAgent):
  """This agent implements the Sense-Plan-Act architecture."""

  def __init__(self,
               observation_space,
               action_space,
               observer=None,
               executer=None):
    super(RandomAgent, self).__init__(observation_space=observation_space,
                                      action_space=action_space)
    self.action_space = action_space
    self.observer = observer
    self.executer = executer

  def plan(self, obs=None):
    action = self.action_space.sample()
    return action
