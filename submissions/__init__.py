from submissions.bbc_weather import bbc_weather
from submissions.bounding_box import bounding_box
from submissions.clean_sales import clean_sales
from submissions.clean_student_marks import clean_student_marks
from submissions.colab_key import colab_key
from submissions.compare_files import compare_files
from submissions.counting_days import counting_days
from submissions.create_markdown import create_markdown
from submissions.encode_image import encode_image
from submissions.excel import excel
from submissions.extract_tables import extract_tables
from submissions.filter_file_attributes import filter_file_attributes
from submissions.function_calling import function_calling
from submissions.google_sheets import google_sheets
from submissions.hacker_news import hacker_news
from submissions.http_requests import http_requests
from submissions.image_lightness import image_lightness
from submissions.imdb_movies import imdb_scrape
from submissions.jigsaw_image import jigsaw_image
from submissions.large_json_extract import large_json_extract
from submissions.llm_embeddings import llm_embeddings
from submissions.local_llm import local_llm
from submissions.log_requests import log_requests
from submissions.most_similar import most_similar
from submissions.newest_github_user import newest_github_user
from submissions.npx_prettier import npx_prettier
from submissions.parse_sales_data import parse_sales_data
from submissions.pdf_to_markdown import pdf_to_markdown
from submissions.prompt_engineering import prompt_engineering
from submissions.replace_across import replace_across
from submissions.request_downloads import request_downloads
from submissions.sentiment_analysis import sentiment_analysis
from submissions.sort_json_values import sort_json_values
from submissions.token_costs import token_costs
from submissions.vector_databases import vector_databases
from submissions.vscode_info import vscode_info
from submissions.wikipedia_outline import wikipedia_outline
from submissions.yt_transcribe import yt_transcribe
from submissions.csv_zipfile import csv_zipfile

tasks = {
    "bbc_weather": bbc_weather,
    "bounding_box": bounding_box,
    "colab_key": colab_key,
    "clean_sales": clean_sales,
    "clean_student_marks": clean_student_marks,
    "compare_files": compare_files,
    "counting_days": counting_days,
    "create_markdown": create_markdown,
    "encode_image": encode_image,
    "excel": excel,
    "extract_tables": extract_tables,
    "filter_file_attributes": filter_file_attributes,
    "function_calling": function_calling,
    "google_sheets": google_sheets,
    "hacker_news": hacker_news,
    "http_requests": http_requests,
    "image_lightness": image_lightness,
    "imdb_scrape": imdb_scrape,
    "jigsaw_image": jigsaw_image,
    "large_json_extract": large_json_extract,
    "llm_embeddings": llm_embeddings,
    "local_llm": local_llm,
    "log_requests": log_requests,
    "most_similar": most_similar,
    "newest_github_user": newest_github_user,
    "npx_prettier": npx_prettier,
    "parse_sales_data": parse_sales_data,
    "pdf_to_markdown": pdf_to_markdown,
    "prompt_engineering": prompt_engineering,
    "replace_across": replace_across,
    "request_downloads": request_downloads,
    "sentiment_analysis": sentiment_analysis,
    "sort_json_values": sort_json_values,
    "token_costs": token_costs,
    "vector_databases": vector_databases,
    "vscode_info": vscode_info,
    "wikipedia_outline": wikipedia_outline,
    "yt_transcribe": yt_transcribe,
    "csv_zipfile": csv_zipfile,
}
