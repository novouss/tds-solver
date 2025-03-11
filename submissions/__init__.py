from submissions.compare_files import compare_files
from submissions.cosine_similarity import cosine_similarity
from submissions.counting_days import counting_days
from submissions.filter_file_attributes import filter_file_attributes
from submissions.hacker_news import hacker_news
from submissions.llm_embeddings import llm_embeddings
from submissions.newest_github_user import newest_github_user
from submissions.pdf_to_markdown import pdf_to_markdown
from submissions.replace_across import replace_across
from submissions.sort_json_values import sort_json_values
from submissions.vscode_info import vscode_info
from submissions.yt_transcribe import yt_transcribe
from submissions.zipfile_extract import zipfile_extract

tasks = {
    "compare_files": compare_files,
    "cosine_similarity": cosine_similarity,
    "counting_days": counting_days,
    "filter_file_attributes": filter_file_attributes,
    "hacker_news": hacker_news,
    "llm_embeddings": llm_embeddings,
    "newest_github_user": newest_github_user,
    "pdf_to_markdown": pdf_to_markdown,
    "replace_across": replace_across,
    "sort_json_values": sort_json_values,
    "vscode_info": vscode_info,
    "yt_transcribe": yt_transcribe,
    "zipfile_extract": zipfile_extract,
}
