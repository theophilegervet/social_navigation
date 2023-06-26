To test multi-GPU multi-env:
```
TORCH_DISTRIBUTED_DEBUG=DETAIL NCCL_DEBUG=INFO CUDA_LAUNCH_BLOCKING=1 \
  HYDRA_FULL_ERROR=1 HABITAT_ENV_DEBUG=1 MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet \
  torchrun --nproc_per_node 2 habitat-baselines/habitat_baselines/run.py -m \
  --config-name experiments_hab3/pop_play_kinematic_oracle_humanoid_spot_fp.yaml \
  habitat_baselines.writer_type=wb \
  habitat_baselines.num_environments=2

HYDRA_FULL_ERROR=1 HABITAT_ENV_DEBUG=1 MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet \
  python habitat-baselines/habitat_baselines/run.py -m \
  --config-name experiments_hab3/pop_play_kinematic_oracle_humanoid_spot_fp.yaml \
  habitat_baselines.writer_type=wb \
  habitat_baselines.num_environments=1

HYDRA_FULL_ERROR=1 HABITAT_ENV_DEBUG=1 MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet \
  python habitat-baselines/habitat_baselines/run.py -m \
  --config-name experiments_hab3/pop_play_kinematic_oracle_humanoid_spot_fp.yaml \
  habitat_baselines.video_dir=../videos/eval \
  habitat_baselines.num_environments=1 \
  habitat_baselines.test_episode_count=5 \
  habitat_baselines.evaluate=True
```

To train social nav:
```
TORCH_DISTRIBUTED_DEBUG=DETAIL NCCL_DEBUG=INFO CUDA_LAUNCH_BLOCKING=1 \
  HYDRA_FULL_ERROR=1 HABITAT_ENV_DEBUG=1 MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet \
  torchrun --nproc_per_node 2 habitat-baselines/habitat_baselines/run.py -m \
  --config-name experiments_hab3/pop_play_kinematic_oracle_humanoid_spot_fp_socialnav.yaml \
  habitat_baselines.writer_type=wb \
  habitat_baselines.num_environments=2

HYDRA_FULL_ERROR=1 HABITAT_ENV_DEBUG=1 MAGNUM_LOG=quiet HABITAT_SIM_LOG=quiet \
  python habitat-baselines/habitat_baselines/run.py -m \
  --config-name experiments_hab3/pop_play_kinematic_oracle_humanoid_spot_fp_socialnav.yaml \
  habitat_baselines.writer_type=wb \
  habitat_baselines.num_environments=1
```