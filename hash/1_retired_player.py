def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(0, len(participant)):
        if i >= len(completion):
            return participant[-1]
        
        if not participant[i] == completion[i]:
            return participant[i]