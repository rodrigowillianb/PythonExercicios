from time import sleep
import time

for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)

print("🎉 BOOOOOM! 🎉")

fogos = ["🎆", "🎇", "✨", "💥", "🌟", "🧨"]

for _ in range(10):
    print("  ".join(fogos))
    time.sleep(0.5)


