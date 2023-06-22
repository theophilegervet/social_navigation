### Debugging
```
HYDRA_FULL_ERROR=1 HABITAT_ENV_DEBUG=1 MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet \
  python habitat-baselines/habitat_baselines/run.py -m \
  --config-name experiments_hab3/socialnav_human_robot_floorplanner.yaml \
  habitat_baselines.num_environments=5 \
  habitat_baselines.torch_gpu_id=1

TORCH_DISTRIBUTED_DEBUG=DETAIL NCCL_DEBUG=INFO CUDA_LAUNCH_BLOCKING=1 \
  HYDRA_FULL_ERROR=1 HABITAT_ENV_DEBUG=1 MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet \
  torchrun --nproc_per_node 8 habitat-baselines/habitat_baselines/run.py -m \
  --config-name experiments_hab3/socialnav_human_robot_floorplanner.yaml \
  habitat_baselines.num_environments=5 \
  habitat_baselines.rl.ddppo.distrib_backend=GLOO
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
  habitat_baselines.num_environments=5 \
  hydra/launcher=submitit_habitat_8
```

### Evaluation
```
HYDRA_FULL_ERROR=1 HABITAT_ENV_DEBUG=1 MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet \
  python habitat-baselines/habitat_baselines/run.py -m \
  --config-name experiments_hab3/socialnav_human_robot_floorplanner.yaml \
  habitat_baselines.video_dir=../videos/eval \
  habitat_baselines.num_environments=5 \
  habitat_baselines.test_episode_count=5 \
  habitat_baselines.evaluate=True
```
