### Debugging
```
HYDRA_FULL_ERROR=1 HABITAT_ENV_DEBUG=1 MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet \
  python habitat-baselines/habitat_baselines/run.py -m \
  --config-name experiments_hab3/socialnav_human_robot_floorplanner.yaml \
  habitat_baselines.num_environments=32 \
  habitat_baselines.torch_gpu_id=1


  "~habitat.task.actions.agent_0_rearrange_stop" \
  "~habitat.task.actions.agent_0_pddl_apply_action" \
  "~habitat.task.actions.agent_0_oracle_nav_with_backing_up_action"
```

### Evaluating oracle policy
```
HYDRA_FULL_ERROR=1 HABITAT_ENV_DEBUG=1 MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet \
  python habitat-baselines/habitat_baselines/run.py -m \
  --config-name experiments_hab3/socialnav_human_robot_oracle.yaml \
  habitat_baselines.num_environments=1 \
  habitat_baselines.evaluate=True \
  habitat_baselines.eval.should_load_ckpt=False \
  habitat_baselines.test_episode_count=5
```

### Training
Training parameters in `submitit_habitat.yaml`
```
MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet \
  python habitat-baselines/habitat_baselines/run.py -m \
  --config-name experiments_hab3/socialnav_human_robot_floorplanner.yaml \
  habitat_baselines.num_environments=32 \
  hydra/launcher=submitit_habitat
```

### Evaluation
```
HYDRA_FULL_ERROR=1 HABITAT_ENV_DEBUG=1 MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet \
  python habitat-baselines/habitat_baselines/run.py -m \
  --config-name experiments_hab3/socialnav_human_robot_floorplanner.yaml \
  habitat_baselines.video_dir=../videos/eval \
  habitat_baselines.num_environments=10 \
  habitat_baselines.test_episode_count=10 \
  habitat_baselines.evaluate=True
```
