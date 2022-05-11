from art import logo

def track_pace_calculator(distance, target_minutes, target_seconds):
    full_rounds = distance // 400
    excess_parts = (distance % 400) / 400
    total_rounds = full_rounds + excess_parts
    total_timing = target_minutes * 60 + target_seconds
    addition = "0"

    pace_per_round = total_timing / total_rounds
    elapsed_time = 0
    for i in range(full_rounds):
        elapsed_time += pace_per_round
        if view_selection == "default":
            print(f"{int(elapsed_time // 60)} minutes & {int(elapsed_time % 60)} seconds")
        else:
            print(f"{int(elapsed_time // 60)}:{int(elapsed_time % 60) if len(str(int(elapsed_time % 60))) > 1 else addition + str(int(elapsed_time % 60))}")
    if excess_parts == 0:
        return
    elapsed_time += (pace_per_round * excess_parts)
    if view_selection == "default":
        print(f"{int(elapsed_time // 60)} minutes & {int(elapsed_time % 60)} seconds")
    else:
        print(f"{int(elapsed_time // 60)}:{int(elapsed_time % 60) if len(str(int(elapsed_time % 60))) > 1 else addition + str(int(elapsed_time % 60))}")

print(logo)
distance = int(input("What track distance are you attempting in metres?\n"))
minutes = int(input("How many minutes are you aiming for?\n"))
seconds = int(input("How many seconds are you aiming for?\n"))
view_selection = "default"
view_selection = input("Which view would you like? (default/minimal)\n")

track_pace_calculator(distance, minutes, seconds)
print("\n\n Jiayous for your goal towards a new PB!")
        
    
