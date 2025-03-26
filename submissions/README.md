
# Graded Assignment Breakdowns

This section focuses on each task for each graded assignment and their associated module within the project. This also serves as a checklist to identify which are possible within a Pythonic approach.

⚠️ Refers to a task that might rely on external control

💣 Refers to a task that cannot be accomplished with just Python

🚫 Refers to a task that cannot be accomplished

- Graded Assignment 1
  1. [VS Code Version](./vscode_info.py)
  2. [Make HTTP Requests with uv](./http_requests.py)
  3. [Run command with npx](./npx_prettier.py) ⚠️
  4. [Use Google Sheets](./google_sheets.py)
  5. [Use Excel](./excel.py)
  6. [Use DevTools](./chrome_devtools.py)
  7. [Count Wednesdays](./counting_days.py)
  8. [Extract CSV from a ZIP](./csv_zipfile.py)
  9. [Use JSON](./sort_json_values.py)
  10. [Multi-cursor edits](./json_cleanup.py)
  11. [CSS Selectors](./css_selectors.py)
  12. [Process files with different encoding](./process_encoding.py)
  13. [Use GitHub](./github_push.py)
  14. [Replace across files](./replace_across.py)
  15. [List files and attributes](./filter_file_attributes.py)
  16. [Move and rename files](./move_rename.py)
  17. [Compare files](./compare_files.py)
  18. [SQL: Ticket Sales](./ticket_sales.py)
- Graded Assignment 2
  1. [Write documentation in Markdown](./create_markdown.py)
  2. [Compress an image](./compress_image.py)
  3. [Hosting Portfolios in Github](./host_portfolio.py)
  4. [Use Google Colab](./colab_key.py)
  5. [Use an Image Library in Google Colab](./image_lightness.py)
  6. [Deploy a Python API to Vercel](./vercel_api.py) 🚫
  7. [Create a GitHub Action](./github_action.py)
  8. [Push an image to Docker Hub](./docker_hub.py)
  9. [Write a FastAPI server to serve data](./fastapi_server.py)
  10. [Run a local LLM with Llamafile and ngrok](./local_llm.py)
- Graded Assignment 3
  1. [LLM Sentiment Analysis](./sentiment_analysis.py)
  2. [LLM Token Costs](./token_costs.py)
  3. [Generate addresses with LLM](./generate_addresses.py) 🚫
  4. [Base64 Encoding](./encode_image.py)
  5. [LLM Embeddings](./llm_embeddings.py)
  6. [Embedding Similarity](./most_similar.py)
  7. [Vector Databases](./vector_databases.py)
  8. [Function Calling](./function_calling.py)
  9. [Prompt Engineering](./prompt_engineering.py) 🚫
- Graded Assignment 4
  1. [Import HTML to Google Sheets](./html_google.py) 💣
  2. [Scrape IMDb Movies](./imdb_scrape.py)
  3. [Wikipedia Outline](./wikipedia_outline.py)
  4. [Scrape the BBC Weather API](./bbc_weather.py)
  5. [Find the bounding box of a city](./bounding_box.py)
  6. [Search Hacker News](./hacker_news.py)
  7. [Find newest GitHub User](./newest_github_user.py)
  8. [Scheduled GitHub Action](./github_actions.py) 💣
  9. [Extract tables from PDF](./extract_tables.py)
  10. [Convert PDF to Markdown](./pdf_to_markdown.py)
- Graded Assignment 5
  1. [Clean up Excel sales data](./excel_sales.py) 💣
  2. [Clean up student marks](./clean_student_marks.py)
  3. [Apache log requests](./log_requests.py)
  4. [Apache log downloads](./request_downloads.py)
  5. [Clean sales data](./clean_sales.py)
  6. [Parsing Partial JSON](./parse_sales_data.py)
  7. [Extract nested JSON keys](./large_json_extract.py)
  8. [DuckDB: Social Media Interactions](./duckdb_interactions.py) ⚠️
  9. [Transcribe a Youtube video](./yt_transcribe.py)
  10. [Reconstruct an image](./jigsaw_image.py)

## Notes

Some approaches to the assignments didn't have codes or isn't possible given the context to the assignment. This section serves as a summary of each assignment and the "suggested" approach by the procters.

- [1.4. Use Google Sheets](./google_sheets.py) Solve using a Python Formula
- [1.5. Use Excel](./excel.py) Solve using a Python Formula
- [1.6. Use DevTools](./chrome_devtools.py) Solve by scraping it
- [1.11. CSS Selectors](./css_selectors.py) No suggestion was mentioned ~~Solve by scraping it~~
- [1.13. Use GitHub](./github_push.py) Solve by using GitHub API
- [2.2. Compress an image](./compress_image.py) Returns Base64 encoded data URI beginning with "data:image/..."
- [2.3. Hosting Portfolios in Github](./host_portfolio.py) Solve by using GitHub API
- [2.4. Use Google Colab](./colab_key.py) You can reverse engineer the output ~~Fake the Google Colab response~~
- [2.5. Use an Image Library in Google Colab](./image_lightness.py) Fake the Google Colab response
- [2.6. Deploy a Python API to Vercel](./vercel_api.py) Let an LLM write and deploy using the Vercel API 🚫
- [2.7. Create a GitHub Action](./github_action.py) Solve by using GitHub API
- [2.8. Push an image to Docker Hub](./docker_hub.py) Solve by using Docker Hub API
- [2.10. Run a local LLM with Llamafile and ngrok](./local_llm.py) Run Llamafile in ngrok
