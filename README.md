# scratchpad

## Using Google Colab:

0. Fork this repo, so you can save changes across class sessions.
1. In Google Colab, create a new notebook.
2. Paste the following commands in a code chunk, and run it:

```python
! git clone https://github.com/<your GitHub username>/scratchpad
%run ./scratchpad/get_data.py
```

This will download and extract the course data for you.

3. When you're done, use `Save a Copy in GitHub` to save your notebook back to your `scratchpad` repo as `nb_2026_mm_dd.ipynb`.

## Using Rivanna HPC, or locally:

0. Fork this repo, so can clone and push easily
1. Start a VS Code Server session on Rivanna
2. Clone this repo:
   ```bash
   git clone https://github.com/<your GitHub username>/scratchpad
   ```
3. Open the `scratchpad` folder in your Code Server session
4. At the command line, run
   ```bash
   bash build.sh
   ```
5. This will build a virtual environment and download/extract your data
6. To save your work locally,
    ```bash
    git commit -am '<Describe your changes>'
    ```
7. To get your work back to Github, at the command line, run
    ```bash
    git push origin main
    ```
8. To get new changes to the repo, at the command line, run
    ```bash
    git pull --rebase
    ```

