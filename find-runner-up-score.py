if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
unique_scores = list(set(arr))  # Remove duplicates
sorted_scores = sorted(unique_scores, reverse=True)  # Sort in descending order

runner_up_score = sorted_scores[1]  # Access the second element

print(runner_up_score)