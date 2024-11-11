
---

This structure keeps each component modular and self-contained, making it easy for others to understand, set up, and run the pipeline. Be sure to add `.gitignore` to avoid committing sensitive files and large data files. Once all files are organized, you can initialize a Git repository and push it to GitHub:

```bash
git init
git add .
git commit -m "Initial commit for brewery data pipeline"
git remote add origin https://github.com/adolfoeliazat/brewery-pipeline.git
git push -u origin main


---

Cloning the Git repository

```bash
git clone https://github.com/adolfoeliazat/brewery-pipeline.git
cd brewery-pipeline
