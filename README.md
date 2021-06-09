# ASoCActionDemo
ASoCActionDemo is a sample application and workflows used to demonstrate HCL AppScan CodeSweep and HCL AppScan on Cloud GitHub capabilities.

ASoCActionDemo is a Python application written purely for demonstration purposes and has known vulnerabilities. A description of the application is in Demo_ReadMe.txt.


## 1. HCL AppScan CodeSweep

**HCL AppScan CodeSweep** is an HCL AppScan extension for Visual Studio Code provides Static Application Security Testing (SAST) functionality for detecting vulnerabilities early in the development life cycle. It's a lightweight, FREE extension for quickly and easily discovering vulnerabilites while you're writing code.

To use, simply clone this project and use Microsoft Visual Code and the HCL AppScan CodeSweep to scan for vulnerabilities. Resources and instructions are listed below.


Instructions and resources are listed below.

* [HCL AppScan CodeSweep | Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=HCLTechnologies.hclappscancodesweep)

* [This is AppScan - AppScan CodeSweep | YouTube](https://www.youtube.com/watch?v=OgVGjpQAgQA&t=207s)


## 2. HCL AppScan CodeSweep Github Action
**HCL AppScan CodeSweep Github Action** extension allows for scanning for vulnerabilities in changed code, triggered via a Pull Request. The **HCL AppScan CodeSweep Github Action** extension for this project is located in [.github/workflows/main.yml](https://github.com/glhcl/ASoCActionDemo/blob/main/.github/workflows/main.yml). 

Instructions and resources are listed below.

* [HCL AppScan CodeSweep Github Action | GitHub Marketplace](https://www.youtube.com/watch?v=Ublu4zPAKtE)

* [This is AppScan - AppScan CodeSweep & GitHub | YouTube](https://www.youtube.com/watch?v=Ublu4zPAKtE)




## 3. HCL ASoC SAST Workflow
**HCL ASoC SAST Workflow** performs a security scan against an entire codebase, triggered manually via Github Actions. The HCL ASoC SAST Workflow is a slightly modified version of the workflow used in [ASoC_Demo](https://github.com/antonychiu2/ASoC_Demo), to work with the Python application in this project. The **HCL ASoC SAST Workflow** for this project is located in [.github/workflows/asoc_codebase.yml](https://github.com/glhcl/ASoCActionDemo/blob/main/.github/workflows/asoc_codebase.yml). 

### A couple key changes where required to make the workflow work with the Python application:
1. Changed the secrets.ASOC_API_KEY and secrets.ASOC_API_KEY varible names to secrets.ASOC_KEY and secrets.ASOC_KEY, respectively, to be consistent with those used in the **HCL AppScan CodeSweep Github Action** extension.
2. Modified appscan-config.xml to exlude the saclientutil, to prevent it from being scanned. The workflow is designed to download the latest version of SAClientUtil to generate the .irx in preparation for the scan. The download happens in the working directory/folder and as a result, SAClientUtil will be included in the scan.
3. Updated ASOC_APPID: [ID] to reflect the ASoC application this scan is for.
4. Removed .NET building, since it's a Python application being scanned.
5. For convienence, the push and pull_request triggers where commented out. To trigger a scan of the codebase, simply run the workflow manually.

To run the workflow manually, go to Github Actions -> HCL ASoC SAST Workflow -> Run workflow.

Instructions and resources are listed below.

* [ASoC_Demo | GitHub](https://github.com/antonychiu2/ASoC_Demo)

