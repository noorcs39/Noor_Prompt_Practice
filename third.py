import subprocess

data = """
Customer_ID,Latency,Jitter,Packet_Loss,Channel2_quality,Channel5_quality,N_distant_devices
1,9.26,3.56,0.00%,5,5,0
"""

conditions ="""
Here are conditions of these attributes:

Latency:
Latency is measured in milliseconds, and indicates the quality of your connection within your network. Anything at 100ms or less is considered acceptable. However, 20-40ms is optimal.

Jitter:
Lower jitter values (below 30ms) are best. Packet loss should be no more than 1%, and latency shouldn't exceed 150 ms one-way (300 ms return).

Packet Loss:
Losses between 5"%" and 10"%: of the total packet stream will affect the quality significantly." Another described less than 1% packet loss as "good" for streaming audio or video, and 1–2.5"%" as "acceptable".

Channel2_quality:
The Quality of the customer's 2.4GHz channel, rated on a scale of 1 to 5 by the modem


Channel5_quality:
The Quality of the customer's 5GHz channel, rated on a scale of 1 to 5 by the modem

N_distant_devices:
The Number of devices far from the modem (more than 10 m)

"""
# Define your question prompt using an f-string for proper formatting
prompt = f"""
Say Suppose you are working as network adminstrator and you are reading follwing {data} Real Dataset From Broadband Customers:

{data}

Here are conditions {conditions} of each paramter is defined:

{conditions}

Now your task is to review each Customer_ID with {data} and {conditions}, suggest which paramter represent fault or not.

Note: Answer should be like:
Customer_ID:
Latency:
Jitter:
Packet_Loss:
Channel2_quality:
Channel5_quality:
N_distant_devices:

As Network Adminstrator, can you read data and tell which attribute shows fault:
Answer can be like:
Latency: fault or not
"""

# Run the LLaMA model via Ollama
result = subprocess.run(
    ['ollama', 'run', 'llama3.1'],
    input=prompt,
    capture_output=True,
    text=True,
    encoding='utf-8'
)

# Get the response from the model
response = result.stdout.strip()

# Print the response
print(response)
