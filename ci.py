import wandb

print('The version of wandb is: {wandb.__version__}')
assert wandb.__version__ == '0.16.6', f'Expected version 0.16.6 but got {wandb.__version__}'
 
