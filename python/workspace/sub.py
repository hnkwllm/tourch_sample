import torch
import torch.distributed as dist
import os

def test_gpus(rank, world_size):
    # Initialize the process group
    dist.init_process_group("gloo", rank=rank, world_size=world_size)

    # Check if GPUs are available
    if torch.cuda.is_available():
        device_count = torch.cuda.device_count()
        device_names = [torch.cuda.get_device_name(i) for i in range(device_count)]
        print(f"Rank {rank}: {device_count} GPU(s) detected: {device_names}")
    else:
        print(f"Rank {rank}: No GPU available.")

    # Synchronize processes
    dist.barrier()
    
    # Clean up
    dist.destroy_process_group()

def main():
    # Environment variables should be set manually for each machine
    rank = int(os.environ["RANK"])  # This process's rank
    world_size = int(os.environ["WORLD_SIZE"])  # Total number of processes

    print(f"Initializing process on Rank {rank} out of {world_size}")
    test_gpus(rank, world_size)

if __name__ == "__main__":
    # Set these variables manually or through the environment
    os.environ["MASTER_ADDR"] = "192.168.1.100"  # Replace with the master node's IP
    os.environ["MASTER_PORT"] = "29500"  # Replace with an available port
    os.environ["WORLD_SIZE"] = "2"  # Total number of processes (machines)
    os.environ["RANK"] = os.getenv("RANK", "0")  # Default to 0 for master

    main()
