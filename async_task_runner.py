import asyncio
from tasks import fetchingData, fileProcessing, logWriting

async def task(name, queue):
    while not queue.empty():
        func, taskID = await queue.get()
        await func(taskID)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    for i in range(5):
        await queue.put((fetchingData, i))
        await queue.put((fileProcessing, i))
        await queue.put((logWriting, i))

    tasks = []
    for i in range(3):  # Number of workers
        tasks.append(asyncio.create_task(task(f"Worker-{i+1}", queue)))

    await asyncio.gather(*tasks)
    print("All tasks completed.")
    

if __name__ == "__main__":
    asyncio.run(main())