from submissions.bbc_weather import bbc_weather
from submissions.bounding_box import bounding_box
from submissions.colab_key import colab_key
from submissions.compare_files import compare_files
from submissions.counting_days import counting_days
from submissions.encode_image import encode_image
from submissions.excel import excel
from submissions.filter_file_attributes import filter_file_attributes
from submissions.google_sheets import google_sheets
from submissions.hacker_news import hacker_news
from submissions.http_requests import http_requests
from submissions.image_lightness import image_lightness
from submissions.large_json_extract import large_json_extract
from submissions.llm_embeddings import llm_embeddings
from submissions.local_llm import local_llm
from submissions.most_similar import most_similar
from submissions.newest_github_user import newest_github_user
from submissions.parse_sales_data import parse_sales_data
from submissions.pdf_to_markdown import pdf_to_markdown
from submissions.prompt_engineering import prompt_engineering
from submissions.replace_across import replace_across
from submissions.sentiment_analysis import sentiment_analysis
from submissions.sort_json_values import sort_json_values
from submissions.vector_databases import vector_databases
from submissions.vscode_info import vscode_info
from submissions.yt_transcribe import yt_transcribe
from submissions.zipfile_extract import zipfile_extract

tasks = {
    "bbc_weather": bbc_weather,
    "bounding_box": bounding_box,
    "colab_key": colab_key,
    "compare_files": compare_files,
    "counting_days": counting_days,
    "encode_image": encode_image,
    "filter_file_attributes": filter_file_attributes,
    "hacker_news": hacker_news,
    "http_requests": http_requests,
    "image_lightness": image_lightness,
    "large_json_extract": large_json_extract,
    "llm_embeddings": llm_embeddings,
    "local_llm": local_llm,
    "most_similar": most_similar,
    "newest_github_user": newest_github_user,
    "parse_sales_data": parse_sales_data,
    "pdf_to_markdown": pdf_to_markdown,
    "prompt_engineering": prompt_engineering,
    "replace_across": replace_across,
    "sentiment_analysis": sentiment_analysis,
    "sort_json_values": sort_json_values,
    "vector_databases": vector_databases,
    "vscode_info": vscode_info,
    "yt_transcribe": yt_transcribe,
    "zipfile_extract": zipfile_extract,
}
