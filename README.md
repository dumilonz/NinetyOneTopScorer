# NinetyOneTopScorer
This is a project for the NinetyOne Top Scorer Problem.

# Requirements 
- Python 3.9.16 or higher

# How to run
This is a script written in python. The script's file name is scorer. 

The script needs to be run with 1 argument (the file name). 

The file type must be included, but it can be a CSV or plain-text file (.txt).

Please view the `input_data` directory for more data test examples
```python
python scorer.py TestData.csv

# OR 

python scorer.py TestData5.txt
```

# Explanation of Design your choices and assumptions

## Design choices
Listed below are some design choices:
- There is a main function where the try and except for incorrect arguments is done. Logic for the sorting of the rows is done in its own function.
- The cleaning of the data (i.e. removing the comma between name and surname) was left till last. This would not impact the alphabetical sort (read assumption later). And this would allow for the entire final string to replace all `,`s in the final output, not piecemeal. Furthermore, if there are multiple lower scores, the scleaning up would be repetitive will iterating through sorted data.



## Assumptions
Listed below are some assumptions that were made:
- All scores are greater than 0
- All scores are integers
- That the file can begin with the opening row `First Name,Second Name,Score` or without it. This row is removed from the data if it is found to be in the file. 
- That no names or surnames of people would include a `,` (a comma).
- The spacing between lines in the provided output example in the document were large. Hence, it was assumed that there ws 1 empty line between each maximum scorer's name and the final line with the Score value displayed. it was also assumed that the final line was an empty line.  


