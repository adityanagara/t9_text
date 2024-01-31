
from typing import List, Dict
from typing import Callable

numbers_to_letters = {"2": ["a", "b", "c"],
                    "3": ["d", "e", "f"],
                    "4": ["g", "h", "i"], 
                    "5": ["j", "k", "l"], 
                    "6": ["m", "n", "o"], 
                    "7": ["p", "q", "r", "s"], 
                    "8": ["t", "u", "v"], 
                    "9": ["w", "x", "y", "z"]}


def validateInput(nums: str, dictionary: Dict[str, Callable[[str], bool]]):
    isNotValidNums = [n for n in nums if n not in numbers_to_letters]
    if any(isNotValidNums):
        raise Exception(f"Input should be string sequence containing numbers in the range 2-9, found: {nums}")
    if "isWord" not in dictionary:
        raise Exception(f"isWord not found in dictionary, found {dictionary.keys()}")



def findAllWords(nums: str, dictionary: Dict[str, Callable[[str], bool]]) -> List[str]:
    """A function that takes a sequence of numbers between 2-9 (inclusive) 
    and returns all combinations of words that satisfy the isWord callable. 

    Args:
        nums : str - A sequence on numbers between 2-9
        dictionary: A dictionary of callables
    """
    validateInput(nums, dictionary)
    n: int = len(nums)
    all_words: List = list()

    def findWordCombinations(current_sequence: List[str], idx: int) -> None:
        currentWord = "".join(current_sequence[:])
        if dictionary["isWord"](currentWord):
            all_words.append(currentWord)
        if len(current_sequence) == n:
            # We have hit the leaf node backtrack to parent to find the next leaf.
            return

        seq = numbers_to_letters.get(nums[idx], [])

        for w in seq:
            current_sequence.append(w)
            # The recursive call here is head recursion since computation takes place
            # after the recursive call. Evaluation of the function happens after
            # the state of each recursive call is completed. 
            findWordCombinations(current_sequence, idx + 1)
            current_sequence.pop()
    
    findWordCombinations([], 0)

    return all_words

def main():
    inputDict = {"isWord": lambda x: len(x) > 0 and len(x) % 2 == 0}
    words = findAllWords("4663", inputDict)
    print(words)

if __name__ == "__main__":
    main()
