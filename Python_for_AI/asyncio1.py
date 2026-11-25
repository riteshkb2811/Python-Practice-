import asyncio


# async def fetch_data(delay,id):
#     print("Start fetching data for id: ",id)
#     await asyncio.sleep(delay)  # Simulating a network request
#     print("Data fetched successfully!")
#     return {"data": "Sample data"}

# async def main():
#     delay = 3  # Simulating a 3-second network delay
#     data1 = await fetch_data(delay, 1)  # Fetching data for id 1
#     data2 = await fetch_data(delay,2)  # Fetching data for id 2
#     print("Fetched data:", data1, data2)
#     print("All tasks completed.")

# asyncio.run(main())


#tasks
# async def fetch_data(delay, id):
#     print("Start fetching data for id: ", id)
#     await asyncio.sleep(delay)  # Simulating a network request
#     print("Data fetched successfully!")
#     return {"data": "Sample data"}      

# async def main():
#     delay = 3  # Simulating a 3-second network delay
#     task1 = asyncio.create_task(fetch_data(delay, 1))  # Creating a task for id 1
#     task2 = asyncio.create_task(fetch_data(delay, 2))  # Creating a task for id 2

#     data1 = await task1  # Awaiting the completion of task1
#     data2 = await task2  # Awaiting the completion of task2

#     print("Fetched data:", data1, data2)
#     print("All tasks completed.")

# asyncio.run(main())

#Gather in asycnio

# async def fetch_data(delay, id):
#     print("Start fetching data for id: ", id)
#     await asyncio.sleep(delay)  # Simulating a network request
#     print("Data fetched successfully!")
#     return {"data": "Sample data"}

# # async def main():
# #     delay =3
# #     data= await asyncio.gather(fetch_data(delay,1),fetch_data(delay,2),fetch_data(delay,3))
# #     for i in data:
# #      print("Fetched data:",i)
# #     print("All tasks completed.")


# async def main():
#     delay =3
#     task=[]
#     async with asyncio.TaskGroup() as tg:
#         for i in range(1,4):
#             t1=tg.create_task(fetch_data(delay,i))
#             task.append(t1)
#     result =[task.result() for task in task]
#     for i in result:
#         print("Fetched data:",i)

# asyncio.run(main())


# Future in asyncio
async def fet_res(delay, val, future):
    await asyncio.sleep(delay)
    future.set_result(val)
    print(f"Set the future result to: {val}")

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    delay = 3
    asyncio.create_task(fet_res(delay, "Future result is ready", future))
    res = await future
    print(f"Received the future result: {res}")

asyncio.run(main())