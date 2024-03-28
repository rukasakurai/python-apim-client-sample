# Python Azure API Management Client Sample
This is a repository containing sample Python code that calls an API published through Azure API Management.

## Preparation
1. Deploy an Azure API Management instance (e.g., leverage https://github.com/Azure-Samples/jp-azureopenai-samples/tree/main/6.azureopenai-landing-zone-accelerator)
1. Deploy https://github.com/Azure-Samples/azure-search-openai-demo
1. Add an API in Azure API Management that calls the AI Search index endpoint of azure-search-openai-demo
1. Add an API in Azure API Management that calls the `/chat` endpoint of azure-search-openai-demo
1. Get your APIM endpoint and subscription key and set them as environment variables as follows

```bash
export AZURE_APIM_ENDPOINT=<Your APIM Endpoint>
export APIM_SUB_KEY=<Your APIM Subscription Key>
```

## Unit Testing calls to API Management
`python -m unittest discover -s tests`

## Forking this repository
You will need to set up GitHub Action secrets for the GitHub Actions to function properly
https://github.com/rukasakurai/python-apim-client-sample/actions