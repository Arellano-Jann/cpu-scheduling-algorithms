import sys

def shortestRemainingSort(batchFileData):
    arrivalQueue = []
    return 0

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
            
            batchFileData = [line.strip().split(', ') for line in batchFileData] # remove \n and splits into a 2d array
            
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