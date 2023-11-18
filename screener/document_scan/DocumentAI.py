from google.api_core.client_options import ClientOptions
from google.cloud import documentai
import sys
import os

def scan_resume():
    PROJECT_ID = "github-recruiter-405500"
    LOCATION = "us_east1"  # Format is 'us' or 'eu'
    PROCESSOR_ID = "90d61cdc4cadeb91"  # Create processor in Cloud Console

    # The local file in your current working directory
    cwd = os.getcwd()
    FILE_PATH = f'{cwd}/document_scan/test_resume/JSandoval-Resume-10-18-23.pdf'
    # Refer to https://cloud.google.com/document-ai/docs/file-types
    # for supported file types
    MIME_TYPE = "application/pdf"   

    # Instantiates a client
    docai_client = documentai.DocumentProcessorServiceClient(
        client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
    )

    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    # You must create new processors in the Cloud Console first
    RESOURCE_NAME = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)

    # Read the file into memory
    with open(FILE_PATH, "rb") as image:
        image_content = image.read()

    # Load Binary Data into Document AI RawDocument Object
    raw_document = documentai.RawDocument(content=image_content, mime_type=MIME_TYPE)

    # Configure the process request
    request = documentai.ProcessRequest(name=RESOURCE_NAME, raw_document=raw_document)

    # Use the Document AI client to process the sample form
    result = docai_client.process_document(request=request)

    document_object = result.document
    print("Document processing complete.")
    print(f"Text: {document_object.text}")
