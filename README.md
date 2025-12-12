# Smart Folder Allocator

This project is an automated file organization tool that uses Google's Gemini AI to intelligently classify and sort files from your Downloads folder into organized categories.

## Features

- **Automated Monitoring**: Watches your `~/Downloads` folder for new files in real-time.
- **AI Classification**: Uses Google's Gemini 1.5 Pro model to analyze filenames and file types to determine the most appropriate category (e.g., Documents, Music, Images, Code).
- **Automatic Organization**: Moves files to designated folders in `~/Organized`.

## Project Structure

- `agent.py`: Handles the core logic for moving files to their target destinations.
- `tool.py`: Contains the `classify_file_gemini` function which interfaces with the Gemini API to get folder suggestions.
- `watch.py`: The main entry point that sets up the file system observer to watch for new files.

## Prerequisites

- **Python 3.x**
- **Gemini API Key**: You need an API key from Google AI Studio.

## Installation

1.  Clone this repository or download the source code.
2.  Install the required Python packages:

    ```bash
    pip install google-generativeai watchdog
    ```

## Configuration

1.  Open `tool.py`.
2.  Insert your Gemini API key in the `genai.configure` line:

    ```python
    genai.configure(api_key="YOUR_API_KEY_HERE")
    ```

    > **Note**: It is recommended to use environment variables for API keys for better security, but the current code expects it directly in the file.

3.  (Optional) Verify/Modify paths in `watch.py` and `agent.py` if you want to change the source or destination directories.
    - Default Source: `~/Downloads`
    - Default Destination: `~/Organized`

## Usage

Run the `watch.py` script to start monitoring your Downloads folder:

```bash
python watch.py
```

The script will keep running and print "Watching: [Path to Downloads]" to the console. Can be stopped with `Ctrl+C`.
