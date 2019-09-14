def solution(phone_book):
    for i in range(0, len(phone_book)):
        for j in range(0, i+1):
            if i==j:
                continue
            
            if phone_book[j].startswith(phone_book[i]) or \
            phone_book[i].startswith(phone_book[j]):
                return False

    return True