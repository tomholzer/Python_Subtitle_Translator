Subtitle Translation Script (SRT to SRT)

**Overview**

This Python script translates subtitle files in .srt format from English to Czech using the deep_translator library. The script preserves the subtitle structure, including numbering and timestamps, while ensuring a batch translation approach to avoid API rate limits.

**Features**

Reads an .srt subtitle file and translates only the text lines.

Preserves subtitle numbering and timestamps.

Uses batch processing to reduce API requests.

Displays progress updates with percentage and elapsed time.

Saves the translated subtitles into a new .srt file.

**Requirements**

Ensure you have Python installed and install the required dependencies:

pip install deep-translator

**Usage**

Modify the input_srt and output_srt variables in the script with the correct file paths and run the script:

python translate_srt.py

Example Input:

1
00:01:21,679 --> 00:01:23,680
<i>Come in, Officer Knight
and Greg the Dog.</i>

2
00:01:23,815 --> 00:01:25,048
<i>Do you copy?</i>

Example Output:

1
00:01:21,679 --> 00:01:23,680
<i>Přijďte, důstojníku Knight
a Gregu, Pse.</i>

2
00:01:23,815 --> 00:01:25,048
<i>Rozumíte?</i>

**Notes**

The script includes a delay (time.sleep(1)) to prevent exceeding API limits.

If a translation fails, the original text is retained.

The progress indicator updates every 10% and shows elapsed time.

**License**

This script is open-source and can be modified freely.
