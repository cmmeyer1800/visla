

def str_to_tuple(str_rep: str, length: int) -> tuple:
    try:
        ret = tuple(int(x) for x in str_rep[1:-1].split(','))
        assert len(ret) == length
        assert type(ret) == tuple
        for i in range(length):
            assert type(ret[i]) == int

    except:
        return None

    return ret