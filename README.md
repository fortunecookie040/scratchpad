# scratchpad

## Google Colab:

0. Fork this repo, so you can save changes across class sessions.
1. In Google Colab, create a new notebook.
2. Paste the following commands in a code chunk, and run it:

```python
! git clone https://github.com/<your GitHub username>/scratchpad
%run ./scratchpad/get_data.py
```

This will download and extract the course data for you.

3. When you're done, use `Save a Copy in GitHub` to save your notebook back to your `scratchpad` repo as `nb_2026_mm_dd.ipynb`.

## Rivanna HPC:

0. Fork this repo, so can clone and push easily
1. Start a VS Code Server session on Rivanna
2. Clone this repo: `git clone https://github.com/<your GitHub username>/scratchpad`
3. Open `scratchpad` in your Code Server session
4. At the command line, run `bash build.sh` ; this will build a virtual environment and download/extract your data

To get your work back to Github, at the command line, run `git push origin main`
