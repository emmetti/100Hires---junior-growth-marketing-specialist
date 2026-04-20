import os
import json
import requests
from datetime import datetime

# --- Configuration ---
SUPADATA_API_KEY = "YOUR_API_KEY_HERE"
OUTPUT_DIR = "research/youtube-transcripts"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# --- Source Data (The "Playbook" Architecture) ---
experts = [
    {
        "author": "Koray Tuğberk GÜBÜR",
        "video_url": "https://www.youtube.com/watch?v=PLACEHOLDER",
        "category": "Semantic Layer",
        "tags": ["Topical Authority", "Semantic Mapping"]
    },
    {
        "author": "Mike King",
        "video_url": "https://www.youtube.com/watch?v=PLACEHOLDER",
        "category": "Technical Architecture",
        "tags": ["Entity Extraction", "Data SEO"]
    },
    {
        "author": "Lily Ray",
        "video_url": "https://www.youtube.com/watch?v=PLACEHOLDER",
        "category": "Risk Mitigation",
        "tags": ["E-E-A-T", "Helpful Content"]
    },
    {
        "author": "Aleyda Solis",
        "video_url": "https://www.youtube.com/watch?v=PLACEHOLDER",
        "category": "Workflow Automation",
        "tags": ["AI Agents", "Technical Audits"]
    },
    {
        "author": "Kevin Indig",
        "video_url": "https://www.youtube.com/watch?v=PLACEHOLDER",
        "category": "Search Architecture",
        "tags": ["Indexing", "Large-Scale SEO"]
    }
]

def fetch_transcript(video_url):
    """Hits the Supadata API to retrieve the transcript."""
    print(f"Fetching transcript for {video_url}...")
    headers = {"x-api-key": SUPADATA_API_KEY}
    endpoint = f"https://api.supadata.ai/v1/youtube/transcript?url={video_url}"
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        return response.json()
    return None

def format_to_markdown(expert_data, transcript_json):
    """Converts the raw JSON into the Playbook-ready Markdown format."""
    date_collected = datetime.now().strftime("%Y-%m-%d")

    md_content = "---\n"
    md_content += f"author: \"{expert_data['author']}\"\n"
    md_content += "source_type: \"YouTube\"\n"
    md_content += f"date_collected: {date_collected}\n"
    md_content += f"strategic_category: \"{expert_data['category']}\"\n"
    md_content += f"key_entities: {json.dumps(expert_data['tags'])}\n"
    md_content += "---\n\n"
    md_content += f"# Transcript Analysis: {expert_data['author']}\n\n"

    content = transcript_json.get("content", [])
    chunk_size = 15

    for i in range(0, len(content), chunk_size):
        chunk = content[i:i + chunk_size]
        start_time = chunk[0].get("offset", 0)
        minutes = int(start_time // 60)
        seconds = int(start_time % 60)
        timestamp = f"[{minutes:02d}:{seconds:02d}]"

        paragraph_text = " ".join([item.get("text", "") for item in chunk])
        md_content += f"### {timestamp}\n{paragraph_text}\n\n"

    filename = f"{OUTPUT_DIR}/{expert_data['author'].replace(' ', '_').lower()}_transcript.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_content)

if __name__ == "__main__":
    for expert in experts:
        raw_data = fetch_transcript(expert["video_url"])
        if raw_data:
            format_to_markdown(expert, raw_data)
