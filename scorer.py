import sys

INPUT_DIRECTORY = "input_data"
CELL_SEPARATOR = ","
NEW_LINE = "\n\n"

# get last instance of ,
# get score

# assumption that scores are between 0 & 100 and integer
# assumption that there is no ',' in names
# assumption that the line spacing in the example

def clean_output(scorers, score):
    sorted_scorers = sorted(scorers)
    clean_scorers = f"{NEW_LINE}".join(sorted_scorers).replace(CELL_SEPARATOR, " ")
    return f"{clean_scorers}{NEW_LINE}Score: {score}{NEW_LINE}"

def sort_rows(rows):
    max_score = 0
    max_scorer = []
    for row in rows:
        if ',' in row:
            score_separator = row.rfind(CELL_SEPARATOR)
            score = int(row[score_separator + 1 :])
            if score > max_score:
                max_score = score
                max_scorer = [row[:score_separator]]
            elif score == max_score:
                also_max = row[:score_separator]
                max_scorer.append(also_max)
    return max_scorer, max_score

def main(args):
    try:
        file_path = f"{INPUT_DIRECTORY}/{args[1]}"
        try:
            with open(file_path, 'r') as file:
                str_data = file.read()
                rows = str_data.split("\n")
                if rows[0].endswith("Score"):
                    rows.pop(0)
                scorer, score = sort_rows(rows)
                output = clean_output(scorer, score)
                sys.stdout.write(output)
        except FileNotFoundError:
            print(f"Error: File not found. Please check the file path. (..{file_path})")
    except IndexError:
        print("Error: Provide file name as srgument when running script")


if __name__ == "__main__":
    main(sys.argv)