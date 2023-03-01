import sys

# "what is the shortest burst time that we can currently see?"
def shortestRemainingSort(batchFileData): # PID, Arrival Time, Burst Time
    completionTimes, arrivalTimes, burstTimes = [], [], [] # completion acts as an auxillary array at first until calculated.
    orderOfExecution, arrivalQueue, processes = [], [], {} # arrivalQueue contains pids that we can see
    current_time = 0
    
    for row in batchFileData: # fill arrival and burst arrays (req'd data)
        pid, arrivalTime, burstTime = row[0], row[1], row[2]
        arrivalTimes.append(arrivalTime)
        completionTimes.append(arrivalTime)
        burstTimes.append(burstTime)
        processes[pid] = [arrivalTime, burstTime] # burst time is the remaining time
        
    # do the queues and calculate completion times, order of execution
    while len(processes) != 0: # while there are still processes to be executed
        for pid, [arrival, burst] in processes.items(): # add processes to queue
            if burst != 0 and arrival <= current_time:
                arrivalQueue.append(pid)
                
        # grabs the lowest burst visible for 1 time unit
        pid = min(arrivalQueue, key = lambda x: processes[x][2])
        processes[pid][2] -= 1 # decrement burst time
        if processes[pid][2] == 0:
            processes.pop(pid)
        orderOfExecution.append(pid)
        current_time += 1
    
    return orderOfExecution, completionTimes, arrivalTimes, burstTimes

def roundRobinSort(batchFileData):
    pass

# Accepts 3 lists with index i corresponding to the same process and computes the avg turnaround time,  avg waiting time, turnaround time list for each process, and wait time list for each process
def computeStat(processCompletionTimes, processArrivalTimes, processBurstTimes):
    length = len(processCompletionTimes)
    totalTurnAroundTime = 0
    totalWaitTime = 0
    turnAroundTimes = [] # list of all turnaround times
    waitTimes = [] # list of all wait times
    
    def calculateTurnAroundTime(completionTime, arrivalTime):
        return completionTime - arrivalTime
    
    def calculateWaitTime(turnAroundTime, burstTime):
        return turnAroundTime - burstTime
    
    for i in range(length):
        turnAroundTime = calculateTurnAroundTime(processCompletionTimes[i], processArrivalTimes[i])
        waitTime = calculateWaitTime(turnAroundTime, processBurstTimes[i])
        
        totalTurnAroundTime += turnAroundTime
        totalWaitTime += waitTime
        
        turnAroundTimes.append(turnAroundTime)
        waitTimes.append(waitTime)
    
    avgTurnAroundTime = totalTurnAroundTime / length
    avgWaitTime = totalWaitTime / length
    return avgTurnAroundTime, avgWaitTime, turnAroundTimes, waitTimes

def main():
    if len(sys.argv) != 3:
        print("Please provide command line arguments when running.\npython3 batchSchedulingComparison.py batchfile.txt ShortestRemaining")
        return 1
    try:
        with open(sys.argv[1]) as batchFile:
            batchFileData = batchFile.readlines() # returns a list of strings, each string is a line in the file with the newline character at the end
            
            batchFileData = [list(map(int, line.strip().split(', '))) for line in batchFileData] # remove \n and splits into a 2d array
            batchFileData.sort(key = lambda x: int(x[1])) # sort by arrival time
            
            if sys.argv[2] == "ShortestRemaining":
                orderOfExecution, completionTimes, arrivalTimes, burstTimes = shortestRemainingSort(batchFileData)
            elif sys.argv[2] == "RoundRobin":
                orderOfExecution, completionTimes, arrivalTimes, burstTimes = roundRobinSort(batchFileData)
            else:
                print("Unidentified sorting algorithm. Please input either ShortestRemaining or RoundRobin.")
                return 1
            avgTurnAroundTime, avgWaitTime, turnAroundTimes, waitTimes = computeStat(completionTimes, arrivalTimes, burstTimes)
            
            print("PID ORDER OF EXECUTION:\n")
            for i in range(len(orderOfExecution)):
                print(orderOfExecution[i])
            print("\nAverage Process Turnaround Time: ", avgTurnAroundTime)
            print("Average Process Wait Time: ", avgWaitTime)
            return 0
            
    except:
        print("Input batchfile not found!")


if __name__=="__main__":
    main()