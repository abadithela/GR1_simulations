from rb import runner
import random 

runner_ctrl = runner()
blocker_st = 2

runner_u = runner_ctrl.move(blocker_st)
runner_st = runner_u["r"]
time = 1
print("Time: ", str(time), " Blocker: ", str(blocker_st), " Runner: ", str(runner_st))

while runner_st != 4:
    if blocker_st == 2:
        if runner_st == 2:
            next_blocker_st = 1
            print("Collision!")
        elif runner_st == 3:
            next_blocker_st = 3
            print("Collision!")
        else:
            next_blocker_st = random.choice([1,3])
    elif blocker_st == 1:
        next_blocker_st = 2
    elif blocker_st == 3:
        next_blocker_st = 2
    else:
        assert blocker_st not in [1,2,3]

    
    runner_u = runner_ctrl.move(next_blocker_st)
    next_runner_st = runner_u["r"]
    time = time + 1
    print("Time:", str(time), " Blocker:", str(next_blocker_st), " Runner:", str(next_runner_st))

    blocker_st = next_blocker_st
    runner_st = next_runner_st
    


