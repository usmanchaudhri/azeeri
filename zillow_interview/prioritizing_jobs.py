"""
prioritize jobs
"""
from collections import defaultdict

"""
#  {0: [None, None, 2], 1: [None, 1, 2], 2: [None, None, None]}
"""
def get_jobs(jobs):
    pjobs = defaultdict(list)
    for i in range(len(jobs)):
        for j in range(len(jobs[0])):
            if jobs[i][j]:
                pjobs[i].append(j)

        if i not in pjobs:
            pjobs[i].append(None)

    job_order = dfs(pjobs)
    print(job_order)

def dfs(pjobs):
    """
    :param pjobs: adjacency's list
    :return:
    """

    # mark all vertex as not visited.
    job_order = []
    visited = []
    count = sum([len(i) for i in pjobs.values()])
    visited = [False for i in range(count)]

    for jobs in pjobs:
        if not visited[jobs]:
            res = dfs_util(jobs, visited, pjobs)
            job_order = job_order + res

    return job_order

def dfs_util(job, visited, pjobs):
    """
    s - the current vertex
    visited - the visited array
    """
    stack = []
    priority = []

    # push the current node to the stack
    stack.append(job)
    while len(stack) != 0:
        # pop the vertex from the stack and print it
        job = stack.pop()

        # stack may contain the same vertex twice
        # so we need to check the pop item only
        if not visited[job]:
            priority.append(job)
            # print(job, end=" ")
            visited[job] = True

        # get all adjacent vertices of the popped
        # vertex s. If a adjacent has not been visited
        # then push it to the stack
        for adjacent_job in pjobs[job]:
            if adjacent_job is None:
                break

            if not visited[adjacent_job]:
                stack.append(adjacent_job)

    priority.reverse()
    return priority


if __name__ == "__main__":
    jobs = [[0,0,1],
            [1,0,1],
            [0,0,0]]
    get_jobs(jobs)

    # a = {}
    # a[1] = [1,2,3]
    # a[2] = [2,3,4]
    # l = a[1]
    # for i in l:
    #     print(i)


