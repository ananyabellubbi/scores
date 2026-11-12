def main():
    scores = [78, 92, 58, 66, 80]
    total = sum(scores)
    average = total / len(scores)

    print("=== main/master output ===")
    print(f"Scores: {scores}")
    print(f"sum: {total}")
    print(f"Average: {average}")


if __name__ == "__main__":
    main()
