import random

prisoners = 100
iterations = 10000

#stats
success = 0
fail = 0

for iteration in range(1, iterations+1):
    # populate boxes with slips
    slips = list(range(1, prisoners+1))
    random.shuffle(slips)
    boxes = {}
    for i in range(1, prisoners+1):
        boxes[i] = slips.pop()
    
    assert len(slips) == 0 # slips have all been put into boxes
    
    iteration_success = True
    chances = prisoners / 2 # Each prisoner can open (number of prisoners)/2 boxes
    assert chances.is_integer()
    chances = int(chances)
    
    for i in range(1, prisoners+1):
        # print(f"Prisoner {i} is opening boxes")
        opened_boxes = set()
        prisoner_success = False
        
        for _ in range(chances):
            next_box_to_open = random.choice(list(set(boxes) - opened_boxes))
            opened_boxes.add(next_box_to_open)
            slip = boxes[next_box_to_open]
            if slip == i:
                # print(f"prisoner {i} found slip {i} in box {next_box_to_open}")
                prisoner_success = True
                break
            
        if not prisoner_success:
            #print(f"prisoner {i} failed to find their number in boxes.")
            iteration_success = False
            break
            
    if iteration_success:
        #print(f"Iteration {iteration} succeded.")
        success += 1
    else:
        #print(f"Iteration {iteration} failed.")
        fail += 1

print(f"Out of {iterations} iterations, {success} attempts succeded, {fail} attempts failed.")