def main():
    scores = [78, 92, 58, 66, 80]
    total = sum(scores)
    average = total / len(scores)
    minimum = min(scores)
    maximum = max(scores)

    print("=== main/master output ===")
    print(f"Scores: {scores}")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")


if __name__ == "__main__":
    main()
