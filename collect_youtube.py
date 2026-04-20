import os
import json
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi

OUTPUT_DIR = "research/youtube-transcripts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Pre-populated with your exact video IDs
experts = [
    {
        "author": "Koray Tuğberk GÜBÜR",
        "video_id": "PCNnLSCjSMc",
        "category": "Semantic Layer",
        "tags": ["Topical Authority", "Semantic Mapping"]
    },
    {
        "author": "Mike King",
        "video_id": "ukpU-EfRtV4",
        "category": "Technical Architecture",
        "tags": ["Entity Extraction", "Data SEO"]
    },
    {
        "author": "Lily Ray",
        "video_id": "nw-dllribgQ",
        "category": "Risk Mitigation",
        "tags": ["E-E-A-T", "Helpful Content"]
    },
    {
        "author": "Aleyda Solis",
        "video_id": "fxa8DAo8hgg",
        "category": "Workflow Automation",
        "tags": ["AI Agents", "Technical Audits"]
    },
    {
        "author": "Kevin Indig",
        "video_id": "jxXPpXL2pFg",
        "category": "Search Architecture",
        "tags": ["Indexing", "Large-Scale SEO"]
    }
]

def format_to_markdown(expert_data, transcript_data):
    date_collected = datetime.now().strftime("%Y-%m-%d")
    author_safe_name = expert_data["author"].replace(" ", "_").lower()

    md_content = "---\n"
    md_content += f"author: \"{expert_data['author']}\"\n"
    md_content += "source_type: \"YouTube\"\n"
    md_content += f"date_collected: {date_collected}\n"
    md_content += f"strategic_category: \"{expert_data['category']}\"\n"
    md_content += f"key_entities: {json.dumps(expert_data['tags'])}\n"
    md_content += "---\n\n"
    md_content += f"# Transcript Analysis: {expert_data['author']}\n\n"
    md_content += f"**Source URL:** https://www.youtube.com/watch?v={expert_data['video_id']}\n\n"
    md_content += "---\n\n"

    chunk_size = 15
    for i in range(0, len(transcript_data), chunk_size):
        chunk = transcript_data[i:i + chunk_size]
        start_time = chunk[0].get("start", 0)
        minutes = int(start_time // 60)
        seconds = int(start_time % 60)
        timestamp = f"### [{minutes:02d}:{seconds:02d}]\n"

        paragraph_text = " ".join([item.get("text", "").replace("\n", " ") for item in chunk])
        md_content += f"{timestamp}{paragraph_text}\n\n"

    filename = f"{OUTPUT_DIR}/{author_safe_name}_transcript.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"✅ Saved: {filename}")

if __name__ == "__main__":
    for expert in experts:
        print(f"Fetching {expert['author']}...")
        try:
            transcript = YouTubeTranscriptApi.get_transcript(expert["video_id"])
            format_to_markdown(expert, transcript)
        except Exception as e:
            print(f"❌ Failed to fetch {expert['author']}: {e}")
