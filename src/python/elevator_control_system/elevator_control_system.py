"""
Elevator control system

The elevator is called from a floor and has a goal.
10
9
8   - Goal  - Goal
7
6
5   - 1st Call
4
3   - 2nd Call
2
1   - E
"""
from heapq import heappush, heappop

class Elevator:
    def __init__(self, id):
        self.id = id
        self.goal = 0
        self.floor = 0
        self.requestQueue = []      # a priority queue
        self.direction = 1

    def status(self):
        return (self.id, self.floor, self.goal)

    def step(self):
        # the elevator moves one step towards it's destination
        if not self.requestQueue:
            return
        self.floor += self.direction
        if self.floor == self.goal:
            # the elevator has reached the goal and so
            # the value will be popped out.
            heappop(self.requestQueue)
            if self.requestQueue:
                # set a new goal which is going to be the next element in the priority queue
                self.goal = self.direction * self.requestQueue[0]

    def update(self, floor, goal):
        """ clears the state of the elevator """
        self.floor = floor
        self.goal = goal
        self.direction = 1 if self.floor < self.goal else -1
        self.requestQueue = []
        self.addRequest(floor, goal)

    def getPendingRequestCount(self):
        return len(self.requestQueue)

    def addRequest(self, floor, goal):
        """ adds a new request to the elevator's queue
            - each elevator call request will have a floor where the elevator request came from and a goal
                which is the destination it is going too.
            - add goal to the elevator's priority queue
            - add the floor to the elevator's priority queue, only if the elevator is not called from current
                floor
            - check if the current goal of the elevator is the smallest number in the priority queue.
        """
        # check if this is the first request
        if len(self.requestQueue) == 0:
            self.direction = 1 if floor < goal else -1
            self.goal = goal * self.direction

        # update the queue with the goal request
        # the goal will be set as + if the elevator is going up or
        # - if the elevator is going down
        newGoal = goal * self.direction
        if newGoal not in self.requestQueue:

            # will act like a priority queue, elevator to the nearest floor
            # will be called.
            heappush(self.requestQueue, newGoal)

        # update the queue with the floor request
        newFloor = floor * self.direction
        if self.floor != floor and newFloor not in self.requestQueue:
            heappush(self.requestQueue, newFloor)

        # update the goal and if a smaller one exists
        # this is to make sure that the Elevator stops
        # at the floor which comes first
        if self.requestQueue[0] < (self.direction * self.goal):
            self.goal = self.direction * self.requestQueue[0]


from collections import deque

class ElevatorControlSystem:
    def __init__(self, floors=100, elevator_count=16):
        self.floors = floors
        self.elevator_count = elevator_count
        self.elevators = [Elevator(i) for i in range(self.elevator_count)]
        self.tobeAssigned = deque()

    def status(self):
        return [e.getStatus() for e in range(self.elevators)]

    def step(self):
        """ steps to the simulation one step at a time  """
        for e in self.elevators:
            e.step()

        if self.tobeAssigned: # if there are pending
            floor, destination = self.tobeAssigned[0]

            # start search the closest free elevator
            availableElevators = []
            for e in self.elevators:
                if e.getPendingRequestCount() == 0:
                    # subtract the floor at which the elevator is at with the
                    # floor from where it was called
                    diff = abs(e.floor - floor)
                    availableElevators.append((diff, e))

            if availableElevators:
                _, e = min(availableElevators)
                self.tobeAssigned.popleft()
                e.addRequest(floor, destination)

    def update(self, id, floor, goal):
        """ clears the state of the elevator with id - id and updates its
            state with new values
        """
        e = self.elevators[id]
        e.update(floor, goal)

    def pickup(self, floor, destination, direction):
        """ handles a pickup request from the client. Works by searching the closest elevator
            that is going in the same direction and then finding the closes one among them.
            In case, no elevators are found, the request is added to a FIFO queue to be handle later by
            a free elevator
        """
        # find elevators which have the same direction as the input direction
        elevators = [e for e in self.elevators if e.direction == direction]

        candidates = []
        for e in elevators:
            # find the closest elevator
            diff = direction * (floor - e.floor)
            if diff >= 0:
                candidates.append((diff, e.id))

            if candidates:
                _, id = min(candidates)
                e = self.elevators[id]
                e.addRequest(floor, destination)
            else:
                self.tobeAssigned.append((floor, destination))


elevator = Elevator(1)
elevator.addRequest(6, 8)
elevator.addRequest(1, 5)
elevator.addRequest(1, 3)

# if __name__ == "__main__":
#
#     q = []
#     heappush(q, 10)
#     heappush(q, 11)
#     heappush(q, 9)
#     heappush(q, 6)
#     heappush(q, 2)
#
#     while len(q):
#         print(heappop(q))