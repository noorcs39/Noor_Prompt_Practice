import subprocess

# Define the data for multiple customers
data = """
Customer_ID,Latency,Jitter,Packet_Loss,Channel2_quality,Channel5_quality,N_distant_devices
1,9.26,3.56,0.00%,5,5,0
2,6.62,3.51,0.00%,5,5,1
"""

# Split the data into lines and parse the headers
lines = data.strip().split('\n')
headers = lines[0].split(',')

# Initialize a list to store summaries for each customer
summaries = []

# Iterate over each customer's data (starting from the second line)
for line in lines[1:]:
    values = line.split(',')
    
    # Create a dictionary to map headers to their corresponding values
    data_dict = {header: value for header, value in zip(headers, values)}
    
    # Convert necessary values to floats for comparison
    jitter_value = float(data_dict['Jitter'])
    latency_value = float(data_dict['Latency'])
    packet_loss_value = float(data_dict['Packet_Loss'].strip('%')) / 100  # Convert percentage to a decimal
    channel2_quality_value = float(data_dict['Channel2_quality'])
    channel5_quality_value = float(data_dict['Channel5_quality'])
    n_distant_devices_value = float(data_dict['N_distant_devices'])
    
    # Evaluate each condition
    faults = []
    if jitter_value > 3.37:
        faults.append("Jitter > 3.37 ms")
    if latency_value > 10:
        faults.append("Latency > 10 ms")
    if packet_loss_value > 0.0037:
        faults.append("Packet Loss > 0.37%")
    if channel2_quality_value > 3.89:
        faults.append("Channel 2 Quality > 3.89")
    if channel5_quality_value > 4.52:
        faults.append("Channel 5 Quality > 4.52")
    if n_distant_devices_value > 1.79:
        faults.append("N_distant_devices > 1.79")
    
    # Determine the fault status
    fault_status = "Faults Detected: " + ", ".join(faults) if faults else "No Faults"
    
    # Create a concise summary for the current customer
    summary = f"""
    Customer ID: {data_dict['Customer_ID']}
    Fault Status: {fault_status}
    Data: Latency: {data_dict['Latency']} ms, Jitter: {data_dict['Jitter']} ms, Packet Loss: {data_dict['Packet_Loss']}, Channel2_quality: {data_dict['Channel2_quality']}, Channel5_quality: {data_dict['Channel5_quality']}, N_distant_devices: {data_dict['N_distant_devices']}
    """
    summaries.append(summary.strip())

# Combine all summaries into one prompt
prompt = f"""
As a network admin, analyze the following data for each customer and determine fault status. Provide a concise summary for each:

{''.join(summaries)}
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
