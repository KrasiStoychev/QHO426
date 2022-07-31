def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  dirs = directions()
  for i in range(len(dirs)):
    print(f"{i}: {dirs[i]}")
  i = int(input())
  return dirs[i]

def run():
  route = []
  print("Working out escape route...")
  for i in range(5):
    route.append(menu())
  print(f"Escape route: {route}")

run()