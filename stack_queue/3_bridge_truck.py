def solution(bridge_length, weight, truck_weights):
    time = []
    times = 0
    finished = []
    running = []

    while True:
        time = list(map(lambda x: x+1, time))
        times = times + 1
        checked = []
        for i in range(0, len(time)):
            if time[i] >= bridge_length:
                checked.append(i)

        for check in checked:
            finished.append(running[check])
            del time[check]
            del running[check]

        if len(truck_weights)>0 and sum(running)+truck_weights[0] <= weight:
            running.append(truck_weights[0])
            time.append(0)
            del truck_weights[0]

        if not truck_weights and not running:
            break;

    return times

# solution(2, 10, [7,4,5,6])
# solution(100,100,[10])
# solution(100,100,[10,10,10,10,10,10,10,10,10,10])
