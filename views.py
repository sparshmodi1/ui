from django.shortcuts import render
import re


def index(request):
    return render(request, "home.html")


def result(request):
    notes = None
    error = None
    source = None

    if request.method == "POST":
        source = request.POST.get("source")

        if source == "youtube":
            video_url = request.POST.get("video_url")
            pattern = r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.be)\/.+$'

            if not video_url:
                error = "❌ Please enter a YouTube link"
            elif not re.match(pattern, video_url):
                error = "❌ Invalid YouTube link format"
            else:
                notes = [
                    "Valid YouTube link detected",
                    "Transcript extracted (dummy)",
                    "Notes generated successfully"
                ]

        elif source == "pdf":
            pdf_file = request.FILES.get("pdf_file")

            if not pdf_file:
                error = "❌ Please upload a PDF file"
            else:
                notes = [
                    "PDF processed successfully",
                    "Notes generated"
                ]

        elif source == "text":
            text_content = request.POST.get("text_content")

            if not text_content or text_content.strip() == "":
                error = "❌ Please enter some text"
            else:
                notes = [
                    "Text processed successfully",
                    "Notes generated"
                ]

        else:
            error = "❌ Invalid source selected"

    return render(request, "result.html", {
        "notes": notes,
        "error": error,
        "source": source
    })