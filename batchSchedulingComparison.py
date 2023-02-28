import sys

def shortestRemainingSort(batchFileData):
    arrivalQueue = []
    

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
    pass


if __name__=="__main__":
    main()