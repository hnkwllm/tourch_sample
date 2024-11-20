import torch
import torch.distributed as dist
import torch.multiprocessing as mp
import os

def test_gpus(rank, world_size):
    # Initialize the process group
    dist.init_process_group("gloo", rank=rank, world_size=world_size)
    
    # Print GPU availability and rank info
    if torch.cuda.is_available():
        device = f"cuda:{rank}"
        print(f"Rank {rank}: GPU {torch.cuda.get_device_name(rank)} is available.")
    else:
        print(f"Rank {rank}: No GPU available.")
    
    # Clean up
    dist.destroy_process_group()

def main():
    world_size = torch.cuda.device_count()
    if world_size == 0:
        print("No GPUs detected. Exiting.")
        return

    print(f"Number of GPUs detected: {world_size}")
    mp.spawn(test_gpus,
             args=(world_size,),
             nprocs=world_size,
             join=True)

if __name__ == "__main__":
    os.environ["MASTER_ADDR"] = "192.168.12.167"
    os.environ["MASTER_PORT"] = "29500"
    main()
