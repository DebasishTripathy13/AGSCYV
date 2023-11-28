import re
import validators
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask import Flask, request, render_template, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import torch

app = Flask(__name__)

# Initialize the WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Add this line if you want to run in headless mode
driver = webdriver.Chrome(options=chrome_options)

def is_valid_url(url):
    if not validators.url(url):
        return False
    if not re.match(r'^https?://(?:www\.)?youtube\.com/watch\?v=[\w-]{11}$', url):
        return False
    return True

def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

# Use the specified model for summarization
hf_name = 'pszemraj/led-large-book-summary'
summarizer = pipeline("summarization", hf_name, device=0 if torch.cuda.is_available() else -1)

def get_summary(transcript):
    summary = summarizer(transcript, max_length=100, min_length=30)[0]['summary_text']
    return summary

def automate_comment(url, summary):
    driver.get(url)
    time.sleep(5)

    # Find the comments section by xpath
    comments_xpath = "//ytd-comments[@id='comments']"
    comments = driver.find_element_by_xpath(comments_xpath)
    comments.click()

    # Find the comment box by xpath
    comment_box_xpath = "//div[@id='contenteditable-root']"
    comment_box = driver.find_element_by_xpath(comment_box_xpath)
    comment = f"Video Summary: {summary}"
    comment_box.send_keys(comment)
    comment_box.send_keys(Keys.RETURN)

    time.sleep(5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comment-and-summary', methods=['GET'])
def comment_and_summary_api():
    url = request.args.get('url')

    if not is_valid_url(url):
        return jsonify({"error": "Invalid YouTube URL"}), 400

    video_id = url.split('=')[1]

    try:
        transcript = get_transcript(video_id)
        print(f"Transcript: {transcript}")  # Add this line for debugging
        summary = get_summary(transcript)
        print(f"Summary: {summary}")  # Add this line for debugging
        automate_comment(url, summary)

        return jsonify({"success": True, "summary": summary}), 200

    except Exception as e:
        print(f"Error: {str(e)}")  # Add this line for debugging
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        driver.quit()
