def solution(sizes):
    width, height = [], []
    
    for arr in sizes:
        width.append(max(arr))
        height.append(min(arr))

    return max(width) * max(height)