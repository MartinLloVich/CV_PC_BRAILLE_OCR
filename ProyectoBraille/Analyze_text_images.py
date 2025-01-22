import os
import cv2
import time
import matplotlib.pyplot as plt
from ultralytics import YOLO

def main():
    # Directories
    test_dir = "datasets/images/test"
    results_dir = "results"
    approved_dir = os.path.join(results_dir, "approved")
    disapproved_dir = os.path.join(results_dir, "disapproved")
    
    # Create results directories if they do not exist
    os.makedirs(approved_dir, exist_ok=True)
    os.makedirs(disapproved_dir, exist_ok=True)
    
    # Initialize YOLO model
    model = YOLO("runs/detect/train/weights/best.pt")

    # Initialize counters
    results_summary = {}
    total_images = 0
    total_approved = 0
    total_disapproved = 0

    # Start time
    start_time = time.time()

    # Process each image in the test directory
    for file_name in os.listdir(test_dir):
        if file_name.endswith(".png"):
            total_images += 1

            # Extract letter from the file name
            letter = file_name.split("_")[0]
            img_path = os.path.join(test_dir, file_name)

            # Read the image
            img = cv2.imread(img_path)

            # Perform prediction
            predictions = model.predict(img)[0]
            pred_image = predictions.plot()

            # Get predicted classes and their scores
            classes = predictions.boxes.cls.cpu().numpy()  # Predicted class indices
            scores = predictions.boxes.conf.cpu().numpy()  # Confidence scores

            # Check predictions
            if len(classes) > 0:
                # Find the prediction with the highest confidence
                max_index = scores.argmax()
                predicted_class = int(classes[max_index])

                # Determine if the prediction matches the letter
                if chr(predicted_class + ord('a')) == letter.lower():
                    output_dir = approved_dir
                    status = "approved"
                    total_approved += 1
                else:
                    output_dir = disapproved_dir
                    status = "disapproved"
                    total_disapproved += 1
            else:  # If no predictions, classify as disapproved
                output_dir = disapproved_dir
                status = "disapproved"
                total_disapproved += 1

            # Save the processed image
            output_path = os.path.join(output_dir, file_name)
            cv2.imwrite(output_path, pred_image)

            # Update results by letter
            if letter not in results_summary:
                results_summary[letter] = {"approved": 0, "disapproved": 0}

            results_summary[letter][status] += 1

    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Write results to results.txt
    results_txt_path = os.path.join(results_dir, "results.txt")
    with open(results_txt_path, "w") as results_file:
        for letter, counts in sorted(results_summary.items()):
            results_file.write(f"Letter: {letter}\n")
            results_file.write(f"  Approved: {counts['approved']}\n")
            results_file.write(f"  Disapproved: {counts['disapproved']}\n")
        results_file.write("\n")
        results_file.write(f"Total images analyzed: {total_images}\n")
        results_file.write(f"Total approved: {total_approved}\n")
        results_file.write(f"Total disapproved: {total_disapproved}\n")
        results_file.write(f"Total simulation time: {elapsed_time:.2f} seconds\n")

    # Generate bar chart
    letters = sorted(results_summary.keys())
    approved_counts = [results_summary[letter]["approved"] for letter in letters]
    disapproved_counts = [results_summary[letter]["disapproved"] for letter in letters]

    plt.figure(figsize=(10, 6))
    bar_width = 0.35
    x = range(len(letters))

    plt.bar(x, approved_counts, width=bar_width, label="Approved")
    plt.bar([p + bar_width for p in x], disapproved_counts, width=bar_width, label="Disapproved")

    plt.xlabel("Letters")
    plt.ylabel("Count")
    plt.title("Approved and Disapproved Counts by Letter")
    plt.xticks([p + bar_width / 2 for p in x], letters)
    plt.legend()

    # Save the chart
    chart_path = os.path.join(results_dir, "results_chart.png")
    plt.savefig(chart_path)
    plt.close()

if __name__ == "__main__":
    main()