def concatenate_kwaargs(*syt):
    answer=""
    for str in syt:
        answer += str
    return answer    


def concatenate_kwargs(**str):
    answer=""
    for stm in str.values():
        answer+=stm
    return answer    
