import os, json
from typing import Any

class DataParser:
    def __init__(self) -> None:
        self.modes = ["test","train"]
        self.subtopics =  ["algebra","counting_and_probability","geometry","intermediate_algebra","number_theory","prealgebra","precalculus"]
        self.datapath = "./"
        self.solutionList = []
        self.resultsList = []
        self.jsonlist = []
        self.resultsDict = {}

    def __getattribute__(self, __name: str) -> Any:
        if __name == "datapath":
            return self.datapath
        elif __name == "subtopics":
            return self.subtopics 
        elif __name == "modes":
            return self.modes
        elif __name == "solutionsList":
            return self.solutionList
        elif __name == "resultsList":
            return self.resultsList
        elif __name == "jsonList":
            return self.jsonlist
        elif __name == "resultsDict":
            return self.resultsDict
        
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "datapath":
            self.datapath == __value
        elif __name == "subtopics":
            self.subtopics == __value
        elif __name == "modes":
            self.modes == __value



    def loadResults(self,mode:str,subtopic:str) -> None:
        self.solutionList = []
        self.resultsList = []
        self.jsonlist = []
        path_to_json = "./"+mode+"/"+subtopic+"/"
        #Get all the json file names in the selected directory
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        
        for file_name in json_files:
            with open(path_to_json + file_name) as f:
                self.jsonlist.append(json.load(f))

        #Extract solutions to a list
        for data in self.jsonlist:
            self.solutionList.append(data["solution"])

        #Extract results from the solutions
        for solution in self.solutionList:
            start = solution.rfind("boxed") + 6
            end = start + 1
            braketCounter = 0
            #Tries to find the end of //boxed{} area
            while end < len(solution) and (solution[end] != '}' or braketCounter != 0) :
                if solution[end] == '{':
                    braketCounter += 1
                if solution[end] == '}':
                    braketCounter -=1
                end += 1 
            #Fail safe for misused boxed at the end
            if(end==len(solution)):
                self.resultsList.append("ERROR")
                continue
            self.resultsList.append(solution[start:end])
        #Match results with the corresponding json
        resultsDict = {}
        for (fileid,result) in zip(self.jsonlist,self.resultsList):
            resultsDict[fileid] = result

    def saveasfile(self,mode:str,subtopic:str)->None:
    #Save results as json
        with open("./"+mode+"/"+subtopic+'_answers.json', 'w') as fp:
            json.dump(self.resultsDict, fp)