import subprocess

# Points to your extracted Kafka folder
KAFKA_ROOT = r"C:\kafka"
CMD = r"bin\windows\kafka-server-start.bat config\kraft\server.properties"

try:
    print("🚀 Starting Kafka Broker...")
    # cwd=KAFKA_ROOT is crucial so it finds the config file
    process = subprocess.Popen(CMD, cwd=KAFKA_ROOT, shell=True)
    process.wait() # Keeps the script running
except KeyboardInterrupt:
    print("\n🛑 Stopping...")
    process.terminate()
