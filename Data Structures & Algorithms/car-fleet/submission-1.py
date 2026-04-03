class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            cars.append((p, s))
        cars.sort()

        stack = [] # time
        for p, s in reversed(cars):
            stack.append((target-p) / s)
            # if the latter takes less time than the former,
            # it merges into the former
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)