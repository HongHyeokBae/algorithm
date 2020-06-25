

def solution(lines):
    """
    type lines: List[str]
    rtype: int
    """
    start_times, end_times = [], []
    
    for line in lines:
        splited = line.split(' ')
        end_time = timeToMills(splited[1])
        process = 1000 * float(splited[2][:-1])

        end_times.append(int(end_time))
        start_times.append(int(end_time - process + 1))

    answer = 0
    for i in range(len(end_times)):
        end = end_times[i]
        curr = 0
        for j in range(i, len(end_times)):
            if (end_times[j] < end + 1000) or (start_times[j] < end + 1000):
                curr += 1

        answer = max(answer, curr)

    return answer

def timeToMills(time):
    h, m, s = time.split(':')
    mills = (int(h) * 3600 + int(m) * 60 + float(s)) * 1000

    return mills