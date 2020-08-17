"""
Given the index of the desired tool in the tools, determines the minimum number of forward or backward moves needed to reach a certain tool

Example:
tools: [‘ballendmill’, ‘keywaycutter’, ‘slotdrill’, ‘facemill’]
k=1
tool=’ballenmill’

The tool currently in use is ‘keywaycutter’ at index 1. The desired tool is ‘ballendmill’ at index 0. It can be reached by moving forward
3 times or backward 1 time. The minimum number of moves is 1.
"""
# def findDesiredTool(tools, k, desiredTool):
#     # either we move forward or backwards in the array
#     # we also have to find which tool isballendmill closer
#     # is there a way we can re-arrange the array to
#     i = k
#     while True:
#         if tools[i % len(tools)] == desiredTool:
#             print(tools[i % len(tools)])
#             print("no of steps : ", i)
#             return True
#         i=i+1

def findDesiredTool(tools, startIdx, target, step):
    if tools[step % len(tools)] == target:
        return abs(step-1)


    forward = findDesiredTool(tools, startIdx, target, step+1)
    step = startIdx    # reset to the startIdx and now go backwards
    backwards = findDesiredTool(tools, startIdx, target, step-1)

    return min(forward, backwards)

if __name__  == "__main__":
    tools = ["ballendmill", "hammer", "keywaycutter", "slotdrill", "facemill", "nail", "drill"]
    k = 2
    target = "ballendmill"
    minNumSteps = findDesiredTool(tools, k, target, step=k)
    print(minNumSteps)
    # print(1%4)
    # tools.sort()
    # print(tools)
    # tools.sort(key = lambda x: len(x))
    # print(tools)

