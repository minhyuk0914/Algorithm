def solution(video_len, pos, op_start, op_end, commands):
    pos_list = list(map(int, pos.split(':')))
    pos_times = pos_list[0] * 60 + pos_list[1]
    video_len_list = list(map(int, video_len.split(':')))
    video_len_times = video_len_list[0] * 60 + video_len_list[1]
    op_start_list = list(map(int, op_start.split(':')))
    op_start_times = op_start_list[0] * 60 + op_start_list[1]
    op_end_list = list(map(int, op_end.split(':')))
    op_end_times = op_end_list[0] * 60 + op_end_list[1]
    
    for idx in range(len(commands)):
        if commands[idx] == 'next':
            commands[idx] = 10
        else:
            commands[idx] = -10
        
    for command in commands:
        if op_start_times <= pos_times <= op_end_times:
            pos_times = op_end_times
        
        if pos_times + command <= 0:
            print('0보다 작은 경우')
            pos_times = 0
        elif pos_times + command >= video_len_times:
            print('비디오 길이 넘은 경우')
            pos_times = video_len_times
        else:
            print('커맨드 정상')
            pos_times += command
            
    if op_start_times <= pos_times <= op_end_times:
        answer = op_end
    else:
        print(pos_times)
        answer = f"{str(pos_times // 60).zfill(2)}:{str(pos_times % 60).zfill(2)}"

    return answer