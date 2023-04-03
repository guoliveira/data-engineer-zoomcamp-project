import os
import psutil
 
# inner psutil function
def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def process_cpu():
    """
    Getting cpu_percent in last 0 and 1 seconds
    """
    cpu_usage = psutil.cpu_percent(2)
    return cpu_usage
 
# decorator function
def profile_mem(func):
    def wrapper(*args, **kwargs):
 
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("Consumed memory: {:,}".format(
            mem_before, mem_after, mem_after - mem_before))
 
        return result
    return wrapper

# decorator function
def profile_cpu(func):
    def wrapper(*args, **kwargs):
 
        
        result = func(*args, **kwargs)
        cpu_before = process_cpu()
        print(f"Consumed cpu: {cpu_before}")
            
 
        return result
    return wrapper