# main.py

import os
from config import URL, BROWSERS, SCREENSHOTS_DIR, DIFFS_DIR, REPORT_PATH
from utils.screenshot import capture_screenshot
from utils.compare import compare_images

# Ensure necessary directories exist
for path in ['screenshots/baseline', 'screenshots/current', 'diffs', 'reports']:
    os.makedirs(path, exist_ok=True)

def main():
    results = []

    for browser in BROWSERS:
        baseline_path = os.path.join(SCREENSHOTS_DIR, "baseline", f"{browser}.png")
        current_path = os.path.join(SCREENSHOTS_DIR, "current", f"{browser}.png")
        diff_path = os.path.join(DIFFS_DIR, f"{browser}_diff.png")

        # Capture baseline if it doesn't exist
        if not os.path.exists(baseline_path):
            print(f"Capturing baseline for {browser}")
            capture_screenshot(browser, URL, baseline_path)

        # Capture current screenshot
        print(f"Capturing current screenshot for {browser}")
        capture_screenshot(browser, URL, current_path)

        # Compare images
        print(f"Comparing images for {browser}")
        has_diff = compare_images(baseline_path, current_path, diff_path)
        results.append((browser, has_diff, diff_path if has_diff else None))

    # Generate report
    generate_report(results)

def generate_report(results):
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    with open(REPORT_PATH, "w") as report:
        report.write("<html><head><title>Visual Regression Report</title></head><body>")
        report.write("<h1>Visual Regression Test Results</h1>")
        for browser, has_diff, diff_path in results:
            report.write(f"<h2>{browser.capitalize()}</h2>")
            if has_diff:
                report.write(f"<p>Differences found. See below:</p>")
                report.write(f'<img src="../{diff_path}" alt="Diff for {browser}"><br>')
            else:
                report.write("<p>No differences found.</p>")
        report.write("</body></html>")

if __name__ == "__main__":
    main()