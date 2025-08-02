import asyncio
import time
import logging

logging.basicConfig(filename="logs.txt",level=logging.INFO,format="%(asctime)s - %(message)s")

def logExecutionTime(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        logging.info(f"Task {func} started.")
        result = await func(*args, **kwargs)
        end = time.time()
        timeTaken = end - start
        logging.info(f"Task {func} finished in {timeTaken} seconds.")
        return result
    return wrapper

@logExecutionTime
async def fetchingData(taskID):
    await asyncio.sleep(2) 
    logging.info(f"Downloaded data for task {taskID}")

@logExecutionTime
async def fileProcessing(taskID):
    await asyncio.sleep(3) 
    logging.info(f"Processed file for task {taskID}")

@logExecutionTime
async def logWriting(taskID):
    await asyncio.sleep(1)
    logging.info(f"Wrote logs for task {taskID}")