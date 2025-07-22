import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    input_folder = "input_folder"
    output_folder = "scatterplots"

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Find all CSV and XLSX files in input_folder
    files = [f for f in os.listdir(input_folder) if f.endswith('.csv') or f.endswith('.xlsx')]
    if not files:
        print(f"No CSV or XLSX files found in '{input_folder}'.")
        return

    # Ask once for the scatterplot title
    plot_title = input("Enter the scatterplot title: ")

    for filename in files:
        file_path = os.path.join(input_folder, filename)
        # Load the data
        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
        # Assume first two columns
        if len(df.columns) < 2:
            print(f"Skipping {filename}: not enough columns.")
            continue

        x_col, y_col = df.columns[:2]
        x = df[x_col]
        y = df[y_col]

        plt.figure()
        plt.scatter(x, y)

        # Add blue line through dots (sorted by x)
        sorted_indices = x.argsort()
        plt.plot(x.iloc[sorted_indices], y.iloc[sorted_indices], '-', color='blue')

        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(plot_title)
        
        # Make y-axis start at 0 and leave headroom at the top
        y_max = y.max()
        plt.ylim(bottom=0, top=y_max + (0.1 * y_max))  # adds 10% extra headroom

        output_filename = os.path.splitext(filename)[0] + "_scatter.png"
        output_path = os.path.join(output_folder, output_filename)
        plt.savefig(output_path)
        plt.close()
        print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()
